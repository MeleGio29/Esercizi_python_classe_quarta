class Coda():
    def __init__(self):
        self.coda = []

    def enqueue(self, elemento):
        self.coda.append(elemento)

    def dequeue(self):
     if(len(self.coda) != 0):
        return self.coda.pop(0)
     else:
        return None

    def print(self):
        print(self.coda)

c1 = Coda()

risp = 's'

while risp == 's':
    num = int(input("Inserisci un elemento nella coda: "))
    c1.enqueue(num)
    risp = input("Vuoi inserirne un altro? [s] [n] ")

c1.print()