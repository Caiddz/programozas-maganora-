import random

iranyok = []
for i in range(6):
    iranyok.append(random.randint(0, 360))

egtaj = input("Melyik égtájra vagy kíváncsi (É/K/D/NY)? ")
print("A feljegyzett szélirányok: ", end="")
for i in range(len(iranyok) - 1):
    print(f"{iranyok[i]}, ", end="")
print(iranyok[-1])

fujt_szel = False

if egtaj == "É":
    for irany in iranyok:
        if irany >= 315 and irany <= 359 or irany >= 0 and irany <= 45:
            fujt_szel = True
elif egtaj == "K":
    for irany in iranyok:
        if irany >= 45 and irany <= 134:
            fujt_szel = True
elif egtaj == "D":
    for irany in iranyok:
        if irany >= 135 and irany <= 224:
            fujt_szel = True
elif egtaj == "NY":
    for irany in iranyok:
        if irany >= 225 and irany <= 315:
            fujt_szel = True

if fujt_szel:
    print("Fújt szél az irányból.")
else:
    print("Nem fújt szél az irányból.")    
