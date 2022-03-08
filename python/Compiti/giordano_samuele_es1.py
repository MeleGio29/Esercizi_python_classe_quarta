import random

def spostamentoCasuale():
    spostamento = 0
    while (spostamento == 0):
        spostamento = random.randint(-1, 1)
    
    return spostamento

lista = [spostamentoCasuale() for _ in range(5 * 24 * 60 * 60)]

spostamentoFinale = 0

for spostamenti in lista:
    spostamentoFinale = spostamentoFinale + spostamenti

print(f"Lo spostamento finale è di: {spostamentoFinale}cm")
