def isPalindroma(str):
    if(str == str[::-1]):
        return True
    else:
        return False

lista,listaMaiuscole,listaPalindrome=["parola1","anna","reer","Parola2","Parola3"],[],[]

for parola in lista:
    if(isPalindroma(parola)):
        listaPalindrome.append(parola)
    
    if(parola[0].isupper()):
        listaMaiuscole.append(parola)

print(f"Lista iniziale {lista} , Lista maiuscole  {listaMaiuscole} , lista palindromi  {listaPalindrome}")