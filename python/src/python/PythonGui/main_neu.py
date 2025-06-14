from typing import Tuple
import tkinter as tk
import customtkinter
from CTkListbox import *
#from PIL import Image, ImageTk
#import sqlalchemy as adb
import numpy as np
import pandas as pd
import math
#from sklearn.model_selection import StratifiedKFold
#from xgboost import XGBClassifier
#from tqdm import tqdm
#from cleanlab.filter import get_label_quality_scores

# Base XGBParams
BASE_XGB_PARAMS = {
    'booster' : 'gbtree',
    'verbosity' : 1, # display warnings
    'validate_parameters' : False,
    'nthread' : 1,

    'eta' : 0.1,
    'gamma' : 0,
    'max_depth' : 10,
    'min_child_weight' : 5, # regularization measure
    'max_delta_step' : 0,
    'subsample' : 1,
    'sampling_method' : 'uniform',
    'colsample_bytree' : 0.5, # too low?
    'colsample_bylevel' : 1.0,
    'colsample_bynode' : 1.0,
    'lambda' : 1.0,
    'alpha' : 0.0,
    'tree_method' : 'auto',
    # 'scale_pos_weight' : 1.0, # unused
    'process_type' : 'default', # new trees
    'grow_policy' : 'depthwise',
    'max_leaves' : 0,
    'max_bin' : 256,
    # predictor_type = 'cpu_predictor',
    'num_parallel_tree' : 1,

    # 'sample_type' : 'uniform', # unused? only for dart booster
    # 'normalize_type' : 'tree', # unused? only for dart booster
    # 'rate_drop' : 0.1, # unused? only for dart booster
    # 'one_drop' : 0, # unused? only for dart booster
    # 'skip_drop' : 0.5, # unused? only for dart booster

    # lambda_lin = 0.0,
    # alpha_lin = 0.0,
    # 'updater' : 'shotgun', # unused? only for linear booster == updaterLin?
    # 'feature_selector' : 'cyclic', # unused? only for linear booster
    # 'top_k' : 0, # unused? only for linear booster with greedy and thrifty feature selector

    'objective' : 'multi:softprob',
    'seed' : 0,
    'seed_per_iteration' : False,
    # 'num_round' : 100, # may by equal to n_estimators 
    'n_estimators' : 100,
    'missing' : float('nan'),

    # 'tweedie_variance_power' : 1.5, # param does not apply to multi:softprob

    # 'huber_slope' : 1.0, # unused? only for pseudo-huber booster

    # importance_type = 'weight', # ??
}
config = BASE_XGB_PARAMS.copy()
config.update({
    'device': 'cuda:0',
    # 'seed': 10,
    # 'colsample_bynode': 0.7,
    # 'n_estimators': 50,
    'n_estimators': 150,
})

class label_errors():
    def load_data(path, sep, decimal):
        """
        loads the .csv containing the data
        path: the path to the .csv
        sep: the separator that is used to separate the columns in the .csv
        decimal: the decimal used in the .csv
        returns: a pandas dataframe only containing trainings- and validation data
        """
        df = pd.read_csv(path,  sep=sep, decimal=decimal, index_col=False, names= ['GaugeID', 'DefectMapID', 'DefectID', 'CameraID', 'ImageID', 'KlasseSoll', 'KlasseIst', 'DefectStatus'] + [f'Feature{i}' for i in range(500)])

        # Drop rows that are not training or validation data
        df = df[df['DefectStatus'].isin([5,8])]

        # Drop samples that have KlasseIst or KlasseSoll as NaN
        df = df[df['KlasseSoll'].notna()]
        df = df[df['KlasseIst'].notna()]
        df.reset_index(inplace=True)
        df.drop(columns=['index'], inplace=True)

        # Drop column that are always NaN
        df.dropna(axis=1, how='all', inplace=True)

        return df

    def cross_val_scores(df, model):
        """
        Performs cross-validation on the given DataFrame
        df: DataFrame containig the data to perform cross_validation on
        model: The model that should be used for training/testing
        returns the probabilities for each sample
        """
        cls_mapping = {cls_i: i for i, cls_i in enumerate(df['KlasseSoll'].unique())}
        df['KlasseSoll'] = df['KlasseSoll'].map(cls_mapping)

        pred_prob = np.zeros((df.shape[0], df['KlasseSoll'].nunique()))
        counts = df['DefectStatus'].value_counts()
        div = math.ceil(((counts[5]+counts[8])/counts[8]))

        kfold = StratifiedKFold(div, shuffle=True)
        for i, (train_index, test_index) in enumerate(kfold.split(df.iloc[:,8:], df['KlasseSoll'])):

            model.fit(df.iloc[train_index,8:],  df.iloc[train_index,:]['KlasseSoll'])
            pred_prob[test_index] = model.predict_proba(df.iloc[test_index,8:])

        return pred_prob

    def compute_AUM(X_train, y_train, model):

        model.fit(X_train, y_train)
        
        n_estimators = model.n_estimators
        values_pos = np.zeros((X_train.shape[0], n_estimators))
        values_neg = np.zeros_like(values_pos)
        values_naive = np.zeros_like(values_pos)
        entropy = np.zeros_like(values_pos)

        # scoring adapted from Pleiss et al. 2020
        for j in tqdm(range(n_estimators)):
            intermediary_preds = model.predict_proba(X_train, iteration_range=[0, j+1])
            
            values_naive[:, j] = intermediary_preds.argmax(axis=1) == y_train # is the predicted class the labeled class

            entropy[:, j] = -np.sum(intermediary_preds * np.log(intermediary_preds), axis=1)

            gt_proba = intermediary_preds[np.arange(X_train.shape[0]), y_train]
            pred_copy = intermediary_preds.copy()
            pred_copy[np.arange(X_train.shape[0]), y_train] = 0.
            highest_non_gt_proba = pred_copy.max(axis=1)
            values_pos[:, j] = gt_proba
            values_neg[:, j] = highest_non_gt_proba

        probas = model.predict_proba(X_train)
        values = values_pos - values_neg # AUM
        return values, probas, values_pos, values_neg

    def pleiss(path, sep, decimal):
        """
        Computes the cleaniness of the samples based on the method by Pleiss et al.
        The scores are normalizes to be between 0 and 1
        0: most likely a label error
        1: least likely a label error

        Parameters:
        path: the path to the .csv
        sep: the separator that is used to separate the columns in the .csv
        decimal: the decimal used in the .csv
        Returns: a pandas dataframe with the columns: GaugeID, DefectMapID, DefectID, LabelErrorScore
        """

        df = label_errors.load_data(path, sep, decimal)
        model = XGBClassifier(**config)

        # Split data into Trainingsdata and Labels
        X_train = df.loc[:,'Feature0':]
        y_train = df['KlasseSoll']
        cls_mapping = {cls_i: i for i, cls_i in enumerate(y_train.unique())}
        y_train = y_train.map(cls_mapping)

        # Compute Pleiss Scores
        values, probas, values_pos, values_neg = label_errors.compute_AUM(X_train, y_train, model)

        # Turn into DF
        label_error_df = df.iloc[:, :3]
        label_error_df.insert(3, 'LabelErrorScore', values.mean(axis=1)) # get mean score for each sample
        label_error_df.sort_values(by='LabelErrorScore', inplace=True) # sort by score
        label_error_df['LabelErrorScore'] = [(i+abs(np.min(label_error_df['LabelErrorScore']))) for i in label_error_df['LabelErrorScore']] # normalize
        label_error_df['LabelErrorScore'] = [i/np.max(label_error_df['LabelErrorScore']) for i in label_error_df['LabelErrorScore'] ] #normalize
        
        return label_error_df

    def cleanlab(path, sep, decimal):

        """
        Computes the cleaniness of the samples using CleanLab
        The scores are normalizes to be between 0 and 1
        0: most likely a label error
        1: least likely a label error

        Parameters:
        path: the path to the .csv
        sep: the separator that is used to separate the columns in the .csv
        decimal: the decimal used in the .csv
        Returns: a pandas dataframe with the columns: GaugeID, DefectMapID, DefectID, LabelErrorScore
        """
        df = label_errors.load_data(path, sep, decimal)

        # Remove classes with one sample because of the cross-validation
        one_sample = df['KlasseSoll'].value_counts()>1
        df = df[df['KlasseSoll'].isin(one_sample[one_sample].index)]

        model = XGBClassifier(**config)
        pred_probs = label_errors.cross_val_scores(df, model)

        cls_mapping = {cls_i: i for i, cls_i in enumerate(df['KlasseSoll'].unique())}
        y_train = df['KlasseSoll'].map(cls_mapping)

        quality_scores = get_label_quality_scores(y_train, pred_probs)

        # Make sure the classes that were dropped don't get missed
        scores = np.zeros(df.shape[0])
        one_sample = df['KlasseSoll'].value_counts()==1
        dropped_index = df.index[df['KlasseSoll'].isin(one_sample[one_sample].index)].tolist()
        scores[dropped_index] = np.nan
        scores[np.setdiff1d(np.arange(df.shape[0]), dropped_index)] = quality_scores

        label_error_df = df.iloc[:, :3]
        label_error_df.insert(3, 'LabelErrorScore', scores)
        label_error_df.sort_values(by='LabelErrorScore', inplace=True)
        return label_error_df

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mein Skript")
        self.geometry("550x450")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(4, weight=0)

        self.item_label_var = tk.StringVar()
        self.var2_strvar = tk.StringVar()
        self.var4_strvar = tk.StringVar()
        self.df_strvar = tk.StringVar()
        self.cmd_strvar = tk.StringVar()

        self.create_widget()

    def create_widget(self):
        self.button_Cleanlab = customtkinter.CTkButton(self, text="Cleanlab", command=self.test)
        self.button_Cleanlab.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        self.button_ReadData = customtkinter.CTkButton(self, text="ReadData", command=self.test2)
        self.button_ReadData.grid(row=1, column=0, padx=10, pady=(10,0), sticky="ew")

        self.button_Compare = customtkinter.CTkButton(self, text="Compare", command=self.upload_database)
        self.button_Compare.grid(row=2, column=0, padx=10, pady=(10,0), sticky="ew")

        self.image = customtkinter.CTkImage(dark_image=Image.open("Image_test.jpg"), size=(300,150))
        self.image_label = customtkinter.CTkLabel(self, text=" ", image=self.image, anchor="w")
        self.image_label.grid(row=0, column=1, columnspan=2, rowspan=4, padx=10, pady=(10,0), sticky="w")

        self.item_label = customtkinter.CTkLabel(self, text="Label", anchor="w")
        self.item_label.grid(row=4, column=1, padx=10, pady=(10,0), sticky="nw")

        self.optionmenu_var = customtkinter.StringVar(value="Relabel:")
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Bruch", "Riss", "Totalschaden", "test1", "test2", "test3", "test4", "Label"], 
                                                        command=self.relabel, variable=self.optionmenu_var)
        self.optionmenu.grid(row=3, column=0, padx=10, pady=(10,0), sticky="ew")

        self.textbox = customtkinter.CTkTextbox(self, width=530)
        self.textbox.grid(row=5, column=0, columnspan=3, padx=10, pady=(10,0),sticky="nw")

        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=4, column=0, padx=10, pady=(10,0), sticky="ew")
        self.entry_frame.configure(fg_color="transparent")

        self.entry2 = customtkinter.CTkEntry(self.entry_frame, width=75, placeholder_text="column")
        self.entry2.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nw")
        self.entry = customtkinter.CTkEntry(self.entry_frame, width=75, placeholder_text="row")
        self.entry.grid(row=0, column=1, padx=10, pady=(10,0), sticky="ne")
    
    def read_database(self):
        self.cmd_strvar.set("read_database")
        def sqlconnect(serverName: str, databaseName: str, user: str, password: str):
            

            #params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverName+';DATABASE='+databaseName+';UID='+user+';PWD='+password)
            driver = "SQL Server"
            
            url = adb.URL.create(
                "mssql+pyodbc",
                username=user,
                password=password,
                database=databaseName,
                host=serverName,
                query={"driver": driver},
                )
            
            #engine = adb.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
            engine = adb.create_engine(url)
            return engine

        sn = r"SURCONSTORAGE\MUSTERTRAINING"
        dn = r'SIS_MasterTraining_HotStripMill_Test'
        user = r'sa'
        pw = r'admin4SQLServer'

        #engine = sqlconnect(sn, dn, user, pw)
        #conn = engine.connect()
        #if not conn.closed:
        #    print('connected')

        query = (""" 
                SELECT D.[GaugeID], 
                        D.[DefectMapID], 
                        D.[DefectID],
                        D.[CameraID]
                    ,D.[ImageID]
                    ,[ClassID] as KlasseSoll
                    ,[ClassTest] as KlasseIst
                    ,[DefectStatus]
                    ,[Feature0]
                    ,[Feature1]
                    ,[Feature2]
                    ,[Feature3]
                    ,[Feature4]
                    ,[Feature5]
                    ,[Feature6]
                    ,[Feature7]
                    ,[Feature8]
                    ,[Feature9]
                    ,[Feature10]
                    ,[Feature11]
                    ,[Feature12]
                    ,[Feature13]
                    ,[Feature14]
                    ,[Feature15]
                    ,[Feature16]
                    ,[Feature17]
                    ,[Feature18]
                    ,[Feature19]
                    ,[Feature20]
                    ,[Feature21]
                    ,[Feature22]
                    ,[Feature23]
                    ,[Feature24]
                    ,[Feature25]
                    ,[Feature26]
                    ,[Feature27]
                    ,[Feature28]
                    ,[Feature29]
                    ,[Feature30]
                    ,[Feature31]
                    ,[Feature32]
                    ,[Feature33]
                    ,[Feature34]
                    ,[Feature35]
                    ,[Feature36]
                    ,[Feature37]
                    ,[Feature38]
                    ,[Feature39]
                    ,[Feature40]
                    ,[Feature41]
                    ,[Feature42]
                    ,[Feature43]
                    ,[Feature44]
                    ,[Feature45]
                    ,[Feature46]
                    ,[Feature47]
                    ,[Feature48]
                    ,[Feature49]
                    ,[Feature50]
                    ,[Feature51]
                    ,[Feature52]
                    ,[Feature53]
                    ,[Feature54]
                    ,[Feature55]
                    ,[Feature56]
                    ,[Feature57]
                    ,[Feature58]
                    ,[Feature59]
                    ,[Feature60]
                    ,[Feature61]
                    ,[Feature62]
                    ,[Feature63]
                    ,[Feature64]
                    ,[Feature65]
                    ,[Feature66]
                    ,[Feature67]
                    ,[Feature68]
                    ,[Feature69]
                    ,[Feature70]
                    ,[Feature71]
                    ,[Feature72]
                    ,[Feature73]
                    ,[Feature74]
                    ,[Feature75]
                    ,[Feature76]
                    ,[Feature77]
                    ,[Feature78]
                    ,[Feature79]
                    ,[Feature80]
                    ,[Feature81]
                    ,[Feature82]
                    ,[Feature83]
                    ,[Feature84]
                    ,[Feature85]
                    ,[Feature86]
                    ,[Feature87]
                    ,[Feature88]
                    ,[Feature89]
                    ,[Feature90]
                    ,[Feature91]
                    ,[Feature92]
                    ,[Feature93]
                    ,[Feature94]
                    ,[Feature95]
                    ,[Feature96]
                    ,[Feature97]
                    ,[Feature98]
                    ,[Feature99]
                    ,[Feature100]
                    ,[Feature101]
                    ,[Feature102]
                    ,[Feature103]
                    ,[Feature104]
                    ,[Feature105]
                    ,[Feature106]
                    ,[Feature107]
                    ,[Feature108]
                    ,[Feature109]
                    ,[Feature110]
                    ,[Feature111]
                    ,[Feature112]
                    ,[Feature113]
                    ,[Feature114]
                    ,[Feature115]
                    ,[Feature116]
                    ,[Feature117]
                    ,[Feature118]
                    ,[Feature119]
                    ,[Feature120]
                    ,[Feature121]
                    ,[Feature122]
                    ,[Feature123]
                    ,[Feature124]
                    ,[Feature125]
                    ,[Feature126]
                    ,[Feature127]
                    ,[Feature128]
                    ,[Feature129]
                    ,[Feature130]
                    ,[Feature131]
                    ,[Feature132]
                    ,[Feature133]
                    ,[Feature134]
                    ,[Feature135]
                    ,[Feature136]
                    ,[Feature137]
                    ,[Feature138]
                    ,[Feature139]
                    ,[Feature140]
                    ,[Feature141]
                    ,[Feature142]
                    ,[Feature143]
                    ,[Feature144]
                    ,[Feature145]
                    ,[Feature146]
                    ,[Feature147]
                    ,[Feature148]
                    ,[Feature149]
                    ,[Feature150]
                    ,[Feature151]
                    ,[Feature152]
                    ,[Feature153]
                    ,[Feature154]
                    ,[Feature155]
                    ,[Feature156]
                    ,[Feature157]
                    ,[Feature158]
                    ,[Feature159]
                    ,[Feature160]
                    ,[Feature161]
                    ,[Feature162]
                    ,[Feature163]
                    ,[Feature164]
                    ,[Feature165]
                    ,[Feature166]
                    ,[Feature167]
                    ,[Feature168]
                    ,[Feature169]
                    ,[Feature170]
                    ,[Feature171]
                    ,[Feature172]
                    ,[Feature173]
                    ,[Feature174]
                    ,[Feature175]
                    ,[Feature176]
                    ,[Feature177]
                    ,[Feature178]
                    ,[Feature179]
                    ,[Feature180]
                    ,[Feature181]
                    ,[Feature182]
                    ,[Feature183]
                    ,[Feature184]
                    ,[Feature185]
                    ,[Feature186]
                    ,[Feature187]
                    ,[Feature188]
                    ,[Feature189]
                    ,[Feature190]
                    ,[Feature191]
                    ,[Feature192]
                    ,[Feature193]
                    ,[Feature194]
                    ,[Feature195]
                    ,[Feature196]
                    ,[Feature197]
                    ,[Feature198]
                    ,[Feature199]
                    ,[Feature200]
                    ,[Feature201]
                    ,[Feature202]
                    ,[Feature203]
                    ,[Feature204]
                    ,[Feature205]
                    ,[Feature206]
                    ,[Feature207]
                    ,[Feature208]
                    ,[Feature209]
                    ,[Feature210]
                    ,[Feature211]
                    ,[Feature212]
                    ,[Feature213]
                    ,[Feature214]
                    ,[Feature215]
                    ,[Feature216]
                    ,[Feature217]
                    ,[Feature218]
                    ,[Feature219]
                    ,[Feature220]
                    ,[Feature221]
                    ,[Feature222]
                    ,[Feature223]
                    ,[Feature224]
                    ,[Feature225]
                    ,[Feature226]
                    ,[Feature227]
                    ,[Feature228]
                    ,[Feature229]
                    ,[Feature230]
                    ,[Feature231]
                    ,[Feature232]
                    ,[Feature233]
                    ,[Feature234]
                    ,[Feature235]
                    ,[Feature236]
                    ,[Feature237]
                    ,[Feature238]
                    ,[Feature239]
                    ,[Feature240]
                    ,[Feature241]
                    ,[Feature242]
                    ,[Feature243]
                    ,[Feature244]
                    ,[Feature245]
                    ,[Feature246]
                    ,[Feature247]
                    ,[Feature248]
                    ,[Feature249]
                    ,[Feature250]
                    ,[Feature251]
                    ,[Feature252]
                    ,[Feature253]
                    ,[Feature254]
                    ,[Feature255]
                    ,[Feature256]
                    ,[Feature257]
                    ,[Feature258]
                    ,[Feature259]
                    ,[Feature260]
                    ,[Feature261]
                    ,[Feature262]
                    ,[Feature263]
                    ,[Feature264]
                    ,[Feature265]
                    ,[Feature266]
                    ,[Feature267]
                    ,[Feature268]
                    ,[Feature269]
                    ,[Feature270]
                    ,[Feature271]
                    ,[Feature272]
                    ,[Feature273]
                    ,[Feature274]
                    ,[Feature275]
                    ,[Feature276]
                    ,[Feature277]
                    ,[Feature278]
                    ,[Feature279]
                    ,[Feature280]
                    ,[Feature281]
                    ,[Feature282]
                    ,[Feature283]
                    ,[Feature284]
                    ,[Feature285]
                    ,[Feature286]
                    ,[Feature287]
                    ,[Feature288]
                    ,[Feature289]
                    ,[Feature290]
                    ,[Feature291]
                    ,[Feature292]
                    ,[Feature293]
                    ,[Feature294]
                    ,[Feature295]
                    ,[Feature296]
                    ,[Feature297]
                    ,[Feature298]
                    ,[Feature299]
                    ,[Feature300]
                    ,[Feature301]
                    ,[Feature302]
                    ,[Feature303]
                    ,[Feature304]
                    ,[Feature305]
                    ,[Feature306]
                    ,[Feature307]
                    ,[Feature308]
                    ,[Feature309]
                    ,[Feature310]
                    ,[Feature311]
                    ,[Feature312]
                    ,[Feature313]
                    ,[Feature314]
                    ,[Feature315]
                    ,[Feature316]
                    ,[Feature317]
                    ,[Feature318]
                    ,[Feature319]
                    ,[Feature320]
                    ,[Feature321]
                    ,[Feature322]
                    ,[Feature323]
                    ,[Feature324]
                    ,[Feature325]
                    ,[Feature326]
                    ,[Feature327]
                    ,[Feature328]
                    ,[Feature329]
                    ,[Feature330]
                    ,[Feature331]
                    ,[Feature332]
                    ,[Feature333]
                    ,[Feature334]
                    ,[Feature335]
                    ,[Feature336]
                    ,[Feature337]
                    ,[Feature338]
                    ,[Feature339]
                    ,[Feature340]
                    ,[Feature341]
                    ,[Feature342]
                    ,[Feature343]
                    ,[Feature344]
                    ,[Feature345]
                    ,[Feature346]
                    ,[Feature347]
                    ,[Feature348]
                    ,[Feature349]
                    ,[Feature350]
                    ,[Feature351]
                    ,[Feature352]
                    ,[Feature353]
                    ,[Feature354]
                    ,[Feature355]
                    ,[Feature356]
                    ,[Feature357]
                    ,[Feature358]
                    ,[Feature359]
                    ,[Feature360]
                    ,[Feature361]
                    ,[Feature362]
                    ,[Feature363]
                    ,[Feature364]
                    ,[Feature365]
                    ,[Feature366]
                    ,[Feature367]
                    ,[Feature368]
                    ,[Feature369]
                    ,[Feature370]
                    ,[Feature371]
                    ,[Feature372]
                    ,[Feature373]
                    ,[Feature374]
                    ,[Feature375]
                    ,[Feature376]
                    ,[Feature377]
                    ,[Feature378]
                    ,[Feature379]
                    ,[Feature380]
                    ,[Feature381]
                    ,[Feature382]
                    ,[Feature383]
                    ,[Feature384]
                    ,[Feature385]
                    ,[Feature386]
                    ,[Feature387]
                    ,[Feature388]
                    ,[Feature389]
                    ,[Feature390]
                    ,[Feature391]
                    ,[Feature392]
                    ,[Feature393]
                    ,[Feature394]
                    ,[Feature395]
                    ,[Feature396]
                    ,[Feature397]
                    ,[Feature398]
                    ,[Feature399]
                    ,[Feature400]
                    ,[Feature401]
                    ,[Feature402]
                    ,[Feature403]
                    ,[Feature404]
                    ,[Feature405]
                    ,[Feature406]
                    ,[Feature407]
                    ,[Feature408]
                    ,[Feature409]
                    ,[Feature410]
                    ,[Feature411]
                    ,[Feature412]
                    ,[Feature413]
                    ,[Feature414]
                    ,[Feature415]
                    ,[Feature416]
                    ,[Feature417]
                    ,[Feature418]
                    ,[Feature419]
                    ,[Feature420]
                    ,[Feature421]
                    ,[Feature422]
                    ,[Feature423]
                    ,[Feature424]
                    ,[Feature425]
                    ,[Feature426]
                    ,[Feature427]
                    ,[Feature428]
                    ,[Feature429]
                    ,[Feature430]
                    ,[Feature431]
                    ,[Feature432]
                    ,[Feature433]
                    ,[Feature434]
                    ,[Feature435]
                    ,[Feature436]
                    ,[Feature437]
                    ,[Feature438]
                    ,[Feature439]
                    ,[Feature440]
                    ,[Feature441]
                    ,[Feature442]
                    ,[Feature443]
                    ,[Feature444]
                    ,[Feature445]
                    ,[Feature446]
                    ,[Feature447]
                    ,[Feature448]
                    ,[Feature449]
                    ,[Feature450]
                    ,[Feature451]
                    ,[Feature452]
                    ,[Feature453]
                    ,[Feature454]
                    ,[Feature455]
                    ,[Feature456]
                    ,[Feature457]
                    ,[Feature458]
                    ,[Feature459]
                    ,[Feature460]
                    ,[Feature461]
                    ,[Feature462]
                    ,[Feature463]
                    ,[Feature464]
                    ,[Feature465]
                    ,[Feature466]
                    ,[Feature467]
                    ,[Feature468]
                    ,[Feature469]
                    ,[Feature470]
                    ,[Feature471]
                    ,[Feature472]
                    ,[Feature473]
                    ,[Feature474]
                    ,[Feature475]
                    ,[Feature476]
                    ,[Feature477]
                    ,[Feature478]
                    ,[Feature479]
                    ,[Feature480]
                    ,[Feature481]
                    ,[Feature482]
                    ,[Feature483]
                    ,[Feature484]
                    ,[Feature485]
                    ,[Feature486]
                    ,[Feature487]
                    ,[Feature488]
                    ,[Feature489]
                    ,[Feature490]
                    ,[Feature491]
                    ,[Feature492]
                    ,[Feature493]
                    ,[Feature494]
                    ,[Feature495]
                    ,[Feature496]
                    ,[Feature497]
                    ,[Feature498]
                    ,[Feature499]
                FROM [dbo].[Defect] as D INNER JOIN [dbo].[FeatureVector] as F ON (D.GaugeID = F.GaugeID AND D.DefectMapID = F.DefectMapID AND D.DefectID = F.DefectID) 
                """)
        #df=pd.read_sql(query, conn)

        #conn.close()
        
        daten = pd.read_csv("Test14.csv", sep=",")
        df = pd.DataFrame(daten)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", df)

    def ex_cleanlab(self): # Funktion read Database
        self.cmd_strvar.set("ex_cleanlab")
        print("Works")

        #result = label_errors.cleanlab(path='Test5.csv',sep=',',decimal='.')
        result = pd.read_csv("Cleanlab.csv", header=1)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", result)

    def relabel(self, choice): # Funktion zum Relabel mit optionmenu
        print("optionmenu dropdown clicked:", choice)
        self.item_label_var.set(choice)
        self.item_label.configure(text=self.item_label_var.get()) 

        self.df.iat[self.var4, self.var2] = choice
        self.choice = choice
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", self.df[["Index","GaugeID","DefectMapID","DefectID","LabelErrorScore","Label"]])

        """
        #self.cmd_var = self.cmd_strvar.get()
        #self.cmd_strvar.set("nichts")

        #if self.cmd_var == "read_database":
        #    daten = daten

        #if self.cmd_var == "ex_cleanlab":
        #    daten = pd.read_csv("Test14.csv", sep=";")
        #    df = pd.DataFrame(daten)
        #    df.iat[self.var4, self.var2] = choice
        #    df.to_csv("Test14.csv", sep=";", index=False)
        """
        
        daten = pd.read_csv("Test9.csv", sep=";")
        df = pd.DataFrame(daten)
        df.iat[self.var4, self.var2] = choice
        df.to_csv("Test9.csv", sep=";", index=False)

    def test(self):
        """
        self.daten = {
            "Index": [4804,1195,5605,5698],
            "GaugeID": [13013201, 12389201, 13421611, 13421611],
            "DefectMapID": [579178, 245753, 50967, 63618],
            "DefectID": [1761, 1085, 51, 6],
            "LabelErrorScore": [7.733031088719144e-05, 0.0006918385624885559, 0.0007425202056765556, 0.0008408152498304844],
            "Image": ["Image_test.jpg", "Image_test2.jpg", "Image_test3.jpg", "Image_test4.jpg"]
        }
        """
        
        self.daten = pd.read_csv("Test9.csv", sep=";")
        self.df = pd.DataFrame(self.daten)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", self.df[["Index","GaugeID","DefectMapID","DefectID","LabelErrorScore","Label"]])

        self.var1 = self.entry2.get()
        if self.var1 == "Index" or self.var1 == "1":
            self.var2 = 0
        elif self.var1 == "GaugeID" or self.var1 == "2":
            self.var2 = 1
        elif self.var1 == "DefectMapID" or self.var1 == "3":
            self.var2 = 2
        elif self.var1 == "DefectID" or self.var1 == "4":
            self.var2 = 3
        elif self.var1 == "LabelErrorScore" or self.var1 == "5":
            self.var2 = 4
        elif self.var1 == "Label" or self.var1 == "6":
            self.var2 = 5
        else:
            return self.var1
    
        self.var3 = self.entry.get()
        self.var4 = int(self.var3)

        self.var2_strvar.set(self.var2)
        self.var4_strvar.set(self.var4)
        
        wert = self.df.iat[self.var4, self.var2]
        
        self.item_label_var.set(wert)
        self.item_label.configure(text=wert)
        self.show_row = self.df.iloc[self.var4, 0:6]
        print(self.show_row) #Row
        im_var = self.df.iat[self.var4, 6]
        self.image.configure(dark_image=Image.open(im_var))

    def test2(self):
        """
        daten = {
            "Name": ["Alice", "Bob", "Charlie"],
            "Alter": [30, 25, 22],
            "Stadt": ["Berlin", "München", "Köln"],
        }
        """
        daten = pd.read_csv("Test9_1.csv", sep=";")
        df = pd.DataFrame(daten)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", df[["Index", "GaugeID", "DefectMapID", "DefectID", "LabelErrorScore", "Label"]])
        """
        [["Index", "GaugeID", "DefectMapID", "DefectID", "LabelErrorScore", "Label"]]
        var1 = self.entry2.get()
        if var1 == "0" or var1 == "Name":
            var2 = 0
        elif var1 == "1" or var1 == "Alter":
            var2 = 1
        elif var1 == "2" or var1 == "Stadt":
            var2 = 2
        else:
            return var1
        print(var2)
    
        var3 = self.entry.get()
        if var3 == "0":
            var4 = 0
        elif var3 == "1":
            var4 = 1
        elif var3 == "2":
            var4 = 2
        else:
            return var3
        print(var4)
        
        wert = df.iat[var4, var2]
        
        self.item_label_var.set(wert)
        self.item_label.configure(text=wert)
        print(df.iat[var2, var4])
        print("")
        print(df.iloc[:, var2]) #Column
        print("")
        print(df.iloc[var2]) #Row
        """
    
    def test3(self):
        #daten = pd.read_csv("Test9.csv", sep=";")
        daten2 = pd.read_csv("Test9_1.csv", sep=";")
        #df = pd.DataFrame(daten)
        df2 = pd.DataFrame(daten2)
        #att1 = str(df.loc[self.var4, "GaugeID":"DefectID"])
        #att2 = str(df2.loc[self.var4, "GaugeID":"DefectID"])
        #print(att1)
        #print(att2)
        #if att1 == att2:

        var1 = self.entry2.get()
        var3 = self.entry.get()
        var4 = int(var3)
        df2.at[var4, var1] = self.choice
        df2.to_csv("Test9_1.csv", sep=";")

    def upload_database(self):
        def sqlconnect(serverName: str, databaseName: str, user: str, password: str):
            """sql connection method"""

            #params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverName+';DATABASE='+databaseName+';UID='+user+';PWD='+password)
            driver = "SQL Server"
            
            url = adb.URL.create(
                "mssql+pyodbc",
                username=user,
                password=password,
                database=databaseName,
                host=serverName,
                query={"driver": driver},
                )
            
            #engine = adb.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
            engine = adb.create_engine(url)
            return engine

        sn = r"SURCONSTORAGE\MUSTERTRAINING"
        dn = r'SIS_MasterTraining_HotStripMill_Test'
        user = r'sa'
        pw = r'admin4SQLServer'

        engine = sqlconnect(sn, dn, user, pw)
        conn = engine.connect()
        if not conn.closed:
            print('connected')

        query = (""" 
                SELECT D.[GaugeID], 
                        D.[DefectMapID], 
                        D.[DefectID],
                        D.[CameraID]
                    ,D.[ImageID]
                    ,[ClassID] as KlasseSoll
                    ,[ClassTest] as KlasseIst
                    ,[DefectStatus]
                    ,[Feature0]
                    ,[Feature1]
                    ,[Feature2]
                    ,[Feature3]
                    ,[Feature4]
                    ,[Feature5]
                    ,[Feature6]
                    ,[Feature7]
                    ,[Feature8]
                    ,[Feature9]
                    ,[Feature10]
                    ,[Feature11]
                    ,[Feature12]
                    ,[Feature13]
                    ,[Feature14]
                    ,[Feature15]
                    ,[Feature16]
                    ,[Feature17]
                    ,[Feature18]
                    ,[Feature19]
                    ,[Feature20]
                    ,[Feature21]
                    ,[Feature22]
                    ,[Feature23]
                    ,[Feature24]
                    ,[Feature25]
                    ,[Feature26]
                    ,[Feature27]
                    ,[Feature28]
                    ,[Feature29]
                    ,[Feature30]
                    ,[Feature31]
                    ,[Feature32]
                    ,[Feature33]
                    ,[Feature34]
                    ,[Feature35]
                    ,[Feature36]
                    ,[Feature37]
                    ,[Feature38]
                    ,[Feature39]
                    ,[Feature40]
                    ,[Feature41]
                    ,[Feature42]
                    ,[Feature43]
                    ,[Feature44]
                    ,[Feature45]
                    ,[Feature46]
                    ,[Feature47]
                    ,[Feature48]
                    ,[Feature49]
                    ,[Feature50]
                    ,[Feature51]
                    ,[Feature52]
                    ,[Feature53]
                    ,[Feature54]
                    ,[Feature55]
                    ,[Feature56]
                    ,[Feature57]
                    ,[Feature58]
                    ,[Feature59]
                    ,[Feature60]
                    ,[Feature61]
                    ,[Feature62]
                    ,[Feature63]
                    ,[Feature64]
                    ,[Feature65]
                    ,[Feature66]
                    ,[Feature67]
                    ,[Feature68]
                    ,[Feature69]
                    ,[Feature70]
                    ,[Feature71]
                    ,[Feature72]
                    ,[Feature73]
                    ,[Feature74]
                    ,[Feature75]
                    ,[Feature76]
                    ,[Feature77]
                    ,[Feature78]
                    ,[Feature79]
                    ,[Feature80]
                    ,[Feature81]
                    ,[Feature82]
                    ,[Feature83]
                    ,[Feature84]
                    ,[Feature85]
                    ,[Feature86]
                    ,[Feature87]
                    ,[Feature88]
                    ,[Feature89]
                    ,[Feature90]
                    ,[Feature91]
                    ,[Feature92]
                    ,[Feature93]
                    ,[Feature94]
                    ,[Feature95]
                    ,[Feature96]
                    ,[Feature97]
                    ,[Feature98]
                    ,[Feature99]
                    ,[Feature100]
                    ,[Feature101]
                    ,[Feature102]
                    ,[Feature103]
                    ,[Feature104]
                    ,[Feature105]
                    ,[Feature106]
                    ,[Feature107]
                    ,[Feature108]
                    ,[Feature109]
                    ,[Feature110]
                    ,[Feature111]
                    ,[Feature112]
                    ,[Feature113]
                    ,[Feature114]
                    ,[Feature115]
                    ,[Feature116]
                    ,[Feature117]
                    ,[Feature118]
                    ,[Feature119]
                    ,[Feature120]
                    ,[Feature121]
                    ,[Feature122]
                    ,[Feature123]
                    ,[Feature124]
                    ,[Feature125]
                    ,[Feature126]
                    ,[Feature127]
                    ,[Feature128]
                    ,[Feature129]
                    ,[Feature130]
                    ,[Feature131]
                    ,[Feature132]
                    ,[Feature133]
                    ,[Feature134]
                    ,[Feature135]
                    ,[Feature136]
                    ,[Feature137]
                    ,[Feature138]
                    ,[Feature139]
                    ,[Feature140]
                    ,[Feature141]
                    ,[Feature142]
                    ,[Feature143]
                    ,[Feature144]
                    ,[Feature145]
                    ,[Feature146]
                    ,[Feature147]
                    ,[Feature148]
                    ,[Feature149]
                    ,[Feature150]
                    ,[Feature151]
                    ,[Feature152]
                    ,[Feature153]
                    ,[Feature154]
                    ,[Feature155]
                    ,[Feature156]
                    ,[Feature157]
                    ,[Feature158]
                    ,[Feature159]
                    ,[Feature160]
                    ,[Feature161]
                    ,[Feature162]
                    ,[Feature163]
                    ,[Feature164]
                    ,[Feature165]
                    ,[Feature166]
                    ,[Feature167]
                    ,[Feature168]
                    ,[Feature169]
                    ,[Feature170]
                    ,[Feature171]
                    ,[Feature172]
                    ,[Feature173]
                    ,[Feature174]
                    ,[Feature175]
                    ,[Feature176]
                    ,[Feature177]
                    ,[Feature178]
                    ,[Feature179]
                    ,[Feature180]
                    ,[Feature181]
                    ,[Feature182]
                    ,[Feature183]
                    ,[Feature184]
                    ,[Feature185]
                    ,[Feature186]
                    ,[Feature187]
                    ,[Feature188]
                    ,[Feature189]
                    ,[Feature190]
                    ,[Feature191]
                    ,[Feature192]
                    ,[Feature193]
                    ,[Feature194]
                    ,[Feature195]
                    ,[Feature196]
                    ,[Feature197]
                    ,[Feature198]
                    ,[Feature199]
                    ,[Feature200]
                    ,[Feature201]
                    ,[Feature202]
                    ,[Feature203]
                    ,[Feature204]
                    ,[Feature205]
                    ,[Feature206]
                    ,[Feature207]
                    ,[Feature208]
                    ,[Feature209]
                    ,[Feature210]
                    ,[Feature211]
                    ,[Feature212]
                    ,[Feature213]
                    ,[Feature214]
                    ,[Feature215]
                    ,[Feature216]
                    ,[Feature217]
                    ,[Feature218]
                    ,[Feature219]
                    ,[Feature220]
                    ,[Feature221]
                    ,[Feature222]
                    ,[Feature223]
                    ,[Feature224]
                    ,[Feature225]
                    ,[Feature226]
                    ,[Feature227]
                    ,[Feature228]
                    ,[Feature229]
                    ,[Feature230]
                    ,[Feature231]
                    ,[Feature232]
                    ,[Feature233]
                    ,[Feature234]
                    ,[Feature235]
                    ,[Feature236]
                    ,[Feature237]
                    ,[Feature238]
                    ,[Feature239]
                    ,[Feature240]
                    ,[Feature241]
                    ,[Feature242]
                    ,[Feature243]
                    ,[Feature244]
                    ,[Feature245]
                    ,[Feature246]
                    ,[Feature247]
                    ,[Feature248]
                    ,[Feature249]
                    ,[Feature250]
                    ,[Feature251]
                    ,[Feature252]
                    ,[Feature253]
                    ,[Feature254]
                    ,[Feature255]
                    ,[Feature256]
                    ,[Feature257]
                    ,[Feature258]
                    ,[Feature259]
                    ,[Feature260]
                    ,[Feature261]
                    ,[Feature262]
                    ,[Feature263]
                    ,[Feature264]
                    ,[Feature265]
                    ,[Feature266]
                    ,[Feature267]
                    ,[Feature268]
                    ,[Feature269]
                    ,[Feature270]
                    ,[Feature271]
                    ,[Feature272]
                    ,[Feature273]
                    ,[Feature274]
                    ,[Feature275]
                    ,[Feature276]
                    ,[Feature277]
                    ,[Feature278]
                    ,[Feature279]
                    ,[Feature280]
                    ,[Feature281]
                    ,[Feature282]
                    ,[Feature283]
                    ,[Feature284]
                    ,[Feature285]
                    ,[Feature286]
                    ,[Feature287]
                    ,[Feature288]
                    ,[Feature289]
                    ,[Feature290]
                    ,[Feature291]
                    ,[Feature292]
                    ,[Feature293]
                    ,[Feature294]
                    ,[Feature295]
                    ,[Feature296]
                    ,[Feature297]
                    ,[Feature298]
                    ,[Feature299]
                    ,[Feature300]
                    ,[Feature301]
                    ,[Feature302]
                    ,[Feature303]
                    ,[Feature304]
                    ,[Feature305]
                    ,[Feature306]
                    ,[Feature307]
                    ,[Feature308]
                    ,[Feature309]
                    ,[Feature310]
                    ,[Feature311]
                    ,[Feature312]
                    ,[Feature313]
                    ,[Feature314]
                    ,[Feature315]
                    ,[Feature316]
                    ,[Feature317]
                    ,[Feature318]
                    ,[Feature319]
                    ,[Feature320]
                    ,[Feature321]
                    ,[Feature322]
                    ,[Feature323]
                    ,[Feature324]
                    ,[Feature325]
                    ,[Feature326]
                    ,[Feature327]
                    ,[Feature328]
                    ,[Feature329]
                    ,[Feature330]
                    ,[Feature331]
                    ,[Feature332]
                    ,[Feature333]
                    ,[Feature334]
                    ,[Feature335]
                    ,[Feature336]
                    ,[Feature337]
                    ,[Feature338]
                    ,[Feature339]
                    ,[Feature340]
                    ,[Feature341]
                    ,[Feature342]
                    ,[Feature343]
                    ,[Feature344]
                    ,[Feature345]
                    ,[Feature346]
                    ,[Feature347]
                    ,[Feature348]
                    ,[Feature349]
                    ,[Feature350]
                    ,[Feature351]
                    ,[Feature352]
                    ,[Feature353]
                    ,[Feature354]
                    ,[Feature355]
                    ,[Feature356]
                    ,[Feature357]
                    ,[Feature358]
                    ,[Feature359]
                    ,[Feature360]
                    ,[Feature361]
                    ,[Feature362]
                    ,[Feature363]
                    ,[Feature364]
                    ,[Feature365]
                    ,[Feature366]
                    ,[Feature367]
                    ,[Feature368]
                    ,[Feature369]
                    ,[Feature370]
                    ,[Feature371]
                    ,[Feature372]
                    ,[Feature373]
                    ,[Feature374]
                    ,[Feature375]
                    ,[Feature376]
                    ,[Feature377]
                    ,[Feature378]
                    ,[Feature379]
                    ,[Feature380]
                    ,[Feature381]
                    ,[Feature382]
                    ,[Feature383]
                    ,[Feature384]
                    ,[Feature385]
                    ,[Feature386]
                    ,[Feature387]
                    ,[Feature388]
                    ,[Feature389]
                    ,[Feature390]
                    ,[Feature391]
                    ,[Feature392]
                    ,[Feature393]
                    ,[Feature394]
                    ,[Feature395]
                    ,[Feature396]
                    ,[Feature397]
                    ,[Feature398]
                    ,[Feature399]
                    ,[Feature400]
                    ,[Feature401]
                    ,[Feature402]
                    ,[Feature403]
                    ,[Feature404]
                    ,[Feature405]
                    ,[Feature406]
                    ,[Feature407]
                    ,[Feature408]
                    ,[Feature409]
                    ,[Feature410]
                    ,[Feature411]
                    ,[Feature412]
                    ,[Feature413]
                    ,[Feature414]
                    ,[Feature415]
                    ,[Feature416]
                    ,[Feature417]
                    ,[Feature418]
                    ,[Feature419]
                    ,[Feature420]
                    ,[Feature421]
                    ,[Feature422]
                    ,[Feature423]
                    ,[Feature424]
                    ,[Feature425]
                    ,[Feature426]
                    ,[Feature427]
                    ,[Feature428]
                    ,[Feature429]
                    ,[Feature430]
                    ,[Feature431]
                    ,[Feature432]
                    ,[Feature433]
                    ,[Feature434]
                    ,[Feature435]
                    ,[Feature436]
                    ,[Feature437]
                    ,[Feature438]
                    ,[Feature439]
                    ,[Feature440]
                    ,[Feature441]
                    ,[Feature442]
                    ,[Feature443]
                    ,[Feature444]
                    ,[Feature445]
                    ,[Feature446]
                    ,[Feature447]
                    ,[Feature448]
                    ,[Feature449]
                    ,[Feature450]
                    ,[Feature451]
                    ,[Feature452]
                    ,[Feature453]
                    ,[Feature454]
                    ,[Feature455]
                    ,[Feature456]
                    ,[Feature457]
                    ,[Feature458]
                    ,[Feature459]
                    ,[Feature460]
                    ,[Feature461]
                    ,[Feature462]
                    ,[Feature463]
                    ,[Feature464]
                    ,[Feature465]
                    ,[Feature466]
                    ,[Feature467]
                    ,[Feature468]
                    ,[Feature469]
                    ,[Feature470]
                    ,[Feature471]
                    ,[Feature472]
                    ,[Feature473]
                    ,[Feature474]
                    ,[Feature475]
                    ,[Feature476]
                    ,[Feature477]
                    ,[Feature478]
                    ,[Feature479]
                    ,[Feature480]
                    ,[Feature481]
                    ,[Feature482]
                    ,[Feature483]
                    ,[Feature484]
                    ,[Feature485]
                    ,[Feature486]
                    ,[Feature487]
                    ,[Feature488]
                    ,[Feature489]
                    ,[Feature490]
                    ,[Feature491]
                    ,[Feature492]
                    ,[Feature493]
                    ,[Feature494]
                    ,[Feature495]
                    ,[Feature496]
                    ,[Feature497]
                    ,[Feature498]
                    ,[Feature499]
                FROM [dbo].[Defect] as D INNER JOIN [dbo].[FeatureVector] as F ON (D.GaugeID = F.GaugeID AND D.DefectMapID = F.DefectMapID AND D.DefectID = F.DefectID) 
                """)
        data=pd.read_sql(query, conn)
        print("Step1")
        df = pd.DataFrame(data)
        df.iat[1,1] = 66
        df.to_sql(name="tabelle", con=conn, if_exists="append")
        print("Step2")
        conn.close()
        print("Step3")

customtkinter.set_appearance_mode("dark")
if __name__ == "__main__":
    app = App()
    app.mainloop()