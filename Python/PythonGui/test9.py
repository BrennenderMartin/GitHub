import csv
import pandas as pd
""" 
with open("Cleanlab2.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    data = [row for row in csv_reader]  

#print(data)

file = pd.read_csv("Cleanlab.csv")
#print(file)

chunksize = 10 ** 6
chunk = {}
for chunk in pd.read_csv("Cleanlab.csv", chunksize=chunksize):
    for index, row in chunk.iterrows():
        print(row)



daten = {
    "Index": [4804,1195,5605,5698],
    "GaugeID": [13013201, 12389201, 13421611, 13421611],
    "DefectMapID": [579178, 245753, 50967, 63618],
    "DefectID": [1761, 1085, 51, 6],
    "LabelErrorScore": [7.733031088719144e-05, 0.0006918385624885559, 0.0007425202056765556, 0.0008408152498304844],
    "Image": ["Image_test.jpg", "Image_test2.jpg", "Image_test3.jpg", "Image_test4.jpg"]
}

#df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
#                  index=['cobra', 'viper', 'sidewinder'],
#                  columns=['max_speed', 'shield'])

df = pd.DataFrame(daten)
df.to_csv("Test8.csv", sep=";", index=False)

"""
 
daten = pd.read_csv("Test8.csv", sep=";")
df = pd.DataFrame(daten)
df.at[1, "DefectID"] = 9999
#print(df)
df.to_csv("Test8.csv", sep=";")
