class lakas:
    def __init__(self, adoszam, utca, hazszam, sav, terulet):
        self.adoszam = adoszam
        self.utca = utca
        self.hazszam = hazszam
        self.sav = sav
        self.terulet = terulet

lakasok = []

adosavA = 0
adosavB = 0
adosavC = 0

with open("/Users/sany/Documents/programozas(maganora)/2024.03.09/./utca.txt", "r") as bemenet:
    for i, sor in enumerate(bemenet):
        mezok = sor.strip().split(" ")
        if i == 0:
            adosavA = int(mezok[0])
            adosavB = int(mezok[1])
            adosavC = int(mezok[2])
        else:
            mezok = sor.strip().split(" ")
            lakasok.append(lakas(mezok[0], mezok[1], mezok[2], mezok[3], int(mezok[4])))

#2.feladat-----------------------------------
        

print(f"2. feladat. A mintában {len(lakasok)} telek szerepel.")

#3.feladat--------------------

tulaj = input("3. feladat. Egy tulajdonos adószáma: ")
tulajvan = False

for i in range(len(lakasok)):
    if tulaj == lakasok[i].adoszam:
        print(f"{lakasok[i].utca} utca {lakasok[i].hazszam}")
        tulajvan = True

if not tulajvan:
    print("Nem szerepel az adatállományban.")

#4.feladat-----------------------------------


def ado(adosav, alapterulet):
    if adosav == "A":
        return adosavA * alapterulet
    elif adosav == "B":
        return adosavB * alapterulet
    else:
        return adosavC * alapterulet


#5.feladat------
A_sav = 0
B_sav = 0
C_sav = 0

A_osszeg = 0
B_osszeg = 0
C_osszeg = 0

for i in range(len(lakasok)):
    if lakasok[i].sav == "A":
        A_sav += 1
        A_osszeg += ado("A" , lakasok[i].terulet)
    elif lakasok[i].sav == "B":
        B_sav += 1
        B_osszeg += ado("B" , lakasok[i].terulet)
    else:
        C_sav += 1
        C_osszeg += ado("C" , lakasok[i].terulet)


print(f"A sávba {A_sav} telek esik, az adó {A_osszeg} Ft.")
print(f"B sávba {B_sav} telek esik, az adó {B_osszeg} Ft.")
print(f"C sávba {C_sav} telek esik, az adó {C_osszeg} Ft.")

#6.feladat--------------
print("6. feladat. A több sávba sorolt utcák:")
tobb_sav = []

for i in range(len(lakasok) - 1):
        if lakasok[i].utca == lakasok[i + 1].utca and lakasok[i].sav != lakasok[i + 1].sav and lakasok[i].utca not in tobb_sav:
            tobb_sav.append(lakasok[i].utca)
for i in range(len(tobb_sav)):
    print(tobb_sav[i])

#7.feladat-------------

for i in range(len(lakasok)):
    print(lakasok[i].adoszam)



