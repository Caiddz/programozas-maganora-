from datetime import datetime

class meres:
    def __init__(self, telepules, ido, szeladatok, homerseklet):
        self.telepules = telepules
        self.ido = ido
        self.szeladatok = szeladatok
        self.homerseklet = homerseklet

meresek = []

with open("/Users/sany/Documents/programozas(maganora)/2024.01.12/./tavirathu13.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(' ')
        meresek.append(meres(mezok[0], datetime(1, 1, 1, int(mezok[1][0:2]), int(mezok[1][2:4])), mezok[2], int(mezok[3])))
        
print("2. feladat")
bekert_varos = input("Adja meg egy település kódját! Település: ")
utolso_meres = meresek[0]
for i in range(len(meresek)):
    if meresek[i].telepules == bekert_varos:
        utolso_meres = meresek[i]     
print(f"Az utolsó mérési adat a megadott településről {utolso_meres.ido.hour}:{utolso_meres.ido.minute}-kor érkezett.")

print("3. feladat")
max_meres = meresek[0]
min_meres = meresek[0]
for i in range(len(meresek)):
    if meresek[i].homerseklet > max_meres.homerseklet:
        max_meres = meresek[i]
    if meresek[i].homerseklet < min_meres.homerseklet:
        min_meres = meresek[i]
print(f"A legalacsonyabb hőmérséklet: {min_meres.telepules} {min_meres.ido.hour}:{min_meres.ido.minute} {min_meres.homerseklet} fok.")
print(f"A legmagasabb hőmérséklet: {max_meres.telepules} {max_meres.ido.hour}:{max_meres.ido.minute} {max_meres.homerseklet} fok.")

print("4. feladat")
volt_szelcsend = False
for i in range(len(meresek)):
    if meresek[i].szeladatok == "00000":
        print(f"{meresek[i].telepules} {meresek[i].ido.hour}:{meresek[i].ido.minute}")
        volt_szelcsend = True
if not volt_szelcsend:
    print("Nem volt szélcsend a mérések idején.")
