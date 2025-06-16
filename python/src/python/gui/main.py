import customtkinter as ctk
import os
from PIL import Image # type: ignore
import subprocess  # Add to top of your file
from playsound import playsound  # type: ignore # pip install playsound (version 1.2.2 preferred)
import tkinter.filedialog as fd

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.radiobutton_variable = ctk.StringVar()
        self.label_list = []
        self.button_list = []
        #self.playing = False
    
    def play_sound(self, item, filetype, filepath):
        filepath = os.path.join(filepath, f"{item}.{filetype}")
        try:
            os.startfile(filepath)
        except Exception as e:
            print(f"Error: {e}")
    
    def edit_sound(self, item, filetype, filepath):
        print(f"Editing sound for item: {item}.{filetype} from path: {filepath}")

    def add_item(self, item, type, path, image=None):
        row_index = len(self.label_list)
        
        label = ctk.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        label2 = ctk.CTkLabel(self, text=f".{type}", compound="left", padx=5, anchor="e")
        button_play = ctk.CTkButton(self, text="Play", width=100, height=24, command=lambda i=item, j=type, k=path: self.play_sound(i, j, k))
        button_edit = ctk.CTkButton(self, text="Edit", width=100, height=24, command=lambda i=item, j=type, k=path: self.edit_sound(i, j, k))
        
        label.grid(row=row_index, column=0, pady=(0, 10), sticky="w")
        label2.grid(row=row_index, column=1, pady=(0, 10), sticky="e")
        button_play.grid(row=row_index, column=2, pady=(0, 10), padx=5)
        button_edit.grid(row=row_index, column=3, pady=(0, 10), padx=5)
        
        self.label_list.append((label, label2))
        self.button_list.append((button_play, button_edit))

    def remove_item(self):
        for (label, label2) in self.label_list:
            label.destroy()
            label2.destroy()
        for (button_play, button_edit) in self.button_list:
            button_play.destroy()
            button_edit.destroy()
        
        self.label_list.clear()
        self.button_list.clear()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.sounds_path = None
        
        self.title("Sound Playback GUI")
        self.geometry("800x600")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # create sidebar frame with widgets fg_color main
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Soundboard", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button = ctk.CTkButton(self.sidebar_frame, text="Select Folder", command=self.select_folder)
        self.sidebar_button.grid(row=1, column=0, padx=20, pady=10)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
        # create scrollable label and button frame
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=1, rowspan=4, padx=0, pady=(55, 0), sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        
    def create_items(self):
        self.scrollable_label_button_frame.remove_item()
        for i, item in enumerate(os.listdir(self.sounds_path)):
                if os.path.isfile(os.path.join(self.sounds_path, item)) and item.endswith(".mp4") or item.endswith(".mp3"):
                    self.scrollable_label_button_frame.add_item(
                        item=item.split(".")[0],
                        type=item.split(".")[-1],
                        path=self.sounds_path,
                        image=ctk.CTkImage(Image.open(os.path.join(CURRENT_DIR, "test_images", "chat_light.png")))
                    )
                else:
                    print(f"Skipping file: {item}")
        
    def select_folder(self):
        folder_path = fd.askdirectory(title="Select a Folder")
        if folder_path:
            print(f"Selected folder: {folder_path}")
            self.sounds_path = folder_path
            self.create_items()
            return folder_path
        else:
            print("No folder selected.")
            return None

if __name__ == "__main__":
    app = App()
    app.mainloop()
