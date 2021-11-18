n1 = int (input("Inserisci un numero: "))
n2 = int (input("Inserisci un numero: "))
lista = []
somma = n1*n1 + n2*n2
lista.append(somma)

somquadrato = (n1 + n2) * (n1 + n2)
lista.append(somquadrato)

differenza = n1*n1 - n2*n2
lista.append(differenza)

diffquadrato = (n1-n2) * (n1-n2)
lista.append(diffquadrato)

print(lista)