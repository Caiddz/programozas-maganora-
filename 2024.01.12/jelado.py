from datetime import datetime
import math

class jel:
    def __init__(self,ido,x,y):
        self.ido = ido
        self.x = x
        self.y = y
jelek = []

with open("/Users/sany/Documents/programozas(maganora)/2024.01.12/./jel.txt", "r" ) as bemenet:
    for sor in bemenet:
        mezok = sor.strip().split(" ")
        jelek.append(jel(datetime(1, 1, 1,int(mezok[0]),int(mezok[1]),int(mezok[2])),int(mezok[3]),int(mezok[4])))
print()
print("2.feladat")
jelsorszam = int(input("Adja meg a jel sorszámát! "))
print(f"x={jelek[jelsorszam -1 ].x} y={jelek[jelsorszam -1].y}")

def eltelt(ido1,ido2):
    return (ido2-ido1).total_seconds()
print()
print("4.feladat")
print(f"Időtartam: {jelek[-1].ido - jelek[0].ido}")
print()
print("5.feladat")

bal_also_x = 999999
bal_also_y = 999999
jobb_felso_x = 0
jobb_felso_y = 0
for i in range(len(jelek)):
    if jelek[i].x < bal_also_x:
        bal_also_x = jelek[i].x 
    if jelek[i].y < bal_also_y:
        bal_also_y = jelek[i].y 
    if jelek[i].x > jobb_felso_x:
        jobb_felso_x = jelek[i].x
    if jelek[i].y > jobb_felso_y:
        jobb_felso_y = jelek[i].y

print(f"Bal alsó: {bal_also_x} {bal_also_y}, jobb felső: {jobb_felso_x} {jobb_felso_y}")
print()
print("6.feladat")
osszeg = 0
for i in range(len(jelek)-1):
    tavolsag = math.sqrt(pow(jelek[i].x - jelek[i + 1].x,2) + pow(jelek[i].y - jelek[i + 1].y,2))
    osszeg += tavolsag
print(f"Elmozdulás: {osszeg:.3f}")



    



