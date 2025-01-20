from typing import Tuple
import tkinter
import tkinter.messagebox
import customtkinter
from CTkListbox import *
#from PIL import Image, ImageTk

label = "Bruch"
value = "Bruch"
choice = "Label"
new_label = label

def relabel():
       print("Relabel")
       
def optionmenu_callback(choice): # Funktion zum Relabel mit optionmenu
        print("optionmenu dropdown clicked:", choice)
        if choice == "Bruch":
                print(choice)
        if choice == "Riss":
                print(choice)
        if choice == "Totalschaden":
                print(choice)

def show_value(selected_option): # Funktion Database einzelne Objekte
        print(selected_option)

def read_database(): # Funktion read Database
        print("Works")

class FrameDatabase(customtkinter.CTkFrame): #Frame der Datenbank
        def __init__(self, master, show_value):
                super().__init__(master)

                listbox = CTkListbox(self, command=show_value)
                listbox.pack(fill="both", expand=True, padx=10, pady=10)

                for i in range(8):
                        listbox.insert(i, f"Option {i}")

class FrameEins(customtkinter.CTkFrame): #Frame von Datenbank und Button darunter
        def __init__(self, master, read_database, show_value):
                super().__init__(master)

                self.checkbox_frame = FrameDatabase(self, show_value)
                self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

                self.button = customtkinter.CTkButton(self, text="my button", command=read_database)
                self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

class FrameZwei(customtkinter.CTkFrame): #Frame von Bild, Label vom Bild und FrameDrei
        def __init__(self, master):
                super().__init__(master)

                #self.image = customtkinter.CTkImage(Image.open("Image_test.jpg"), size=(300, 150))

                #self.image_label = customtkinter.CTkLabel(self, text="", image=self.image)
                #self.image_label.grid(row=0, column=0, pady=(10,0), sticky="nw")

                self.appearance_mode_label = customtkinter.CTkLabel(self, text="Relabel:", anchor="w")
                self.appearance_mode_label.grid(row=1, column=0, padx=10, pady=(10,0), sticky="w")

                self.text_var = tkinter.IntVar(value=choice)
                self.item_label = customtkinter.CTkLabel(self, textvariable=self.text_var, anchor="w")
                self.item_label.grid(row=1, column=0, padx=200, pady=(10,0), sticky="n")
                self.item_label.update()

                self.Frame = FrameDrei(self)
                self.Frame.grid(row=2, column=0, sticky="w")
                self.Frame.configure(fg_color="transparent")

class FrameDrei(customtkinter.CTkFrame): #Frame von OptionMenu fürs relabel
        def __init__(self, master):
                super().__init__(master)

                #self.appearance_mode_label = customtkinter.CTkLabel(self, text="Relabel:", anchor="w")
                #self.appearance_mode_label.grid(row=3, column=0, padx=10, pady=(10,0), sticky="w")
                self.optionmenu_var = customtkinter.StringVar(value="label")
                self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Bruch", "Riss", "Totalschaden", "Test", "Test2", "Test3", "Test4"],
                                                        command=optionmenu_callback,
                                                        variable=self.optionmenu_var)
                self.optionmenu.grid(row=4, column=0, pady=(10,10), sticky="n")

                #self.text_var = tkinter.IntVar(value=choice)
                #self.item_label = customtkinter.CTkLabel(self, textvariable=self.text_var, anchor="w")
                #self.item_label.grid(row=3, column=1, padx=50, pady=(10,0), sticky="n")

                self.button = customtkinter.CTkButton(self, text="Relabel", command=relabel)
                self.button.grid(row=4, column=1, padx=10, pady=(10,0), sticky="n")

class App(customtkinter.CTk):
        def __init__(self):
                super().__init__()

                self.title("Mein Skript")
                self.geometry("550x300")
                self.grid_columnconfigure(1, weight=1)
                self.grid_rowconfigure(1, weight=1)

                self.checkbox_frame = FrameEins(self, read_database, show_value)
                self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
                self.checkbox_frame.configure(fg_color="transparent")

                self.checkbox_frame = FrameZwei(self)
                self.checkbox_frame.grid(row=0, column=1, padx=10, pady=(10, 0))
                self.checkbox_frame.configure(fg_color="transparent")

customtkinter.set_appearance_mode("dark")


app = App()
app.mainloop()