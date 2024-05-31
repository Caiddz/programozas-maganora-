def ellenorzes(taj_szam) :
    ellenorzo_szam = int(taj_szam[-1])
    print(f"Az ellenőrzőszámjegy: {ellenorzo_szam}")

    osszeg = 0
    for i in range(8):
        szamjegy = int(taj_szam[i])
        pozicio = i + 1
        if pozicio % 2 == 1:  
            osszeg += szamjegy * 3
        else:
            osszeg += szamjegy * 7
    print(f"A szorzatok összege: {osszeg}")

    maradek = osszeg % 10
    if maradek == ellenorzo_szam:
        print("Helyes a szám!")
    else:
        print("Hibás a szám!")

taj_szam = input("Kérem a TAJ-számot: ")
ellenorzes(taj_szam)