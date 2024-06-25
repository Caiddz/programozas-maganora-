from datetime import datetime

taborok = []

class tabor:
    def __init__(self,kezdett,vege,diakbetujel,tabortema):
        self.kezdett = kezdett
        self.vege = vege
        self.diakbetujel = diakbetujel
        self.tabortema = tabortema

with open("/Users/sany/Documents/programozas(maganora)/2024.02.22/./taborok.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split('\t')
        taborok.append(tabor(datetime(1, int(mezok[0]), int(mezok[1])), datetime(1, int(mezok[2]), int(mezok[3])), mezok[4], mezok[5]))

#2.feladat--------------------------------------------------------------------

print("2.feladat")
print(f"Az adatsorok száma: {len(taborok)}")
print(f"Az először rögzített tábor témája: {taborok[0].tabortema}")
print(f"Az utoljára rögzített tábor témája: {taborok[-1].tabortema}")

# 3.feladat---------------------------------------------------------------------

print("3.feladat")
for i in range(len(taborok)):
    if taborok[i].tabortema == "zenei":
        print(f"Zenei tábor kezdődik {taborok[i].kezdett.month}. hó {taborok[i].kezdett.day}. napján.")

#4.feladat---------------------------------------------------------------------

print("4.feladat")
jelszamindex = 0
jelszama = 0

for i in range(len(taborok)):
    if jelszama < len(taborok[i].diakbetujel):
        jelszama = len(taborok[i].diakbetujel)
        jelszamindex = i

print("Legnépszerűbbek: ")
print(taborok[jelszamindex].kezdett.month, taborok[jelszamindex].kezdett.day, taborok[jelszamindex].tabortema)

# 5. feladat---------------------------------------------------------------------
#fuggveny letrehozas ,nap szamolas

def sorszam(honap, nap):
    if honap == 6:
        return nap - 16 + 1
    elif honap == 7:
        return nap + 16
    else:
        return nap + 46

#6. feladat-------------------------------------------------------
# megadottnap ?? 
honap = int(input("hó: "))
nap = int(input("nap: "))

bekertdatum = datetime(1, honap, nap)
hany_tabor = 0

for i in range(len(taborok)):
    #if taborok[i].kezdett.month <= honap and taborok[i].kezdett.day <= nap and taborok[i].vege.month >= honap and taborok[i].vege.day >= nap:
        #hany_tabor += 1
    if taborok[i].kezdett <= bekertdatum and taborok[i].vege >= bekertdatum:
        hany_tabor += 1 
    

print(f"Ekkor éppen {hany_tabor} tábor tart.")

#7.feladat--------------------------------------------------------
#tanulo,taborok amik erdeklik+datum

egytanulo = input("Adja meg egy tanuló betűjelét: ")

rendezett_taborok = sorted(taborok, key = lambda x : x.kezdett)

mehet_e = True

elozotaboravege = datetime(1,1,1)

with open("/Users/sany/Documents/programozas(maganora)/2024.02.22/./egytanulo.txt", "w") as kimenet:
    for i in range(len(rendezett_taborok)):
        for j in range(len(rendezett_taborok[i].diakbetujel)):
            if egytanulo == rendezett_taborok[i].diakbetujel[j]:
                kimenet.write(f"{rendezett_taborok[i].kezdett.month}.{rendezett_taborok[i].kezdett.day}-{rendezett_taborok[i].vege.month}.{rendezett_taborok[i].vege.day}. {rendezett_taborok[i].tabortema}\n")
                if i > 0 and rendezett_taborok[i].kezdett < elozotaboravege:
                    mehet_e = False
                elozotaboravege = rendezett_taborok[i].vege

if mehet_e:
    print("ELmehet mindegyik tábroba")
else:
    print("Nem mehet el mindegyik táborba.")
