nome = (input("Inserisci un nome:"))
cognome = (input("Inserisci un cognome:"))
giorno = int(input("Inserisci il giorno in cui sei nato:"))
mese = int(input("Inserisci il mese in cui sei nato:"))
anno = int(input("Inserisci l'anno in cui sei nato:"))

dizionario = {"Nome":nome, "Cognome":cognome, "Giorno":giorno, "Mese":mese, "Anno":anno}

f = open("./testo3.txt", "w")

for chiave in dizionario:
    f.write(f"{dizionario[chiave]} ")

f.close()