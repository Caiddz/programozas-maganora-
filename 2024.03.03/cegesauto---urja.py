from datetime import datetime

class auto:
    def __init__(self, nap, ora, rendszam, dolgozo, km, kibe)
        self.nap = nap
        self.ora = ora
        self.rendszam = rendszam
        self.dolgozo = dolgozo
        self.km = km
        self.kibe = kibe

autok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.03/./autok.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split("\t")
        ido = datetime.strptime(mezok[1], "%H:%M")
        if mezok[5] == "0":
            autok.append(auto(int(mezok[0]), ido, mezok[2], int(mezok[3]), int(mezok[4]), "ki"))
        else:
            autok.append(auto(int(mezok[0]), ido, mezok[2], int(mezok[3]), int(mezok[4]), "be"))


print("2. feladat")

