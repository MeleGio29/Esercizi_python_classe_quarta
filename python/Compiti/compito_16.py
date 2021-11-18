lista = [0, 1, 2, 3, 5, 6, 7, 8]
max = lista[1]
min = lista[1]

for numeri in lista:
    if(max < lista[numeri]):
        max = numeri
    if(min > lista[numeri]):
        min = numeri
    

print(f"Il numero più grande è: {max} mentre il minore è: {min}")