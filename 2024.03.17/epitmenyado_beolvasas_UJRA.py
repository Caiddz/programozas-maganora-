class ado:
    def __init__(self, adoszam, utca, hazszam, adosav, terulet):
        self.adoszam = adoszam
        self.utca = utca
        self.hazszam = hazszam
        self.adosav = adosav
        self.terulet = terulet

A_adosav = 0
B_adosav = 0
C_adosav = 0

adok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.17/./utca.txt", "r") as bemenet:
    for i, sor in enumerate(bemenet):
        if i == 0:
            mezok = sor.strip().split(" ")
            A_adosav = int(mezok[0])
            B_adosav = int(mezok[1])
            C_adosav = int(mezok[2])
        else:
            mezok = sor.strip().split(" ")
            adok.append(ado(mezok[0], mezok[1], mezok[2], mezok[3], int(mezok[4])))

print("2. feladat")