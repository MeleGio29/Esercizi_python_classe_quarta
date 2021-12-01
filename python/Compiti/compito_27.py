nome = (input("Inserisci un nome:"))
cognome = (input("Inserisci un cognome:"))
giorno = int(input("Inserisci il giorno in cui sei nato:"))
mese = int(input("Inserisci il mese in cui sei nato:"))
anno = int(input("Inserisci l'anno in cui sei nato:"))

dizionario = {"Nome":{nome}, "Cognome":{cognome}, "Giorno":{giorno}, "Mese":{mese}, "Anno":{anno}}

f = open("./testo3.txt", "w")

f.write(dizionario["Nome"])
f.write("\n")
f.write(dizionario["Cognome"])
f.write("\n")
f.write(dizionario["Giorno"])
f.write("\n")
f.write(dizionario["Mese"])
f.write("\n")
f.write(dizionario["Anno"])

f.close()