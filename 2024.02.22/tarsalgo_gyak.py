# 1.feladat(beolvasas)------------------------------------------------------------------------------

from datetime import datetime

class tarsalgo:
    def __init__(self, ido, azon, kibe):
        self.ido = ido
        self.azon = azon
        self.kibe = kibe

tarsalgok = []

with open ("/Users/sany/Documents/programozas(maganora)/2024.02.22/./ajto-1.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(" ")
        tarsalgok.append(tarsalgo(datetime(1,1,1, int(mezok[0]), int(mezok[1])), int(mezok[2]), mezok[3]))

#print(tarsalgok)
#2.feladat(elsobelep, utolso belep)-------------------------------------------------------------

print(f"Az első belépő: {tarsalgok[0].azon}")

utolsoki = 0
for i in range(len(tarsalgok)):
    if tarsalgok[i].kibe == "ki":
        utolsoki = tarsalgok[i].azon
        
print(f"Az utolsó kilépő: {utolsoki}")

#3.feladat(hanyszor ment at ajton -novekvo- )
