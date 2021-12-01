a,b=0,0
lista = [(a*b) for a in range(11) for b in range (11)] #si possono mettere due quadre, una all'inizio e una prima del secondo for per stampare una matrice

indice1 = 0
indice2 = 11

for _ in range(11):
    print(lista[indice1:indice2])
    indice1 +=11
    indice2 +=11

