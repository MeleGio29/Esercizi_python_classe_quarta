import Pile_Code as pc #alias

def main():
    c = pc.Coda()
    c2 = pc.Coda()
    p = pc.Pila()

    risp = 's'
    conta = 0

    while risp == 's':
        num = int(input("Inserisci un numero da aggiungere alla coda: "))
        c.enqueue(num)
        risp = input("Vuoi inserirne un altro? [s] [n] ")
        conta = conta + 1

    for _ in range(conta):
        v = c.dequeue()
        p.push(v)

    for _ in range(conta):
        r = p.pop()
        c2.enqueue(r)

    c.print()
    c2.print()

if __name__ == "__main__":
    main()