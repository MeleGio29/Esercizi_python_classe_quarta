f = open("./testo2.txt", "w")

def ePrimo(num):
    div,count=2,0

    while div<=num/2 and count==0:
        if num%div==0:
            count+=1
        else:
            div+=1
    if count==0:
       return True 
    else:
       return False

conta = 0

for num in range(2,1000):
    if((ePrimo(num))):
        f.write(f"{num} \n")
        conta+=1

f.close()