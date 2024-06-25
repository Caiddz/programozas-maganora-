class reklam:
    def __init__(self, nap, tipus, db):
        self.nap = nap
        self.tipus = tipus
        self.db = db

reklamok = []

with open ("/Users/sany/Documents/programozas(maganora)/2024.03.22/./rendel.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(" ")
        reklamok.append(reklam(int(mezok[0]), mezok[1], int(mezok[2])))

#2.feladat------------
print("2. feladat:")

osszrendeles = 0
for i in range(len(reklamok)):
    osszrendeles += 1

print(f"A rendelések száma: {osszrendeles}")

#3.feladat-----------
print("3. feladat:")

bekertnap = int(input("Kérem, adjon meg egy napot: "))
bekertnap_rendelesei = 0

for i in range(len(reklamok)):
    if reklamok[i].nap == bekertnap:
        bekertnap_rendelesei += 1

print(f"A rendelések száma az adott napon: {bekertnap_rendelesei}")

#4.feladat--------
print("4. feladat:")
voltrendeles = True
Nemvolt_rendeles_nap = 0

for i in range(len(reklamok)):
    if reklamok[i].tipus == "NR" and reklamok[i].db == 0:
        Nemvolt_rendeles_nap = reklamok[i].nap
    elif reklamok[i].tipus == "NR" and reklamok[i].db != 0:
        voltrendeles = False

if voltrendeles is True:
    print(f"{Nemvolt_rendeles_nap} nap nem volt a reklámban nem érintett városból rendelés")
else:
    print("Minden nap volt rendelés a reklámban nem érintett városból")

#5.feladat-------
print("5. feladat")
legnagyobb = 0
legnagyobbnap = 0

for i in range(len(reklamok)):
    if legnagyobb < reklamok[i].db:
        legnagyobb = reklamok[i].db
        legnagyobbnap = reklamok[i].nap

print(f"A legnagyobb darabszám: {legnagyobb}, a rendelés napja: {legnagyobbnap}")

#6.feladat--------

def osszes(varos, nap):
    szamlalo = 0
    for i in range(len(reklamok)):
        if reklamok[i].nap == nap and reklamok[i].tipus == varos:
             szamlalo += reklamok[i].db
    return szamlalo

#7.feladat-----------

print("7. feladat:")

PL_osszes=osszes("PL", 21)
TV_osszes=osszes("TV", 21)
NR_osszes=osszes("NR", 21)

print(f"A rendelt termékek darabszáma a 21. napon PL: {PL_osszes} TV: {TV_osszes} NR: {NR_osszes}")

#8.feladat--------
print("8. feladat:")
pl_elso10 = 0
tv_elso10 = 0
nr_elso10 = 0

for i in range(len(reklamok)):
    if reklamok[i].nap < 10 and reklamok[i].tipus == "PL":
        pl_elso10 += reklamok[i].db
    elif reklamok[i].nap < 10 and reklamok[i].tipus == "TV":
        tv_elso10 += reklamok[i].db
    elif reklamok[i].nap < 10 and reklamok[i].tipus == "NR":    
        nr_elso10 += reklamok[i].db

pl_kozep = 0
tv_kozep = 0
nr_kozep = 0

for i in range(len(reklamok)):
    if reklamok[i].nap > 10 and reklamok[i].nap < 20:
        pl_kozep += reklamok[i].db
        tv_kozep += reklamok[i].db
        nr_kozep += reklamok[i].db

pl_utso = 0
tv_utso = 0
nr_utso = 0

for i in range(len(reklamok)):
    if reklamok[i].nap > 20:
        pl_utso += reklamok[i].db
        tv_utso += reklamok[i].db
        nr_utso += reklamok[i].db

    tablazat = [
    ["Napok","1...10","11...20","21...30"],
    ["PL",f"{pl_elso10}",f"{pl_kozep}",f"{pl_utso}"],
    ["TV",f"{tv_elso10}",f"{tv_kozep}",f"{tv_utso}"],
    ["NR",f"{nr_utso}",f"{nr_kozep}",f"{nr_utso}"]
]

with open("/Users/sany/Documents/programozas(maganora)/2024.03.22/./kampany.txt", "w") as kimenet:
    for i in tablazat:
        kimenet.write(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]} \n")

#---------------------
varosok = ["PL", "TV", "NR"]
PL_adatok = [0,0,0]
Tv_adatok = [0,0,0]
NR_adatok = [0,0,0]


for i in range(len(varosok)):
    for j in range(len(reklamok)):
        if reklamok[j].tipus == varosok[i]:
            if i == 0:
                if reklamok[j].nap < 11:
                    PL_adatok[0] += 1
                elif reklamok[j].nap > 10 and reklamok[j].nap < 21:
                    PL_adatok[1] += reklamok[j].db
                else:
                    PL_adatok[2] += reklamok[j].db
            elif i == 1:
                if reklamok[j].nap < 11:
                    Tv_adatok[0] += reklamok[j].db
                elif reklamok[j].nap > 10 and reklamok[j].nap < 21:
                    Tv_adatok[1] += reklamok[j].db
                else:
                    Tv_adatok[2] += reklamok[j].db
            else:
                if reklamok[j].nap < 11:
                    NR_adatok[0] += reklamok[j].db
                elif reklamok[j].nap > 10 and reklamok[j].nap < 21:
                    NR_adatok[1] += reklamok[j].db
                else:
                    NR_adatok[2] += reklamok[j].db
                    
with open("/Users/sany/Documents/programozas(maganora)/2024.03.22/./kampany2.txt", "w") as kimenet:
    kimenet.write(f"Napok\t1...10\t11..20\t21..30\n")
    kimenet.write(f"PL\t{PL_adatok[0]}\t")