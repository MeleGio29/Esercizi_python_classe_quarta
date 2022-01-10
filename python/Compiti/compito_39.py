f=open("./covid-19_gen1.txt","r")
testo,dict = f.readlines(),{"A" : 0 ,"T": 0 ,"C": 0 ,"G": 0 }

for line in testo:
        for char in line:
           if char in dict:
               dict[char]+=1

print (dict)