print("Budapest kerületeinek lakossága")
print("1 Budapest kerületeinek népessége:")
kisebb50 = 0
nagyobb100k = 0
lakossag = [25172, 89452, 130560, 100071, 26013, 38541, 52362, 76916, 59720, 78030, 148517, 57566, 121657, 124218, 
79675, 74499, 87673, 102216, 59648, 65611, 76092, 55112, 22965]
for i in range(1,24):
    keruletek = print(f"{i}. kerület lakossága: {lakossag[i - 1]} fő")
    if lakossag[i-1] < 50000:
            kisebb50 += 1
    if lakossag[i - 1] > 100000:
                i  

print(f"2. 50000 főnél kevesebb lakosú {kisebb50} kerület.")            