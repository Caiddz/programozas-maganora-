class beosztas:
    def __init__(self, tanar, tantargy, osztaly, oraszam):
        self.tanar = tanar
        self.tantargy = tantargy
        self.osztaly = osztaly
        self.oraszam = oraszam

beosztasok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.17/./beosztas.txt", "r") as bemenet:
    mezok = [""] * 4
    for i, sor in enumerate(bemenet):
        if i % 4 == 0:
            mezok[0] = sor.strip()
        elif i % 4 == 1:
            mezok[1] = sor.strip()
        elif i % 4 == 2:
            mezok[2] = sor.strip()
        elif i % 4 == 3:
            mezok[3] = sor.strip()
            beosztasok.append(beosztas(mezok[0], mezok[1], mezok[2], int(mezok[3])))
