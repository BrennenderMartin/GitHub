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
