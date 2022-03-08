def numeroDizionario(mappa):
    adiacenze, liberi, dim = {}, 0, 4

    #dizionario delle adiacenze (chiavi: le celle libere,valore: lista dei possibili movimenti)

    for k in range(0,dim):
        for j in (0,dim):
            #print (posto)
            if mappa[k[j]] == 0:
                adiacenze[liberi] = [k, j]
                liberi += 1

    return adiacenze

def controlloBordi(lista):
    dizionarioBooleano, ritorno = {"su":None, "giu":None, "destra":None, "sinistra":None}

    if lista[0] == 0:
        dizionarioBooleano["su"] = False
    if lista[1] == 0:
        dizionarioBooleano["sinistra"] = False
    if lista[0] == 3:
        dizionarioBooleano["giu"] = False
    if lista[1] == 3:
        dizionarioBooleano["destra"] = False
    
    for chiave in dizionarioBooleano:
        if dizionarioBooleano[chiave] == False: ritorno.append(chiave)

    return ritorno

def trovaAdiacenze(mappa, dizionarioCelleVuote):
    dizionarioCelleVuote, opzioniSbagliate = {}, []


def main():
    mappa = [[0,0,0,1], [1, 0, 0, 1], [0, 0, 0, 0,],[1, 1, 1, 0]]

    dizionarioCelleVuote = numeroDizionario(mappa)
    print(f"Dizionario delle celle dove si può andare: {dizionarioCelleVuote}")
    print(f"")

if __name__ == "__main__":
    main()