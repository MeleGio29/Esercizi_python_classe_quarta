lista = [0, 2, 1, 4, 5, 1]
listaNuova = []
x = len(lista)

for k in range (0, x) :
    for j in range (0, x):
        if (k != j) and (lista[k] == lista[j]):
            listaNuova = lista[0:j] + lista[j+1:]

print(lista)
print(listaNuova)

#elemento in lista
#elemento not in lista
#entrambe restituiscono un booleano