import random

szekrenyek_szama = 10 
foglalt_szekrenyek = 0
idő = 420
prev = 0

while foglalt_szekrenyek < szekrenyek_szama:
    varakozas_perc = random.randint(1,10)
    szolgáltatás = random.choice([1,2])
    prev += varakozas_perc
    if szolgáltatás == 1:
        foglalt_szekrenyek += 1
        prev += szolgáltatás 
    elif szolgáltatás == 2 and foglalt_szekrenyek != 0:
        foglalt_szekrenyek -= 1 
        prev += szolgáltatás
    
    print(f"Foglalt szekrények száma: {foglalt_szekrenyek} Munkaidő idáig: {prev} ")
    print(f"Milyen szolgáltatást kíván igénybe venni (csomagfeladás: 1 , csomagátvétel 2)? {szolgáltatás} ")

munkavegeido_ora = round((idő + prev) / 60)
munkavageido_perc = (idő + prev) % 60

print(f"A munkaidő vége: {munkavegeido_ora}:{munkavageido_perc}")    
       

    