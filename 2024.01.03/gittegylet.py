import random

Emberek = ["Barabás", "Kolnay", "Csele", "Leszik", "Richter", "Nemecsek"]
napok = []

print("A gittrágás októberi beosztása:")
prev = ""
van = False

for i in range(1,31):
    emberekrandom = random.choice(Emberek)
    print(f" {i}. napon {emberekrandom}" )
    if prev == emberekrandom:
        van = True
    prev = emberekrandom
    
if van == True:
    print("Van")
else:
    print("Nincs")    
