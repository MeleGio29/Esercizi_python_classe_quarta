stringa = input("Inserisci una  stringa: ")
controllo = lambda stringa: (stringa.isupper())

ok = controllo(stringa[0])

if(ok == True):
    print("Inizia con una maiuscola ")
else:
    print("Non inizia con una maiuscola ")