import customtkinter
import pandas as pd

#customtkinter setup
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Variablen:
g = 9.81
m = 80
cw = 1.1
p = 1.3
A = 0.65
dt = 1
t = 0
v = 0
h = 2000
k = 0.5 * cw * A * p

n = 20

#g, m, cw, A, dt, t, v, h

counter = []
verl = []
height = []

#Programm:

class App(customtkinter.CTk):
    def __init__(self, g, m, k, dt, t, v, h, n):
        super().__init__()

        #while h > 0:
        #    i += 1
        for i in range(n):
            t += dt
            y = v
            v = v + (g + (k / m) * v * v) * dt
            h -= 0.5 * (y + v) * dt
            verl.append(v)
            height.append(h)
            counter.append(i)
        print(counter)
        print(verl)
        print(height)
        df = pd.DataFrame()
        #df["Zeit"] = counter
        df["Geschwindigkeit"] = verl
        df["Höhe"] = height
        print(df)

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.textbox.insert("0.0", df)

app = App(g, m, k, dt, t, v, h, n)
app.mainloop()