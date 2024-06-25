from datetime import datetime

class jelentes:
    def __init__(self, telepules, ido, szelirany, homerseklet):
        self.telepules = telepules
        self.ido = ido
        self.szelirany = szelirany
        self.homerseklet = homerseklet

jelentesek = []

with open("/Users/sany/Documents/programozas(maganora)/2020érettségi/tavirathu13.txt", "r") as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(" ")
        jelentesek.append(jelentes(mezok[0], datetime(1,1,1, int(mezok[1][0:2]), int(mezok[1][2:4])), mezok[2], int(mezok[3])))

#2.feladat--------------
        
print("2. feladat")

bekert_varos = input("Adja meg egy település kódját! Település: ")

utso_meres = datetime(1,1,1,0,0)

for i in range(len(jelentesek)-1, -1, -1):
    if bekert_varos == jelentesek[i].telepules:
        print(f"Az utolsó mérési adat a megadott településről {jelentesek[i].ido.hour} : {jelentesek[i].ido.minute} -kor érkezett.")
        break
    
#3.feladat----------
print("3. feladat")

min_meres = jelentesek[0]
max_meres = jelentesek[0]

for i in range(len(jelentesek)):
    if jelentesek[i].homerseklet < min_meres.homerseklet:
        jelentesek[i] = min_meres
    elif jelentesek[i].homerseklet > max_meres.homerseklet:
        jelentesek[i] = max_meres


print(f"A legalacsonyabb hőmérséklet: {min_meres.telepules} {min_meres.ido.hour} : {min_meres.ido.minute} {min_meres.homerseklet} fok")

#4.feladat-------
print("4. feladat")
szelcsend = False

for i in range(len(jelentesek)):
    if jelentesek[i].szelirany == "00000":
        print(f"{jelentesek[i].telepules} {jelentesek[i].ido.hour} : {jelentesek[i].ido.minute}")
        szelcsend = True

if not szelcsend:
    print("Nem volt szélcsend a mérések idején.")
