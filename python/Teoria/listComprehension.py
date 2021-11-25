parole = ["ciao", "anna", "Alice"]
palindrome = [parola for parola in parole if parola == parola[::-1]]
maiuscole = [parola for parola in parole if(parola[0] >= 'A' and parola[0] <= 'Z')]

print(palindrome)
print(maiuscole)

#serve per filtrare una lista dichiarata precedentemente