from datetime import datetime
class utas:
    def __init__(self, megallo, felszallas, azon, tipus, ervenyesseg, jegydb):
        self. megallo = megallo
        self.felszallas = felszallas
        self.azon = azon
        self.tipus = tipus
        self.ervenyesseg = ervenyesseg
        self.jegydb = jegydb

utasok = []

with open("/Users/sany/Documents/programozas(maganora)/2024.01.12/./utasadat.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(" ")
        if int(mezok[4]) > 100:
            utasok.append(utas(int(mezok[0]), datetime(int(mezok[1][0:4]), int(mezok[1][4:6]), int(mezok[1][6:8]), int(mezok[1][9:11]), int(mezok[1][11:13])), mezok[2], mezok[3], datetime(int(mezok[4][0:4], int(mezok[4][4:6]), int(mezok[4][6:8]), 23, 59, 59)), 0))
        else:
            utasok.append(utas(int(mezok[0]), datetime(int(mezok[1][0:4]), int(mezok[1][4:6]), int(mezok[1][6:8]), int(mezok[1][9:11]), int(mezok[1][11:13])), mezok[2], mezok[3], datetime(1, 1, 1, 0, 0, 0), int(mezok[4])))
