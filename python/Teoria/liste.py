#le liste sono mutabili
lista = [3, 3.1415, "ciao"] #prende il nome di lista eterogenea perché è composta da tipi diversi
print(lista)
numeri_primi = [2, 3, 5, 7, 11, 13]

lista[1] = 2.645 #può essere modificata
print(lista)

numeri_primi.append(17)
print(numeri_primi)

#il doppio underscore __ viene chiamato "dunder"

print(f"La lunghezza è {len(numeri_primi)}") #il comando len ci calcola la lunghezza della stringa

altri_numeri_primi = [19, 23, 29]
molti_numeri_primi = numeri_primi + altri_numeri_primi #l'operatore + concatena più liste
print(molti_numeri_primi)

print(5 * altri_numeri_primi) #stampa 5 volte la lista

for numero_primo in numeri_primi: #non c'è nessun indice, cicla per gli elementi
    print(numero_primo)
print("FINE")
