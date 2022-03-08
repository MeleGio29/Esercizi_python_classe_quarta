def main():
    f = open("./medals.csv", "r")
    righe = f.readlines()
    f.close()

    numeroGold, numeroSilver, numeroBronze = 0, 0, 0

    dizionario = {"Gold":numeroGold, "Silver":numeroSilver, "Bronze":numeroBronze}

    for riga in righe:
        lista = riga.split(",")

        if(lista[0] == "Gold"):
            if(lista[8] == "Italy"):
                numeroGold = numeroGold + 1
                dizionario["Gold"] = numeroGold
        elif(lista[0] == "Silver"):
            if(lista[8] == "Italy"):
                numeroSilver = numeroSilver + 1
                dizionario["Silver"] = numeroSilver
        elif(lista[0] == "Bronze"):
            if(lista[8] == "Italy"):
                numeroBronze = numeroBronze + 1
                dizionario["Bronze"] = numeroBronze

    print(dizionario)

if __name__ == "__main__":
    main()