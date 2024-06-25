class felosztas:
    def __init__(self, nev, tantargy, osztaly, oraszam):
        self.nev = nev
        self.tantargy = tantargy
        self.osztaly = osztaly
        self.oraszam = oraszam

felosztasok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.09/./beosztas.txt", "r") as bemenet:
    mezok = [""] * 4
    for i, sor in enumerate(bemenet):
        if i % 4 == 0:
            mezok[0] = sor.strip()
        elif i % 4 == 1:
            mezok[1] = sor.strip()
        elif i % 4 == 2:
            mezok[2] = sor.strip()
        elif i % 4 == 3:
            mezok[3] = sor.strip()
            felosztasok.append(felosztas(mezok[0], mezok[1], mezok[2], int(mezok[3])))    

#2.feladat-------
            
print("2. feladat")

osszadat = 0

for i in range(len(felosztasok)):
    osszadat += 1

print(f"A fájlban {osszadat} bejegyzés van.")

#3.feladat-------
print("3. feladat")

orak = 0

for i in range(len(felosztasok)):
    orak += felosztasok[i].oraszam 
print(orak)

#4feladat-------

print("4. feladat")

bekerttan_ora = 0

bekerttan = input("Egy tanár neve= ")
for i in range(len(felosztasok)):
    if bekerttan == felosztasok[i].nev:
        bekerttan_ora += felosztasok[i].oraszam

print(f"A tanár heti óraszáma: {bekerttan_ora}")

#5.feladat

with open("/Users/sany/Documents/programozas(maganora)/2024.03.09/./of.txt", "w") as kimenet:
    for i in range(len(felosztasok)):
        if felosztasok[i].tantargy == "osztalyfonoki":
            kimenet.write(f"{felosztasok[i].osztaly} - {felosztasok[i].nev}\n")

#6.feladat-------
print("6. feladat")

kertosztaly = input("Osztály= ")
kerttantargy = input("Tantárgy=" )

bontott_tantargyak = []
tantargyak = 0
for i in range(len(felosztasok)):
   if felosztasok[i].osztaly == kertosztaly and felosztasok[i].tantargy == kerttantargy:
        bontott_tantargyak.append(felosztasok[i].tantargy)
for i in range(len(bontott_tantargyak)):
    tantargyak += 1

if tantargyak != 1:
    print("Csoportbontásban tanulják.")
else:
    print("Nem Csoportbontásban tanulják.")

#7.feladat-----
print("7. feladat")
ossztanar = 0
ossztanarnev = []


for i in range(len(felosztasok)):
    if felosztasok[i].nev not in ossztanarnev:
        ossztanarnev.append(felosztasok[i].nev)
for i in range(len(ossztanarnev)):
    ossztanar += 1

print(f"Az iskolában {ossztanar} tanár tanít.")

