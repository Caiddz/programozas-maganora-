import random
kartyak = ["Pi2", "Pi3", "Pi4", "Pi5", "Pi6", "Pi7", "Pi8", "Pi9", "Pi10", "PiJ", "PiQ", "PiK", "PiÁ", "Ká2", "Ká3", "Ká4", "Ká5", "Ká6", "Ká7", "Ká8", "Ká9", "Ká10", "KáJ", "KáQ", "KáK", "KáÁ", "Tr2", "Tr3", "Tr4", "Tr5", "Tr6", "Tr7", "Tr8", "Tr9", "Tr10", "TrJ", "TrQ", "TrK", "TrÁ", "Kő2", "Kő3", "Kő4", "Kő5", "Kő6", "Kő7", "Kő8", "Kő9", "Kő10", "KőJ", "KőQ", "KőK", "KőÁ"]
print("Kártyakeverés")
print()
print("Eredeti sorrend:", end="")
for i in range(len(kartyak)):
    print(kartyak[i], end=" ")

for i in range(1000):
    valasztott_sorszam1 = random.randint(0, len(kartyak) - 1) 
    valasztott_sorszam2 = random.randint(0, len(kartyak) - 1)
    temp = kartyak[valasztott_sorszam1]
    kartyak[valasztott_sorszam1] = kartyak[valasztott_sorszam2]
    kartyak[valasztott_sorszam2] = temp
print()
print("Megkevert pakli:", end="")
for i in range(len(kartyak)):
    print(kartyak[i], end=" ")



