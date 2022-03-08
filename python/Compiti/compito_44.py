def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n - 1)

def main():
    n = int(input("Scegli un elemento: "))
    fatt = fattoriale(n)

    print(fatt)
    
if __name__ == "__main__":
    main()