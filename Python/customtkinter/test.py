import customtkinter as ctk

def App():
    def __init__(self):
        super().__init__()
        
        self.title("test for a Sudoku")
        
        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
