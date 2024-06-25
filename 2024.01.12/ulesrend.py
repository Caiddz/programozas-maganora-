tanulok = "Huba", "Soma", "Aliz", "Lili", "Rita", "Márk", "Imre", "Nóra", "Egon", "Irma", "Hugó", "Ödön", "Ella", "Anna", "Ottó", "Emil", "Jenő", "Zita", "Irén", "Emma", "Áron", "Réka", "Máté", "Liza"
print("A 9.b ülésrendje:")
print()

for i in range(0,len(tanulok), 4):
    print(f"{tanulok[i]}-{tanulok[i + 1]}\t{tanulok[i + 2]}-{tanulok[i + 3]}") 
    

