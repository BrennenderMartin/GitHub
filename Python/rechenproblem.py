""" 
    Dies ist ein Programm welches unter 
    dem Namen TikTokTrend2 als Java-Datei zu finden ist.
    Hier habe ich es mit Python erstellt.
"""
zahl = 0
max_op = 0
min_op = 420
max_co = 0
min_co = 0

for i in range(2,1000):
    counter = 0
    zahl = i

    while zahl != 1:
        counter += 1
        if zahl % 2 == 0:
            zahl /= 2
        else:
            zahl *= 3
            zahl += 1
    if counter > max_op:
        max_op = i
        max_co = counter
        
    if counter < min_op:
        min_op = i
        min_co = counter

print(f" Größte Zahl: {max_op} Anzahl Operationen: {max_co}")
print(f" Kleinste Zahl: {min_op} Anzahl Operationen: {min_co}")




zahl = int(input("Gib eine Zahl ein: "))
counter = 0

while zahl != 1:
    if zahl % 2 == 0:
        zahl = zahl / 2
    else:
        zahl = zahl * 3 + 1
    counter += 1
    print(f"Die Zahl beträgt gerade: {zahl}")

print(f"Die gegebene Zahl benötigt {counter} Durchgänge")
