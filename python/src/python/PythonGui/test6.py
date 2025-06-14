from typing import Tuple
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import customtkinter
from CTkListbox import *
#from PIL import Image, ImageTk

class FrameEins(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widget()

    def create_widget(self):
        listbox = CTkListbox(self, command=self.show_value)
        listbox.pack(fill="both", expand=True, padx=10, pady=10)
        for i in range(8):
            listbox.insert(i, f"Option {i}")
        listbox.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")

        button = customtkinter.CTkButton(self, text="my button", command=self.read_database)
        button.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
    
    def show_value(self, selected_option): # Funktion Database einzelne Objekte
        print(selected_option)

    def read_database(self): # Funktion read Database
        print("Works")

class FrameZwei(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.item_label_var = tk.StringVar()
        
        self.create_widget()

    def create_widget(self):
        #image = customtkinter.CTkImage(Image.open("Image_test.jpg"), size=(300,150))
        #image_label = customtkinter.CTkLabel(self, text=" ", image=image)
        #image_label.grid(row=0, column=0, padx=0, pady=(10,0), sticky="w")

        relabel_label = customtkinter.CTkLabel(self, text="Relabel:", anchor="w")
        relabel_label.grid(row=1, column=0, padx=10, pady=(10,0), sticky="nw")

        self.item_label = customtkinter.CTkLabel(self, anchor="e")
        self.item_label.grid(row=1, column=0, padx=100, pady=(10,0), sticky="n")

        optionmenu_var = customtkinter.StringVar()
        optionmenu = customtkinter.CTkOptionMenu(self, values=["Bruch", "Riss", "Totalschaden", "test1", "test2", "test3", "test4"], 
                                                      command=self.optionmenu_callback, 
                                                      variable=optionmenu_var)
        optionmenu.grid(row=2, column=0, padx=0, pady=(10,10), sticky="nw")
    
    def optionmenu_callback(self, choice): # Funktion zum Relabel mit optionmenu
        print("optionmenu dropdown clicked:", choice)
        self.item_label_var.set(choice)
        self.item_label.configure(text=self.item_label_var.get())


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mein Skript")
        self.geometry("550x300")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.create_widget()

    def create_widget(self):
        self.FrameEins = FrameEins(self)
        self.FrameEins.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")
        self.FrameEins.configure(fg_color="transparent")

        self.FrameZwei = FrameZwei(self)
        self.FrameZwei.grid(row=0, column=1, padx=10, pady=(10,0), sticky="nsw")
        self.FrameZwei.configure(fg_color="transparent")


customtkinter.set_appearance_mode("dark")
if __name__ == "__main__":
    app = App()
    app.mainloop()