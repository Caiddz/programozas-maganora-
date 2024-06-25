from datetime import datetime

class bejegyzes:
    def __init__(self, datum, vezeteknev, keresztnev, hiany):
        self.datum = datum
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.hiany = hiany

bejegyzesek = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.17/./naplo-2.txt", "r" ) as bemenet:
    datum = datetime(1,1,1)
    for sor in bemenet:
        if sor[0] == "#":
            mezok = sor.strip().split(" ")
            datum = datetime(1, int(mezok[1]), int(mezok[2]))
        else:
            mezok = sor.strip().split(" ")
            bejegyzesek.append(bejegyzes(datum, mezok[0], mezok[1], mezok[2]))

#2.feladat-----------
print("2. feladat")

ossz = 0

for i in range(len(bejegyzesek)):
    if sor[0] != "#":
        ossz += 1

print(f"A naplóban {ossz} bejegyzés van.")

#3.feladat----------------------
print("3. feladat")
igazolthiany = 0
igazolatlan = 0

for i in range(len(bejegyzesek)):
    for j in range(len(bejegyzesek[i].hiany)):
        if bejegyzesek[i].hiany[j] == "X":
            igazolthiany += 1
        elif bejegyzesek[i].hiany[j] == "I":
            igazolatlan += 1

print(f"Az igazolt hiányzások száma {igazolthiany}, az igazolatlanoké {igazolatlan} óra.")

#4.feladat---------------

def hetnapja(honap, nap): 
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok",
              "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1]+nap) % 7
    return napnev[napsorszam]

#5.feladat--------
    
bekerthonap = int(input("A hónap sorszáma="))
bekertnap = int(input("A nap sorszáma="))

#6.feladat--------

bekert_tannap = input("A nap neve=")
bekert_tanoraszam = input("Az óra sorszáma=")

for i in range(len(bejegyzesek)):
    if bekert_tannap == bejegyzesek[i].datum.day:
        if bekert_tanoraszam == bejegyzesek[i]:
            break
#7feladat------
        
hianyzasok = {}
    
for i in range(len(bejegyzesek)):
    if hianyzasok.get(bejegyzesek[i].vezeteknev + " " + bejegyzesek[i].keresztnev) is None:
        aznapihianyzasok = 0
        for j in range(len(bejegyzesek[i].hiany)):
            if bejegyzesek[i].hiany[j] == "X":
                aznapihianyzasok += 1
            elif bejegyzesek[i].hiany[j] == "I":
                aznapihianyzasok += 1
        hianyzasok[bejegyzesek[i].vezeteknev + " " + bejegyzesek[i].keresztnev] = aznapihianyzasok
    else:
        aznapihianyzasok = 0
        for j in range(len(bejegyzesek[i].hiany)):
            if bejegyzesek[i].hiany[j] == "X":
                aznapihianyzasok += 1
            elif bejegyzesek[i].hiany[j] == "I":
                aznapihianyzasok += 1
        hianyzasok[bejegyzesek[i].vezeteknev + " " + bejegyzesek[i].keresztnev] += aznapihianyzasok

maxertek = max(hianyzasok, key= lambda x:hianyzasok[x])
print(maxertek)

rendezett_hianyzasok = sorted(hianyzasok.items(), key = lambda x:x[1], reverse= True)
print(rendezett_hianyzasok)    
