#1) chiedere stringa utente
#2) ciclo sulla stringa in cui snobbate tutto ciò che non è ()[]{}
#3) se trovo parentesi aperta faccio push
#4) se trovo parentesi chiusa faccio pop

stringa = "abc()"

for _ in stringa:
    