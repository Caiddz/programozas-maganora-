baracskara = 0
pettendre = 0 
kocsik_szama = 0
szerelveny = 0
irany = ("b","p","")
while irany != "":
    input("Baracskára vagy Pettendre ment a vonat (b/p)? " )
    if input == "b":
        baracskara += 1
    elif input == "p":
        pettendre += 1
    kocsik_szama = input("Hány kocsiból állt a szerelvény? ")
    

print(f"Baracskára {baracskara} vonat ment, összesen {szerelvenyek_szama} és {szerelvények_átlaga}")            
    