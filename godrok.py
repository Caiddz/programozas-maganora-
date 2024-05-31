godrok = []

with open("/Users/sany/Documents/programozas(maganora)/Érettségire_készülés/./melyseg.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip()
        godrok.append(int(mezok[0]))

#--------------------------------------------
ossz = 0

for i in range(len(godrok)):
    ossz += 1

print("1. feladat")
print(f"A fájl adatainak száma: {ossz}")

#2.feladadt---------------
tavertek = int(input("Adjon meg egy távolságértéket! "))

print(f"Ezen a helyen a felszín {godrok[tavertek]} méter mélyen van.")

#3.feladat-----------
erintetlen = 0
erintett = 0

for i in range(len(godrok)):
    if godrok[i] == 0:
        erintetlen += 1
    else:
        erintett += 1

arany = (erintetlen / erintett) * 100
kerek_arany = round(arany, 2)
print(f"Az érintetlen terület aránya {kerek_arany} %")

#4.feadladt----------------
godor_t = []
godor = []

for i in range(len(godrok)):
    if godrok[i] != 0:
        godor.append(godrok[i])
    if godrok[i] == 0:
        godor_t.append(godor)
        godor = []


null_mentes = []
with open("/Users/sany/Documents/programozas(maganora)/Érettségire_készülés/godrok.txt", "w") as kimenet:
    for i in godor_t:
        if i != []:

            #5Feladathoz
            null_mentes.append(i)

            for a in i:
                kimenet.write(f'{a} ')
            kimenet.write('\n')


#5.feladat-----
hanygodor = 0

db = len(null_mentes)

print(db)

#6.feladat-------

print("6. feladat")
print("a)")

for i in range(len(godrok)):
    if godrok[tavertek] == i:
        





#print(f"A gödör kezdete: {}")
  
    
        


