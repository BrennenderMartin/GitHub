import pandas as pd

# Listen für Namen, Studiengänge und Noten
names = ["aparna", "pankaj", "sudhir", "Geeku"]
degrees = ["MBA", "BCA", "M.Tech", "MBA"]
scores = [90, 40, 80, 98]

# DataFrame erstellen
df = pd.DataFrame({'name': names, 'degree': degrees, 'score': scores})

# DataFrame in CSV-Datei speichern
#print(df)
df.to_csv('GFG.csv')
