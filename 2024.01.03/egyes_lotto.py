import random

print("Egyes lottó")

tipp = 0
huzott_szam = 1
hetek_szama = 1

while tipp != huzott_szam:
    huzott_szam = random.randint(1,10)

    tipp = int(input(f"{hetek_szama}. heti tipp="))
    print(f"{hetek_szama}. heti húzás={huzott_szam}")
    hetek_szama += 1
    
    if tipp == huzott_szam:
        print(f"A(z) {hetek_szama}. héten nyert!")
        break
    else:
        print(f"A(z) {hetek_szama}. héten nem nyert!") 
          