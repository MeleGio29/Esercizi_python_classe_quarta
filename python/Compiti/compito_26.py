f = open("./testo2.txt", "w")

def ePrimo(num):
    div,count=2,0

    while div <= num/2 and count == 0:
        if num % div == 0:
            count+=1
        else:
            div+=1
    if count == 0:
       return True 
    else:
       return False

nNum = 0
num = 2

while(nNum < 100):
    if((ePrimo(num))):
        f.write(str(num))
        f.write("\n")
        nNum +=1
    num += 1

f.close()