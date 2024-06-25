from datetime import datetime

class adat:
    def __init__(self,belepes,szemelyazon,beki):
        self.belepes = belepes
        self.szemelyazon = szemelyazon
        self.beki = beki

adatok = []


with open("/Users/sany/Documents/programozas(maganora)/2024.01.12/./ajto-1.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(' ')
        adatok.append(adat(datetime(1, 1, 1, int(mezok[0]), int(mezok[1])), mezok[2], mezok[3]))

print("2. feladat")
print(f"Az elsoő belépő: {adatok[0].szemelyazon}")

for i in range(len(adatok)-1, -1, -1):
    if adatok[i].beki == "ki":
        print(f"Az utolsó kilépő: {adatok[i].szemelyazon}")
        break
print()
print("5. feladat")

hanyan = 0
max_hanyan = 0
oraperc = datetime(1, 1, 1, 0, 0, 0)
for i in range(len(adatok)):
    if adatok[i].beki == "be":
        hanyan += 1
    else:
        hanyan -= 1    
    if hanyan > max_hanyan:
        max_hanyan = hanyan
        oraperc = adatok[i].belepes
print(f"Például {oraperc.hour}:{oraperc.minute}-kor voltak a legtöbben a társalgóban. ")

