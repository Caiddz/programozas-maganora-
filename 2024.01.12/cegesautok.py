from datetime import datetime

class auto:
    def __init__(self, nap, ido, rendszam, szemazon, km, kibe):
        self.nap = nap
        self.ido = ido
        self.rendszam = rendszam
        self.szemazon = szemazon
        self.km = km
        self.kibe = kibe

autok = []

with open ("/Users/sany/Documents/programozas(maganora)/2024.01.12/./autok.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(" ")
        ido = datetime.strptime(mezok[1], "%H:%M")
        if mezok[5] == "0":
            autok.append(auto(int(mezok[0]), ido, mezok[2], mezok[3], mezok[4], "ki"))
        else:
            autok.append(auto(int(mezok[0]), ido, mezok[2], mezok[3], mezok[4], "be"))


print("2. feladat")

utsonap = 0 
utolsorendsz = 0

for i in range(len(autok)):
    if autok[i].kibe == "ki":
        utsonap = autok[i].nap
        utolsorendsz = autok[i].rendszam

print(f"{utsonap}. nap rendszám: {utolsorendsz}")

print("")
print("3.feladat")

adottnap = int(input("Nap: "))
print(f"Forgalom a(z) {adottnap} napon:")
for i in range(len(autok)):
    if autok[i].nap == adottnap:
        print(f"{autok[i].ido.hour}:{autok[i].ido.minute} {autok[i].rendszam} {autok[i].szemazon} {autok[i].kibe}")

print("")
print("4.feladat")

nemhoztakvissza = 0

for i in range(len(autok)):
    
    
