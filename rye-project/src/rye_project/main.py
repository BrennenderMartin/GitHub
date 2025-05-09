import pandas as pd

m = 0.2
D = 0.1
x = 0.15

v_alt = 0
v = 0
a = 0
t = 0

delta_t = 0.2
n = 1000

def loop(n: int) -> list:
    global m, D, x, v_alt, v, a, t, delta_t
    data = []
    for i in range(n):
        v_alt = v
        t = t + delta_t
        a = -(D / m) * x
        v = v + a * delta_t
        x = x + (v + v_alt) / 2 * delta_t
        data.append([round(t, 1), round(a, 3), round(v, 3), round(x, 3)])
    return data

df = pd.DataFrame(loop(n), columns=["t", "a", "v", "h"])

df.to_csv("results_anim.csv", index=True)

print(df)