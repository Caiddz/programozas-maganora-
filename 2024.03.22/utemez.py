from datetime import datetime

class tabor:
    def __init__(self, kezdett, vege, tanulok, tema):
        self.kezdett = kezdett
        self.vege = vege
        self.tanulok = tanulok
        self.tema = tema

taborok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.22/./taborok.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split("\t")
        taborok.append(tabor(datetime(1, int(mezok[0]), int(mezok[1])), datetime(1, int(mezok[2]), int(mezok[3])), mezok[4], mezok[5]))

#2.feladat------------

print("2. feladat")

összadat = 0
for i in range(len(taborok)):
    összadat += 1

print(f"Az adatsorok száma: {összadat}")
print(f"Az először rögzített tábor témája: {taborok[0].tema}")
print(f"Az utoljára rögzített tábor témája: {taborok[-1].tema}")

#3.feladat----------------
print("3. feladat")

for i in range(len(taborok)):
    if taborok[i].tema == "zenei":
        print(f"Zenei tábor kezdődik {taborok[i].kezdett.month}. hó {taborok[i].kezdett.day}. napján.")

#4.feladat--------
        
print("4. feladat")

legtobb = 0
legtobbindex = 0

for i in range(len(taborok)):
    if legtobb < len(taborok[i].tanulok):
        legtobb = len(taborok[i].tanulok)
        legtobbindex = i

print("Legnépszerűbbek: ")
print(taborok[legtobbindex].kezdett.month, taborok[legtobbindex].kezdett.day, taborok[legtobbindex].tema)

# 5. feladat---------------------------------------------------------------------
#fuggveny letrehozas ,nap szamolas

def sorszam(honap, nap):
    if honap == 6:
        return nap - 16 + 1
    elif honap == 7:
        return nap + 16
    else:
        return nap + 46
    

#6.feladat
print("6. feladat")

ho = int(input("hó: "))
nap = int(input("nap: "))
bekertdatum = datetime(1, ho, nap)
tabormegy = 0

for i in range(len(taborok)):
    if taborok[i].kezdett <= bekertdatum and taborok[i].vege >= bekertdatum:
        tabormegy += 1

print(f"Ekkor éppen {tabormegy} tábor tart.")

#7feladat-----

print("7. feladat")

bekerttanulo = input("Adja meg egy tanuló betűjelét: ")

rendezett_taborok = sorted(taborok, key=lambda x : x.kezdett)
mehet_e = True

elozotaboravege = datetime(1, 1, 1)

with open("/Users/sany/Documents/programozas(maganora)/2024.03.22/./egytanulo.txt", "w")as kimenet:
    for i in range(len(rendezett_taborok)):
        for j in range(len(rendezett_taborok[i].tanulok)):
            if bekerttanulo == len(rendezett_taborok[i].tanulok[j]):
                kimenet.write(f"{rendezett_taborok[i].kezdett.month}.{rendezett_taborok[i].kezdett.day}-{rendezett_taborok[i].vege.month}.{rendezett_taborok[i].vege.day}. {rendezett_taborok[i].tabortema}\n")
                if i > 0 and rendezett_taborok[i].kezdett < elozotaboravege:
                    mehet_e = False
                elozotaboravege = rendezett_taborok[i].vege

if mehet_e:
    print("ELmehet mindegyik tábroba")
else:
    print("Nem mehet el mindegyik táborba.")

