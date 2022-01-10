def data():       
    mese = input("mese: ")
    anno = input("anno: ")
    return mese,anno

def articoli(): 
    lista = []
    for _ in range (5):
        art =  str(input("inseririsci articolo: "))
        lista.append(art)
    return lista


f = open("./prezzi.csv","r")
righe = f.readlines()

riga,colonna = 0,0

mese,anno = data()
listaSpesa = articoli()        

f.close()
