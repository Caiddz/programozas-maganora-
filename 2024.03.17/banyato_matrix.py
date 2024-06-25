sorok_szama = 0
oszlopok_szama = 0
banyato = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.17/./melyseg-banya.txt", "r") as bemenet:
    for i, sor in enumerate(bemenet):
        if i == 0:
            sorok_szama = int(sor.strip())
        elif i == 1:
            oszlopok_szama = int(sor.strip())
        else:
            mezok = sor.strip().split(" ")
            mezok_szamkent = []
            for j in range(len(mezok)):
                mezok_szamkent.append(mezok_szamkent)

#2.feladat----------------
                
print("2. feladat")

bekert_sor = int(input("A mérés sorának azonosítója="))
bekert_oszlop = int(input("A mérés oszlopának azonosítója="))

print(f"A mért mélység az adott helyen {banyato[bekert_sor - 1][bekert_oszlop - 1]} dm")