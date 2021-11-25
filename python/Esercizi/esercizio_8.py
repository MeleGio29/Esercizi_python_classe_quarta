lista = []
ok = "s"
while(ok == 's'):
    numero = int(input("Inserisci un numero: "))
    lista.append(numero)
    ok = input("Inserisci 's' se vuoi continuare. ")
print(lista)