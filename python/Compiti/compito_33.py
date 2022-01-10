lista = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

def cifrario(frase, chiave):
    parolaDecodificata = ""

    for lettera in frase:
        ok = False
        k = 0

        while(ok == False):
            if lettera == lista[k]:
                lettera = lista[(k + chiave) % len(lista)]
                parolaDecodificata = parolaDecodificata + lettera
                ok = True
            k += 1
    
    return parolaDecodificata

def main():
    domanda = (input("Vuoi CODIFICARE o DECODIFICARE?"))
    chiave = 3
    
    if(domanda == "DECODIFICARE"):
        parola = input("Inserisci una parola da decodificare: ")
        parola = parola.upper()
        parolaDecodificata = cifrario(parola, -1 * chiave)
        print(f"PAROLA DECODIFICATA: {parolaDecodificata}")
    else:
        parola = input("Inserisci una parola da codificare: ")
        parola = parola.upper()
        parolaCodificata = cifrario(parola, chiave)
        print(f"PAROLA CODIFICATA: {parolaCodificata}")

if __name__ == "__main__":
    main()