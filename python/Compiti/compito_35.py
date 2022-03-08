lista = ["zero", "uno", "due", "tre"]
dict = {}

for k, elemento in enumerate(lista): #python styleeeeee
    dict[k] = elemento
print(dict)

#dictionary comprehension
#dizionario = {x: elemento for x, elemento in enumerate(lista)}