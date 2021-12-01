import turtle
snow = turtle.Turtle()
finestra = turtle.Screen()

for riga in range(9):
    snow.forward(100)
    snow.back(20)
    snow.left(45)
    snow.forward(20)
    snow.back(20)
    snow.right(45)
    snow.forward(20)
    snow.goto(0,0)
    snow.right(45)

    snow.speed(0)

finestra.exitonclick()