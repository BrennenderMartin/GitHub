import customtkinter
import pandas as pd

#customtkinter setup
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Variablen:
g = 9.81
t = 0
dt = 0.1
v = 0
h = 10

i = 0
n = 15

#g, t, d_t, v, h, n

counter = []
verl = []
height = []

#Programm:

class App(customtkinter.CTk):
    def __init__(self, g, t, dt, v, h, n, i):
        super().__init__()

        #while h >= 0:
        #    i += 1
        for i in range(n):
            t += dt
            y = v 
            v += g * dt
            h -= 0.5 * (y + v) * dt

            verl.append(v)
            height.append(h)
            counter.append(dt * i)
        print(counter)
        print(verl)
        print(height)
        df = pd.DataFrame()
        df["Zeit"] = counter
        df["Geschwindigkeit"] = verl
        df["Höhe"] = height
        print(df)

        self.textbox = customtkinter.CTkTextbox(self, width=300, height=300)
        self.textbox.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.textbox.insert("0.0", df)

app = App(g, t, dt, v, h, n, i)
app.mainloop()
