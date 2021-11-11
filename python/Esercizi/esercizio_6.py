numero = int (input("Quale operazione desideri eseguire? "))
n1 = int(input("Inserisci un numero: "))
n2 = int(input("Inserisci un numero: "))
if(numero == 0):
    somma = n1 + n2
    print(somma)
elif(numero == 1):
    sottrazione = n1 - n2
    print(sottrazione)
elif(numero == 2):
    moltiplicazione = n1 * n2
    print(moltiplicazione)
else:
    divisione = n1 / n2
    print(divisione)