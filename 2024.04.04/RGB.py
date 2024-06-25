class kod:
    def __init__(self, piros, zold, kek):
        self.piros = piros
        self.zold = zold
        self.kek = kek

kodok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.04.04/./kep.txt", "r") as bemenet:
    for sor in bemenet: 
        mezok = sor.strip().split(" ")
        kodok.append(kod(int(mezok[0]), int(mezok[1]), int(mezok[1])))

#2.feladat----
        
print("2. feladat")

print("Kérem egy képpont adatait!")
bekert_sor = int(input("Sor:"))
bekert_oszlop = int(input("Oszlop:"))

