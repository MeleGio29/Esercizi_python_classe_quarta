def controlloVittoriaGiocatore1(griglia):
    ok = False

    if(griglia[0] == 'X' and griglia[1] == 'X' and griglia[2] == 'X'):
        ok = True
    elif(griglia[0] == 'X' and griglia[4] == 'X' and griglia[8] == 'X'):
        ok = True
    elif(griglia[0] == 'X' and griglia[3] == 'X' and griglia[6] == 'X'):
        ok = True
    elif(griglia[3] == 'X' and griglia[4] == 'X' and griglia[5] == 'X'):
        ok = True
    elif(griglia[6] == 'X' and griglia[7] == 'X' and griglia[8] == 'X'):
        ok = True
    elif(griglia[1] == 'X' and griglia[4] == 'X' and griglia[7] == 'X'):
        ok = True
    elif(griglia[2] == 'X' and griglia[5] == 'X' and griglia[8] == 'X'):
        ok = True
    elif(griglia[2] == 'X' and griglia[4] == 'X' and griglia[6] == 'X'):
        ok = True

    return ok

def controlloVittoriaGiocatore2(griglia):
    ok = False

    if(griglia[0] == 'O' and griglia[1] == 'O' and griglia[2] == 'O'):
        ok = True
    elif(griglia[0] == 'O' and griglia[4] == 'O' and griglia[8] == 'O'):
        ok = True
    elif(griglia[0] == 'O' and griglia[3] == 'O' and griglia[6] == 'O'):
        ok = True
    elif(griglia[3] == 'O' and griglia[4] == 'O' and griglia[5] == 'O'):
        ok = True
    elif(griglia[6] == 'O' and griglia[7] == 'O' and griglia[8] == 'O'):
        ok = True
    elif(griglia[1] == 'O' and griglia[4] == 'O' and griglia[7] == 'O'):
        ok = True
    elif(griglia[2] == 'O' and griglia[5] == 'O' and griglia[8] == 'O'):
        ok = True
    elif(griglia[2] == 'O' and griglia[4] == 'O' and griglia[6] == 'O'):
        ok = True
    
    return ok
        

def stampaGriglia(griglia):
    print(f"{griglia[0]} | {griglia[1]} | {griglia[2]} \n---------\n{griglia[3]} | {griglia[4]} | {griglia[5]} \n---------\n{griglia[6]} | {griglia[7]} | {griglia[8]} \n")

griglia = {0:" ", 1:" ",  2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" "}

partitaFinita1 = False
partitaFinita2 = False

while(partitaFinita1 == True or partitaFinita2 == True):
    ok = True
    while(ok == True):
        mossa1 = int(input("Fai una mossa Giocatore 1:"))
        if(griglia[mossa1] == " "):
            griglia[mossa1] = 'X'
            ok = False

    stampaGriglia(griglia)
    partitaFinita1 = controlloVittoriaGiocatore1(griglia)

    if(partitaFinita1 == True):
        print("Giocatore 1 HAI VINTO!!!")

    ok = True
    while(ok == True):
        mossa2 = int(input("Fai una mossa Giocatore 2:"))
        if(griglia[mossa2] == " "):
            griglia[mossa2] = 'O'
            ok = False

    stampaGriglia(griglia)
    partitaFinita2 = controlloVittoriaGiocatore2(griglia)

    if(partitaFinita2 == True):
        print("Giocatore 2 HAI VINTO!!!")