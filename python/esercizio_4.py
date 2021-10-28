#slicing di stringhe, ovvero come si tagliano le stringhe

stringa = "Classe quarta A robotica"

# stringa[15] = "B"
#le stringhe in Python sono IMMUTABILI
# TypeError: 'str' object does not support item assignment

stringa_nuova = stringa[0:14] + "B" + stringa[15:]
print(stringa_nuova)

print(f"Il primo carattere della stringa è {stringa[0]}")
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

#prende i caratteri a partire da quello con indice 0
#fino a quello con indice 6 ESCLUSO
print(stringa[0:6]) 

#prende dal sesto carattere fino all'ultimo
print(stringa[6:])

#prende dal primo carattere fino a quello con indice -2
print(stringa[:-2]) 

#prende tutti i caratteri dal 2 al 14 facendo balzi di 2
print(stringa[2:14:2])

#prende la stringa a salti di -1, quindi stampa la
#stringa al contrario
print(stringa[::-1])

