import pandas as pd

daten = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Alter": [30, 25, 22],
    "Stadt": ["Berlin", "München", "Köln"],
}

df = pd.DataFrame(daten)
print(df)

print(" ")

df["Name"] = df["Name"].replace(["Alice", "Charlie"], "THOMAS")
print(df)
#df.to_csv("personen.csv", index=False)

#Variablen:

g = 9.81
# 0.9 < c < 1.1
c = 1
# 0.2 < A < 0.8
A = 0.5
p = 1.3
k = 0.5 * c * A * p

#Masse des Springer, hier: 75kg
m = 75

t = 0
v = 0
h = 2000
n = 3

counter = []
verl = []
height = []

for i in range(n):
    #2. v_neu berechnen
    y = v
    v = v + (g + (k / m) * v * v) * i
    verl.append(v)
    #3. h_neu berechnen
    h = h - 0.5 * (y + v) * i
    height.append(h)
    counter.append(i)
print(counter)
print(verl)
print(height)
df = pd.DataFrame()

df["Zeit"] = counter
df["Geschwindigkeit"] = verl
df["Höhe"] = height

print(df)