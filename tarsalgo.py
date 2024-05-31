from datetime import datetime

class tarsalgo:
    def __init__(self, ido, azon, beki):
        self.ido = ido
        self.azon = azon
        self.beki = beki

tarsalgok = []

with open("/Users/sany/Documents/programozas(maganora)/készules part2/ajto.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(" ")
        tarsalgok.append(tarsalgo(datetime(1, 1, 1, int(mezok[0]), int(mezok[1])), int(mezok[2]), mezok[3]))

#feladatok------

#2.feladat------

print("2. feladat")
utsokilepo = 0


for i in range(len(tarsalgok)):
    if tarsalgok[i].beki == "ki":
        utsokilepo = tarsalgok[i].azon
        

print(f"Az első belépő: {tarsalgok[0].azon}")
print(f"Az utolsó kilépő: {utsokilepo}")

#3.feladat------
athaladasok = {}

for i in range(len(tarsalgok)):
    if tarsalgok[i].azon not in athaladasok.keys():
        athaladasok.update({tarsalgok[i].azon:0})
for i in range(len(tarsalgok)):
    athaladasok[tarsalgok[i].azon] += 1

rendezett_athaladasok = sorted(athaladasok.keys())

with open("/Users/sany/Documents/programozas(maganora)/készules part2/athaladas.txt", "w") as kimenet:
    for key in rendezett_athaladasok:
        kimenet.write(f"{key} {athaladasok[key]}\n")


#4.feladat-----
        
print("4. feladat")

bentlevok = {}

for i in range(len(tarsalgok)):
    if tarsalgok[i].azon not in bentlevok.keys():
        bentlevok.update({tarsalgok[i].azon:False})
for i in range(len(tarsalgok)):
    if tarsalgok[i].beki == "be":
        bentlevok[tarsalgok[i].azon] = True
    else:
        bentlevok[tarsalgok[i].azon] = False

print(f"A végén a társalgóban voltak: ", end="")
for key, value in bentlevok.items():
    if value:
        print(key ,end=" ")





#5.fealadat----
print("5. feladat")

hanyan = 0
max_hanyan = 0
oraperc = (datetime(1,1,1,0,0,0))
for i in range(len(tarsalgok)):
    if tarsalgok[i].beki == "be":
        hanyan += 1
    else:
        hanyan -= 1
    if hanyan > max_hanyan:
        max_hanyan = hanyan
        oraperc = tarsalgok[i].ido
print(f"Például {oraperc.hour}:{oraperc.minute}-kor voltak a legtöbben a társalgóban. ")

#6.feladat---

print("6. feladat")

bekert_szemely = int(input("Adja meg a személy azonosítóját!" ))

#7.feladat-----------
print("7. feladat")

bent = datetime(1,1,1,0,0,0)

for i in range(len(tarsalgok)):
    if bekert_szemely == tarsalgok[i].azon:
        bent = tarsalgok[i].ido
    print(f"{bent.hour}:{bent.minute}")


