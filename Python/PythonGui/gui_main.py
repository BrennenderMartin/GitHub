import customtkinter
import os
#from PIL import Image, ImageTk
#from lib.outlier_detection.cleanlab import *


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Surcon Software Collection")
        self.geometry("820x500")
        d = os.getcwd()
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        file_path = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(file_path,"..", "lib\src_images")
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "background.png")), size=(600, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.sql_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "sql_dark.png")), 
                                                 dark_image=Image.open(os.path.join(image_path, "sql_light.png")), size=(20, 20))
        self.yolo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "yolo_dark.png")), 
                                                 dark_image=Image.open(os.path.join(image_path, "yolo_light.png")), size=(20, 20))
        self.cleanlab_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "cleanlab.png")), 
                                                     dark_image=Image.open(os.path.join(image_path, "cleanlab.png")), size=(20, 20))
        self.pleiss_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "pleiss_dark.png")), 
                                                     dark_image=Image.open(os.path.join(image_path, "pleiss_light.png")), size=(20, 20))
        self.settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "gear_dark.png")), 
                                                     dark_image=Image.open(os.path.join(image_path, "gear_light.png")), size=(20, 20))

        icon_path = os.path.join(image_path, "IMS_surcon_logo_small.png")
        photo = ImageTk.PhotoImage(file=icon_path)
        self.after(300, lambda :self.iconphoto(False, photo))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Software Collection", 
                                    image=None, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                    text="SQL Connection", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                    image=self.sql_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                    text="YoloV8", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                    image=self.yolo_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                    text="Cleanlab", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                    image=self.cleanlab_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                    text="Pleiss", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                    image=self.pleiss_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        
        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                    text="Settings", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                    image=self.settings_image, anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create sql frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=0)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="SQL Settings", image=self.large_test_image)
        self.home_frame_large_image_label.configure(font = ("Segoe UI", 30))
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10, columnspan = 2)

        self.home_frame_label_1 = customtkinter.CTkLabel(self.home_frame,text="Server:")
        self.home_frame_label_1.grid(row=1, column=0, padx=20, pady=10, sticky = 'e')
        self.home_frame_label_1.configure(font = ("Segoe UI", 18))
        self.home_frame_label_2 = customtkinter.CTkLabel(self.home_frame, text="Database:")
        self.home_frame_label_2.grid(row=2, column=0, padx=20, pady=10, sticky = 'e')
        self.home_frame_label_2.configure(font = ("Segoe UI", 18))
        self.home_frame_label_3 = customtkinter.CTkLabel(self.home_frame, text="Use Windows Authentication:")
        self.home_frame_label_3.grid(row=3, column=0, padx=20, pady=10, sticky = 'e')
        self.home_frame_label_3.configure(font = ("Segoe UI", 18))
        self.home_frame_label_4 = customtkinter.CTkLabel(self.home_frame, text="User:")
        self.home_frame_label_4.grid(row=4, column=0, padx=20, pady=10, sticky = 'e')
        self.home_frame_label_4.configure(font = ("Segoe UI", 18))
        self.home_frame_label_5 = customtkinter.CTkLabel(self.home_frame, text="Password:")
        self.home_frame_label_5.grid(row=5, column=0, padx=20, pady=10, sticky = 'e')
        self.home_frame_label_5.configure(font = ("Segoe UI", 18))
        
        self.server_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text=SQL.DEFAULT_SERVER)
        self.server_entry.grid(row=1, column=1, padx=10, pady=(15, 15), sticky = 'w')
        self.server_entry.insert(-1, SQL.DEFAULT_SERVER)
        self.database_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text=SQL.DEFAULT_DATABASE)
        self.database_entry.grid(row=2, column=1, padx=10, pady=(15, 15), sticky = 'w')
        self.database_entry.insert(-1, SQL.DEFAULT_DATABASE)
        self.checkbox_windows = customtkinter.CTkCheckBox(self.home_frame, text="")
        self.checkbox_windows.grid(row=3, column=1, pady=(5, 0), padx=10, sticky = 'w')
        self.checkbox_windows.select()
        self.username_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="User")
        self.username_entry.grid(row=4, column=1, padx=10, pady=(15, 15), sticky = 'w')
        self.password_entry = customtkinter.CTkEntry(self.home_frame, width=200, show='*', placeholder_text="Password")
        self.password_entry.grid(row=5, column=1, padx=10, pady=(15, 15), sticky = 'w')

        # create Yolo frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=0)
        
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="YoloV8", image=self.large_test_image)
        self.second_frame_large_image_label.configure(font = ("Segoe UI", 30))
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create Cleanlab frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=0)
        
        self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="CleanLab", image=self.large_test_image)
        self.third_frame_large_image_label.configure(font = ("Segoe UI", 30))
        self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        #test start
        self.third_frame_get_data_button = customtkinter.CTkButton(self.third_frame, width=60, text='Get Data', command=self.frame_3_get_data_event)
        self.third_frame_get_data_button.grid(row=2, column=0, pady=10)
        
        self.third_frame_text = customtkinter.CTkTextbox(self.third_frame, width=400)
        self.third_frame_text.grid(row=1, column=0, pady=10, sticky='sew')
        #test end
        
        # create Pleiss frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=0)
        
        self.fourth_frame_large_image_label = customtkinter.CTkLabel(self.fourth_frame, text="Pleiss", image=self.large_test_image)
        self.fourth_frame_large_image_label.configure(font = ("Segoe UI", 30))
        self.fourth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        #create settings frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_columnconfigure(0, weight=0)
        
        self.fifth_frame_large_image_label = customtkinter.CTkLabel(self.fifth_frame, text="Settings", image=self.large_test_image)
        self.fifth_frame_large_image_label.configure(font = ("Segoe UI", 30))
        self.fifth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        # select default frame
        self.select_frame_by_name("sql")

    #frame switch
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "sql" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "yolo" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "cleanlab" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "pleiss" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # show selected frame
        if name == "sql":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "yolo":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "cleanlab":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "pleiss":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "settings":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")    
        else:
            self.fifth_frame.grid_forget()
    
    #button events
    #frames
    def home_button_event(self):
        self.select_frame_by_name("sql")

    def frame_2_button_event(self):
        self.select_frame_by_name("yolo")

    def frame_3_button_event(self):
        self.select_frame_by_name("cleanlab")
        
    def frame_4_button_event(self):
        self.select_frame_by_name("pleiss")
        
    def frame_5_button_event(self):
        self.select_frame_by_name("settings")
    
    #other buttons  
    def frame_3_get_data_event(self):
        result = Cleanlab.get_test_data(server=self.server_entry.get(), database=self.database_entry.get())
        self.third_frame_text.delete("0.0", customtkinter.END)
        self.third_frame_text.insert("0.0", result)

    #change dark / light mode
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

