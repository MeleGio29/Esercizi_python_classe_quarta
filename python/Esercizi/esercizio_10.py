import turtle
snow = turtle.Turtle()
finestra = turtle.Screen()
f = open("./testo.txt", "r")

righe = f.readlines()
f.close()

for riga in righe:
    lista = riga.split(":")
    print(lista)

    if(lista[0] == "forward"):
        snow.forward(int(lista[1][:-1]))
    elif(lista[0] == "back"):
        snow.back(int(lista[1][:-1]))
    elif(lista[0] == "left"):
        snow.left(int(lista[1][:-1]))
    elif(lista[0] == "right"):
        snow.right(int(lista[1][:-1]))
    elif(lista[0] == "goto"):
        snow.goto(0, 0)
    elif(lista[0] == "speed"):
        snow.speed(int(lista[1][:-1]))

finestra.exitonclick()