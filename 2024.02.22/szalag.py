class szalag:
    def __init__(self,ido, indulas, erkezes, tomeg):
        self.ido = ido
        self. indulas = indulas
        self.erkezes = erkezes
        self.tomeg = tomeg 

szalagok = []
szalaghossz = 0
egysegnyiido = 0

with open ("/Users/sany/Documents/programozas(maganora)/2024.02.22/./szallit.txt", "r") as bemenet:
    elsosor = bemenet.readline().strip().split(" ")
    szalaghossz = int(elsosor[0])
    egysegnyiido = int(elsosor[1])

    for sor in bemenet:
        mezok = sor.strip().split(" ")
        szalagok.append(szalag(int(mezok[0]), int(mezok[1]), int(mezok[2]), int(mezok[3])))

#2.feladat------------------------------(input,honnan-hova)
        
print("2. feladat")

kiv_adat = int(input("Adja meg, melyik adatsorra kíváncsi! "))

print(f"Honnan: {szalagok[kiv_adat -1 ].indulas} Hova: {szalagok[kiv_adat -1].erkezes}")

#3.feladat------------------------------(

def tav(szalaghossz, indulashelye, erkezeshelye):
    if szalag
