classi = ["4arob", "3arob", "5brob", "4achi", "3ainf"]
indirizzi = {"rob":"Smart robot", "chi":"Chimica", "inf":"Informatica"}
for indice, classe in enumerate(classi):
    indirizzo = indirizzi[classe[-3:]]
    print(f"Posizione {indice + 1} nella lista: ")
    print(f"La classe {classe} è dell'indirizzo {indirizzo}", end = "\n\n")
