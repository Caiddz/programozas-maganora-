class tanc:
    def __init__(self, fajta, lany, fiu):
        self.fajta = fajta
        self.lany = lany
        self.fiu = fiu

tancok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.17/./tancrend.txt", "r") as bemenet:
    mezok = [""] * 3
    for i, sor in enumerate(bemenet):
        if i % 3 == 0:
            mezok[0] = sor.strip()
        elif i % 3== 1:
            mezok[1] = sor.strip()
        elif i % 3 == 2:
            mezok[2] = sor.strip()
            tancok.append(tanc(mezok[0], mezok[1], mezok[2]))

#2.feladat--------
            
print(f"Elsőként bemutatott tánc: {tancok[0].fajta}")
print(f"Utolsóként bemutatott tánc: {tancok[-1].fajta}")

#3.feladat-----------

sambaparok = 0

for i in range(len(tancok)):
    if tancok[i].fajta == "samba":
        sambaparok += 1

print(f"Samba táncot {sambaparok} pár mutatta be.")


#4.feladat-------------

vilma_tancai = []

for i in range(len(tancok)):
    if tancok[i].lany == "Vilma":
        vilma_tancai.append(tancok[i].fajta)
for i in range(len(vilma_tancai)):
    print(vilma_tancai[i])

#5.feladat------------
bekert_tanc = input("Tánc neve=")

Vilmavolt = False
párja = ""

for i in range(len(tancok)):
    if bekert_tanc == tancok[i].fajta and tancok[i].lany == "Vilma":
        Vilmavolt = True
        párja = tancok[i].fiu

if Vilmavolt is True:
    print(f"A {bekert_tanc} bemutatóján Vilma párja {párja} volt.")
else:
    print(f"Vilma nem táncolt {bekert_tanc}-t.")

#7feladat------------

lanyok = {}
fiuk = {}

for i in range(len(tancok)):
    if lanyok.get(tancok[i].lany) is None:
        lanyok[tancok[i].lany] = 1
    else:
        lanyok[tancok[i].lany] += 1

for i in range(len(tancok)):
    if fiuk.get(tancok[i].fiu) is None:
        fiuk[tancok[i].fiu] = 1
    else:
        fiuk[tancok[i].fiu] += 1