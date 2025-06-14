import customtkinter
import pandas as pd

#customtkinter setup
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Variablen:
delta_t = 0.2
t = 0
v = 0
m = 0.2
D = 0.1
x = 0.15
a = 0

n = 15

#delta_t, t, v, m, D, x, a, n

counter = []
verl = []
height = []

#Programm:

class App(customtkinter.CTk):
    def __init__(self, delta_t, t, v, m, D, x, a, n):
        super().__init__()

        for i in range(n):
            t = t + delta_t
            a = -(D / m) * x
            y = v
            v = v + a * delta_t
            x = x + 0.5 + (y + v) * delta_t

            verl.append(v)
            height.append(a)
            counter.append(delta_t * i)
        print(counter)
        print(verl)
        print(height)
        df = pd.DataFrame()
        df["Zeit"] = counter
        df["Geschwindigkeit"] = verl
        df["Höhe"] = height
        print(df)

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.textbox.insert("0.0", df)

app = App(delta_t, t, v, m, D, x, a, n)
app.mainloop()
