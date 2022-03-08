class Pila():
    def __init__(self):
        self.pila = []
    
    def push(self, elemento):
        self.pila.append(elemento)
    
    def pop(self):
        if len(self.pila) != 0:
          return self.pila.pop()
        else:
          return None

    def print(self):
        print(self.pila)

p1 = Pila() #istanza classe Pila

risp = 's'

while risp == 's':
    num = int(input("Inserisci un elemento nella pila: "))
    p1.push(num)
    risp = input("Vuoi inserirne un altro? [s] [n] ")

p1.print()