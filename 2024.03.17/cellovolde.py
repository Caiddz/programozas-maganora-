lovesek = []
lovesek_szama = []

with open("/Users/sany/Documents/programozas(maganora)/2024.03.17/./verseny-1.txt", "r") as bemenet:
    for i, sor in enumerate(bemenet):
        if i == 0:
            lovesek_szama = int(sor.strip())
        else:
            lovesek.append(sor.strip())
#2feleadat-------
            
print("2. feladat")

egymasutan_talalok = ""
print("Az egymast kovetoen tobbszor talalo versenyzok: ", end="")
for i in range(len(lovesek)):
    for j in range(len(lovesek[i]) - 1):
        if lovesek[i][j] == "+" and lovesek[i][j + 1] == "+":
            print(i + 1, end=" ") 
            break