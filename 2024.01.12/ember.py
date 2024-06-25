class ember:
    def __init__(self, nev, kor, nem):
        self.nev = nev
        self.kor = kor
        self.nem = nem

ember_1 = ember("Tamás", "26", "fiú")
ember_2 = ember("zsolti", "100", "lány")
ember_3 = ember("kati", "33", "lány") 

print(ember_1.nev)
print(ember_3.kor)