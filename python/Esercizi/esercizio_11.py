def stampaGriglia(griglia):
    print(f"{griglia[0]} | {griglia[1]} | {griglia[2]} \n---------\n{griglia[3]} | {griglia[4]} | {griglia[5]} \n---------\n{griglia[6]} | {griglia[7]} | {griglia[8]} \n")

griglia = {0:" ", 1:" ",  2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" "}

partitaFinita = False


while(True):
    ok = True
    while(ok == True):
        mossa1 = int(input("Fai una mossa Giocatore 1:"))
        if(griglia[mossa1] == " "):
            griglia[mossa1] = 'X'
            ok = False

    stampaGriglia(griglia)

    ok = True
    while(ok == True):
        mossa2 = int(input("Fai una mossa Giocatore 2:"))
        if(griglia[mossa2] == " "):
            griglia[mossa2] = 'O'
            ok = False

    stampaGriglia(griglia)