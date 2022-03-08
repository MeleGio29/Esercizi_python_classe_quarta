import turtle

griglia = turtle.Turtle()
finestra = turtle.Screen()

lato = 100

for _ in range(4):
    griglia.forward(lato * 4)
    griglia.left(90)
    griglia.forward(lato)
    griglia.right(90)
    griglia.back(lato * 4)
    griglia.right(90)
    griglia.forward(lato)
    griglia.left(90)

    griglia.speed(0)

for _ in range(4):
    griglia.forward(lato)
    griglia.left(90)
    griglia.forward(lato * 4)
    griglia.right(90)
    griglia.forward(lato)
    griglia.right(90)
    griglia.forward(lato * 4)
    griglia.left(90)
    griglia.forward(lato)
    griglia.forward(lato * 4)
    griglia.left(90)
    griglia.forward(lato)

    griglia.speed(0)

finestra.exitonclick()