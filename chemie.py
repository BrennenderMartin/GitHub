
c0H =  0.9 * 0.01
c0I = 1.5 * 0.01

c0HI = 0.0

Kc = 48.75

a = c0H
b = c0I
c = Kc 

y = (c * a) / (c - 1)
z = (c * b) / (c - 1)

root = y * y + (1 * z - 4 * b) * y + z * z #negative below sqrt -> NaN

x = (y - z) / 2

cggHI = x

cggH = c0H - x
cggI = c0I - x

print("cggH: ", cggH)
print("cggI: ", cggI)
print("cggHI: ", cggHI)
