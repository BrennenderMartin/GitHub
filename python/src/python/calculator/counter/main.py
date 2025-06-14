import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title("Card counter")
        
        self.count = 0
        
        self.up_button = ctk.CTkButton(
            self,
            border_spacing=10,
            text="Up",
            command=self.count_up
        )
        self.up_button.grid(row=0, column=0, sticky="ew")
        
        self.down_button = ctk.CTkButton(
            self,
            border_spacing=10,
            text="Down",
            command=self.count_down
        )
        self.down_button.grid(row=2, column=0, sticky="ew")
        
        self.textbox = ctk.CTkTextbox(self, height=20, corner_radius=0)
        self.textbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self.textbox.insert("end", f"{self.count}")
    
    def count_up(self):
        self.count += 1
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", f"{self.count}")
    
    def count_down(self):
        self.count -= 1
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", f"{self.count}")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
