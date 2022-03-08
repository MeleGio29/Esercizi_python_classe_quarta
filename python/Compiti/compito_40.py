def data():       
    mese = input("Inserisci il mese: ")
    anno = input("Inserisci l'anno: ")
    return mese, anno

def articoli(): 
    lista = []
    for _ in range(5):
        articolo =  str(input("Inserisci articolo: "))
        lista.append(articolo)
    return lista

f = open("./prezzi.csv","r")
righe = f.readlines()
f.close()

riga, colonna = 0, 0

mese, anno = data()
listaArticoli = articoli()