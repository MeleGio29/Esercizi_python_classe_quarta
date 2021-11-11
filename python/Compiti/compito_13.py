import math
n1 = int (input("Inserisci la prima coordinata del primo punto: "))
n2 = int (input("Inserisci la seconda coordinata del primo punto: "))

c1 = int (input("Inserisci la prima coordinata del secondo punto: "))
c2 = int (input("Inserisci la seconda coordinata del secondo punto: "))

punto1 = (n1, n2) 
punto2 = (c1, c2)
distanza = (((punto1[0] - punto1[1]) **2) + ((punto2[0] - punto2[1]) **2))**(1/2)
print(distanza)