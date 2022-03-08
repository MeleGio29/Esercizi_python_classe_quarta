def enqueue(coda, elemento):
    coda.append(elemento)

def dequeue(coda):
    if(len(coda) != 0):
        return coda.pop(0)
    else:
        return None

coda = []
risp = 's'

while risp == 's':
    num = int(input("Inserisci un numero da aggiungere alla coda: "))
    enqueue(coda, num)
    risp = input("Vuoi inserirne un altro? [s] [n] ")

elemento = dequeue(coda)

while elemento != None:
    print(elemento)
    elemento = dequeue(coda)
