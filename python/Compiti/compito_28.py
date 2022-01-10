num = int(input("Inserisci un valore: "))

potenzaDue = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

lista = [numeri for numeri in potenzaDue if numeri <= num]

print(lista)