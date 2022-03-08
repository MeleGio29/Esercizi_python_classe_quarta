def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) != 0:
        return pila.pop()
    else:
        return None

pila = []
risp = 's'

while risp == 's':
    num = int(input("Inserisci un numero da aggiungere alla pila: "))
    push(pila, num)
    risp = input("Vuoi inserirne un altro? [s] [n] ")

elemento = pop(pila)

while elemento != None:
    print(elemento)
    elemento = pop(pila)
