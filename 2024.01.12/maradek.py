import random
osztando = 0
oszto = 0
jo = 0
for i in range(5):
    osztando = random.randint(15,21)
    oszto = random.randint(3,8)
    tipp = int(input(f"Mennyi a(z) {osztando}:{oszto} maradéka?"))
    maradek = osztando % oszto
    if tipp ==  maradek:
        print("Így van ügyes vagy.")
        jo += 1
    else:
        print(f"Nincs igazad, a helyes eredmény: {maradek}")
        jo -= 1
print(f"{jo} esetben állatpítottad meg jól a maradékot.")    

