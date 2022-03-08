def fibonacci(n):
    if n < 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Introduci un valore: "))

    for k in range(0, n):
        print(fibonacci(k))

if __name__ == "__main__":
    main()