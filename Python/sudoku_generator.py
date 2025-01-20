import csv
from dokusan import generators
import numpy as np
import pandas as pd

#numpy
arr = np.array(list(str(generators.random_sudoku(avg_rank=50))))
numpy_matrix = arr.reshape(9, 9)

#print(numpy_matrix)

# Matrix speichern
#numpy_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
with open('matrix.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(numpy_matrix)



#pandas
daten = {
    "Index": [4804,1195,5605,5698],
    "GaugeID": [13013201, 12389201, 13421611, 13421611],
    "DefectMapID": [579178, 245753, 50967, 63618],
    "DefectID": [1761, 1085, 51, 6],
    "LabelErrorScore": [7.733031088719144e-05, 0.0006918385624885559, 0.0007425202056765556, 0.0008408152498304844],
    "Image": ["Image_test.jpg", "Image_test2.jpg", "Image_test3.jpg", "Image_test4.jpg"]
}

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                index=['cobra', 'viper', 'sidewinder'],
                columns=['max_speed', 'shield']
                )

#df = pd.DataFrame(daten)
#df.to_csv("Test8.csv", sep=";", index=False)

#print(df)
