def controllaComm(testo):
    commento=0
    for linea in testo:
        for parola in linea.split():
            if parola == "//":
                commento+=1
    
    return commento

f=open("./main.c","r")

testo ,  k = f.readlines()  , 0
nRighe=len(testo)

for linea in testo:
    for parola in linea.split():
        if parola == "printf":
            k+=1

comm = controllaComm(testo)

print(f"Le righe del file sono : {nRighe} , printf è stata chiamata {k} e sono stati inseriti {comm} commenti del codice)")