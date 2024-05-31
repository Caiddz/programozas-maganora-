from datetime import datetime

class meres:
    def __init__(self, telepules, ido, szelirany, homerseklet):
        self.telepules = telepules
        self.ido = ido
        self.szelirany = szelirany
        self.homerseklet = homerseklet

meresek = []

with open("/Users/sany/Documents/programozas(maganora)/Érettségire_készülés/./tavirathu13.txt", "r") as bement:
    for sor in bement:
        mezok = sor.strip().split(" ")
        meresek.append(meres(mezok[0], datetime(1,1,1, int(mezok[1][0:2]),int(mezok[1][2:4])), mezok[2], int(mezok[3])))

#2. feladat----------
        
print("2. feladat")
bekert_tel = input("Adja meg egy település kódját! Település: ")
bekert_tel_utso = ""
for i in range(len(meresek)):
    if bekert_tel == meresek[i].telepules:
        bekert_tel_utso = meresek[i].ido

print(f"Az utolsó mérési adat a megadott településről {bekert_tel_utso.hour}:{bekert_tel_utso.minute}-kor érkezett.")

#3.feladat------

print("3. feladat")
#legalacsonyabb = meresek[0]

#for i in range(len(meresek)):
#    if meresek[i].homerseklet < legalacsonyabb:
#        legalacsonyabb = meresek[i]

#print(f"A legalacsonyabb hőmérséklet: {legalacsonyabb.telepules}   fok")

max_meres = meresek[0]
min_meres = meresek[0]
for i in range(len(meresek)):
    if meresek[i].homerseklet > max_meres.homerseklet:
        max_meres = meresek[i]
    if meresek[i].homerseklet < min_meres.homerseklet:
        min_meres = meresek[i]
print(f"A legalacsonyabb hőmérséklet: {min_meres.telepules} {min_meres.ido.hour}:{min_meres.ido.minute} {min_meres.homerseklet} fok.")
print(f"A legmagasabb hőmérséklet: {max_meres.telepules} {max_meres.ido.hour}:{max_meres.ido.minute} {max_meres.homerseklet} fok.")

#4.feladat------------

print("4. feladat")
szelcsend = False
for i in range(len(meresek)):
    if meresek[i].szelirany == "00000":
        print(f"{meresek[i].telepules} {meresek[i].ido.hour} : {meresek[i].ido.minute}")
        szelcsend = True
    if not szelcsend:
        print("Nem volt szélcsend a mérések idején.")

#5.feladat----------
        
for i in range(len(meresek)):



                       

