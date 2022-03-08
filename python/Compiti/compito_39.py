f=open("./covid-19_gen1.txt","r")
testo, dizionario = f.readlines(),{"A" : 0 ,"T": 0 ,"C": 0 ,"G": 0 }

for line in testo:
        for char in line:
           if char in dizionario:
               dizionario[char]+=1

print (dizionario)