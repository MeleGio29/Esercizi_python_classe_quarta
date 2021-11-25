lista = ["uno", "due", "quattro"]
max = lista[0]
for parola in lista:
    if(len(max) < len(parola)):
        max = parola
print(f"La parola {max} è la parola con più lettere")