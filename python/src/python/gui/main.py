import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sound Playback GUI")
        self.geometry("800x600")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_frame = ctk.CTkFrame(self, height=100)
        self.title_frame.grid(row=0, column=0, sticky="new")
        
        self.button = ctk.CTkButton(
            self.title_frame,
            width=60,
            height=60,
            fg_color="transparent",
            image="./src/rye_project/gui/image/folder.png",
            command=self.on_button_click
        )
        self.button.grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )
        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

    def on_button_click(self):
        print("Button Clicked!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
