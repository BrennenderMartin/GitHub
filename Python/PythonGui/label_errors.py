import numpy as np
import pandas as pd
import math
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier
from tqdm import tqdm
from cleanlab.filter import get_label_quality_scores


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

    df = load_data(path, sep, decimal)
    model = XGBClassifier(**config)

    # Split data into Trainingsdata and Labels
    X_train = df.loc[:,'Feature0':]
    y_train = df['KlasseSoll']
    cls_mapping = {cls_i: i for i, cls_i in enumerate(y_train.unique())}
    y_train = y_train.map(cls_mapping)

    # Compute Pleiss Scores
    values, probas, values_pos, values_neg = compute_AUM(X_train, y_train, model)

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
    df = load_data(path, sep, decimal)

    # Remove classes with one sample because of the cross-validation
    one_sample = df['KlasseSoll'].value_counts()>1
    df = df[df['KlasseSoll'].isin(one_sample[one_sample].index)]

    model = XGBClassifier(**config)
    pred_probs = cross_val_scores(df, model)

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

result = pleiss(path='Test5.csv',sep=',',decimal='.')
result.to_csv("Pleiss.csv", sep=';')
print(result)