from datetime import datetime

class vonat:
    def __init__(self, vonat, allomas, ido, ive):
        self.vonat = vonat
        self.allomas = allomas
        self.ido = ido
        self.ive = ive
        
vonatok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.03/./vonat.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split("\t")
        vonatok.append(vonat(int(mezok[0]), int(mezok[1]), datetime(1,1,1, int(mezok[2]), int(mezok[3])), mezok[4]))
#2.feladat------------------------------------------------------------
print("2.feladat")

allomasokszama = 0

for i in range(len(vonatok)):
    if allomasokszama < vonatok[i].allomas:
        allomasokszama = vonatok[i].allomas 
        

print(f"Az állomások száma: {allomasokszama + 1}")

vonatokszama = 0

for i in range(len(vonatok)):
    if vonatokszama < vonatok[i].vonat:
        vonatokszama = vonatok[i].vonat

print(f"A vonatok száma: {vonatokszama}")

#3.feladat-------------------------------------------------------------------------------------

print("3.feladat")






#4.feladat-----------------------------------------------------------------------------------------------

print("4.feladat")

adott_vonat = input("Adja meg egy vonat azonosítóját! ")
adott_idopont = input("Adjon meg egy időpontot (óra perc)! ")

#5.feladat---------------------------------------------------------------------------------

print("5.feladat")

adott_vonat_adatai = []
percek = 0


for i in range(len(vonatok)):
    if adott_vonat == vonatok[i].vonat:
        adott_vonat_adatai.append(vonatok[i])
        
print(f"A(z) {adott_vonat} vonat útja {percek} perccel hosszabb volt az előírtnál.")

#6.feladat--------------------------------------------------------------------------------------


