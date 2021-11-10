import math
n1 = int (input("Inserisci la prima coordinata del primo punto: "))
n2 = int (input("Inserisci la seconda coordinata dek primo punto: "))

c1 = int (input("Inserisci la prima coordinata del secondo punto: "))
c2 = int (input("Inserisci la seconda coordinata dek secondo punto: "))

tupla = (n1, n2, c1, c2)
distanza = (((n1 - n2) **2) + ((c1 - c2) **2))**(1/2)

print(distanza)