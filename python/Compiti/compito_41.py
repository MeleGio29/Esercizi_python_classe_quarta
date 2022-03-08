def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    return pila.pop()

pila = [1, 2, 3, 4]

push(pila, 9999)
print(pila)
pop(pila)
print(pila)