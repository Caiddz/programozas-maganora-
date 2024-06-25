import random
print("A sebességváltó állásai: " ,end="")
uthossz = 5,5 * 60
sebessegek = []
for i in range (33):
    sebesseg = random.randint(1,12)
    print(f"{sebesseg}, ",end="")
    sebessegek.append(sebesseg)

ora = 0    

for i in range(len(sebessegek)):
    if sebessegek[i] == 12:
        perc = i * 10
        ora = perc // 60 + 1
        break
print()
print(f"A(z) {ora}. órában sikerült eőször a legmagasabb fokozatba váltani.")    