import customtkinter

app = customtkinter.CTk()

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(app, values=["option 1", "option 2"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)


app.mainloop()