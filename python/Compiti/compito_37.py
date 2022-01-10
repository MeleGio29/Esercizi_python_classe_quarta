def controlloDIM(m):
    """controllo numero inserito utente"""
    if(m >= 0 and m <= 41):
        ok = True
    else:
        ok = False
    return ok

def controllo(m):
    """controllo piena o vuota"""
    if ( griglia[m] == None):
        ok = True
    else:
       ok = False
    return ok

def disegnaGriglia(g, g1, g2):
    for i in range(42):
        if g[i] == None:
            print("   ",end="")
        elif g[i] == g1:
            print(" X ",end="")
        elif g[i] == g2:
            print(" O ",end="")
        
        if(i==6 or i==13 or i==20 or i==27 or i==34):
            print("\n---------------------------")
        elif i==41:
            print("\n")
        else: 
            print("|",end="")

def controlloVittoria(griglia):
    vittoria = False
    #prima riga
    if griglia[0]==griglia[1]==griglia[2]==griglia[3] and griglia[0]!=None:
        vittoria = True
    elif griglia[1]==griglia[2]==griglia[3]==griglia[4] and griglia[1]!=None:
        vittoria = True
    elif griglia[2]==griglia[3]==griglia[4]==griglia[5] and griglia[2]!=None:
        vittoria = True
    elif griglia[3]==griglia[4]==griglia[5]==griglia[6] and griglia[3]!=None:
        vittoria = True
    #seconda riga
    elif griglia[7]==griglia[7]==griglia[9]==griglia[10] and griglia[7]!=None:
        vittoria = True
    elif griglia[8]==griglia[9]==griglia[10]==griglia[11] and griglia[8]!=None:
        vittoria = True
    elif griglia[9]==griglia[10]==griglia[11]==griglia[12] and griglia[9]!=None:
        vittoria = True
    elif griglia[10]==griglia[11]==griglia[12]==griglia[13] and griglia[10]!=None:
        vittoria = True
    #terza riga
    elif griglia[14]==griglia[15]==griglia[16]==griglia[17] and griglia[14]!=None:
        vittoria = True
    elif griglia[15]==griglia[16]==griglia[17]==griglia[18] and griglia[15]!=None:
        vittoria = True
    elif griglia[16]==griglia[17]==griglia[18]==griglia[19] and griglia[16]!=None:
        vittoria = True
    elif griglia[17]==griglia[18]==griglia[19]==griglia[20] and griglia[17]!=None:
        vittoria = True
    #quarta riga
    elif griglia[21]==griglia[22]==griglia[23]==griglia[24] and griglia[21]!=None:
        vittoria = True
    elif griglia[22]==griglia[23]==griglia[24]==griglia[25] and griglia[22]!=None:
        vittoria = True
    elif griglia[23]==griglia[24]==griglia[25]==griglia[26] and griglia[23]!=None:
        vittoria = True
    elif griglia[24]==griglia[25]==griglia[26]==griglia[27] and griglia[24]!=None:
        vittoria = True
    #quinta riga
    elif griglia[28]==griglia[29]==griglia[30]==griglia[31] and griglia[28]!=None:
        vittoria = True
    elif griglia[29]==griglia[30]==griglia[31]==griglia[32] and griglia[29]!=None:
        vittoria = True
    elif griglia[30]==griglia[31]==griglia[32]==griglia[33] and griglia[30]!=None:
        vittoria = True
    elif griglia[31]==griglia[32]==griglia[33]==griglia[34] and griglia[31]!=None:
        vittoria = True
    #sesta riga
    elif griglia[35]==griglia[36]==griglia[37]==griglia[38] and griglia[35]!=None:
        vittoria = True
    elif griglia[36]==griglia[37]==griglia[38]==griglia[39] and griglia[36]!=None:
        vittoria = True
    elif griglia[37]==griglia[38]==griglia[39]==griglia[40] and griglia[37]!=None:
        vittoria = True
    elif griglia[38]==griglia[39]==griglia[40]==griglia[41] and griglia[38]!=None:
        vittoria = True
    #prima colonna
    elif griglia[0]==griglia[7]==griglia[14]==griglia[21] and griglia[0]!=None:
        vittoria = True
    elif griglia[7]==griglia[14]==griglia[21]==griglia[28] and griglia[7]!=None:
        vittoria = True
    elif griglia[14]==griglia[21]==griglia[28]==griglia[35] and griglia[14]!=None:
        vittoria = True
    #seconda colonna
    elif griglia[1]==griglia[8]==griglia[15]==griglia[22] and griglia[1]!=None:
        vittoria = True
    elif griglia[8]==griglia[15]==griglia[22]==griglia[29] and griglia[8]!=None:
        vittoria = True
    elif griglia[15]==griglia[22]==griglia[29]==griglia[36] and griglia[15]!=None:
        vittoria = True
    #terza colonna
    elif griglia[2]==griglia[9]==griglia[16]==griglia[23] and griglia[2]!=None:
        vittoria = True
    elif griglia[9]==griglia[16]==griglia[23]==griglia[30] and griglia[9]!=None:
        vittoria = True
    elif griglia[16]==griglia[23]==griglia[30]==griglia[37] and griglia[16]!=None:
        vittoria = True
    #quarta colonna
    elif griglia[3]==griglia[10]==griglia[17]==griglia[24] and griglia[3]!=None:
        vittoria = True
    elif griglia[10]==griglia[17]==griglia[24]==griglia[31] and griglia[10]!=None:
        vittoria = True
    elif griglia[17]==griglia[24]==griglia[31]==griglia[38] and griglia[17]!=None:
        vittoria = True
    #quinta colonna
    elif griglia[4]==griglia[11]==griglia[18]==griglia[25] and griglia[4]!=None:
        vittoria = True
    elif griglia[11]==griglia[18]==griglia[25]==griglia[32] and griglia[11]!=None:
        vittoria = True
    elif griglia[18]==griglia[25]==griglia[32]==griglia[39] and griglia[18]!=None:
        vittoria = True
    #sesta colonna
    elif griglia[5]==griglia[12]==griglia[19]==griglia[26] and griglia[5]!=None:
        vittoria = True
    elif griglia[12]==griglia[19]==griglia[26]==griglia[33] and griglia[12]!=None:
        vittoria = True
    elif griglia[19]==griglia[26]==griglia[33]==griglia[40] and griglia[19]!=None:
        vittoria = True
    #settima colonna
    elif griglia[6]==griglia[13]==griglia[20]==griglia[27] and griglia[6]!=None:
        vittoria = True
    elif griglia[13]==griglia[20]==griglia[27]==griglia[34] and griglia[13]!=None:
        vittoria = True
    elif griglia[20]==griglia[27]==griglia[34]==griglia[41] and griglia[20]!=None:
        vittoria = True
    #diagonali /
    elif griglia[21]==griglia[15]==griglia[9]==griglia[3] and griglia[21]!=None:
        vittoria = True
    elif griglia[28]==griglia[22]==griglia[16]==griglia[10] and griglia[28]!=None:
        vittoria = True
    elif griglia[35]==griglia[29]==griglia[23]==griglia[17] and griglia[35]!=None:
        vittoria = True
    elif griglia[36]==griglia[30]==griglia[24]==griglia[18] and griglia[36]!=None:
        vittoria = True
    elif griglia[37]==griglia[31]==griglia[25]==griglia[19] and griglia[37]!=None:
        vittoria = True
    elif griglia[38]==griglia[32]==griglia[26]==griglia[20] and griglia[35]!=None:
        vittoria = True
    elif griglia[22]==griglia[16]==griglia[10]==griglia[4] and griglia[22]!=None:
        vittoria = True
    elif griglia[29]==griglia[23]==griglia[17]==griglia[11] and griglia[29]!=None:
        vittoria = True
    elif griglia[30]==griglia[24]==griglia[18]==griglia[12] and griglia[30]!=None:
        vittoria = True
    elif griglia[31]==griglia[25]==griglia[19]==griglia[13] and griglia[31]!=None:
        vittoria = True
    elif griglia[24]==griglia[18]==griglia[12]==griglia[6] and griglia[24]!=None:
        vittoria = True
    elif griglia[23]==griglia[17]==griglia[11]==griglia[5] and griglia[23]!=None:
        vittoria = True
    #diagonali \
    elif griglia[3]==griglia[11]==griglia[19]==griglia[27] and griglia[3]!=None:
        vittoria = True
    elif griglia[10]==griglia[18]==griglia[26]==griglia[34] and griglia[10]!=None:
        vittoria = True
    elif griglia[17]==griglia[25]==griglia[33]==griglia[41] and griglia[17]!=None:
        vittoria = True
    elif griglia[16]==griglia[24]==griglia[32]==griglia[40] and griglia[16]!=None:
        vittoria = True
    elif griglia[15]==griglia[23]==griglia[31]==griglia[39] and griglia[15]!=None:
        vittoria = True
    elif griglia[14]==griglia[22]==griglia[30]==griglia[38] and griglia[14]!=None:
        vittoria = True
    elif griglia[2]==griglia[10]==griglia[18]==griglia[26] and griglia[2]!=None:
        vittoria = True
    elif griglia[9]==griglia[17]==griglia[25]==griglia[33] and griglia[9]!=None:
        vittoria = True
    elif griglia[8]==griglia[16]==griglia[24]==griglia[32] and griglia[8]!=None:
        vittoria = True
    elif griglia[7]==griglia[15]==griglia[23]==griglia[31] and griglia[7]!=None:
        vittoria = True
    elif griglia[0]==griglia[8]==griglia[16]==griglia[24] and griglia[0]!=None:
        vittoria = True
    elif griglia[1]==griglia[9]==griglia[17]==griglia[25] and griglia[1]!=None:
        vittoria = True

    return vittoria

def pareggiOvittoria(conta):
    ok = False
    if (conta == 42):
        print(f"PAREGGIO TRA {G1} E {G2}")
        ok = True   
    elif(controlloVittoria(griglia) == True):
        if(conta%2 == 0):
            print(f"HA VINTO {G2}") 
            ok = True            
        else:
            print(f"HA VINTO {G1}")
            ok = True  
    return ok   

griglia = {0: None, 1: None,2: None,3: None,4: None,5: None,6: None,7: None,8: None,9: None,10: None, 11: None,12: None,13: None,14: None,15: None,
            16: None,17: None,18: None,19: None, 20: None, 21: None, 22: None,23: None,24: None,25: None,26: None,27: None,28: None,29: None, 30: None, 
            31: None,32: None,33: None,34: None,35: None,36: None,37: None,38: None,39: None,40: None, 41: None,42: None }
G1 = input("Inserisci Giocatore1[X]: ")
G2 = input("Inserisci Giocatore2[O]: ")

disegnaGriglia(griglia,G1,G2)
conta = 0
while(True):
    c1 = False
    print(f"{G1}")
    while c1 == False:
        m = int(input("Inserici numero di casella: "))
        if controlloDIM(m):
            if controllo(m):
                griglia[m] = G1
                c1 = True
                conta = conta + 1
    
    disegnaGriglia(griglia,G1,G2)

    if pareggiOvittoria(conta):
        break
    
    c2 = False
    print(f"{G2}")
    while c2 == False:
        m = int(input("Inserici numero di casella: "))
        if controlloDIM(m):
            if controllo(m):
                griglia[m] = G2
                c2 = True
                conta=conta +1
              
    disegnaGriglia(griglia,G1,G2)
    
    if pareggiOvittoria(conta):
        break