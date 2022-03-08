import turtle
import random

def disegno(x,y):
    Stella.penup()
    Stella.setposition(x,y)
    Stella.pendown()
    Stella.speed(100)

    for _ in range(5):
        Stella.forward(280)
        Stella.right(144)

Stella = turtle.Turtle()
finestra = turtle.Screen()

for _ in range(50):
    disegno(random.randint(-480,480),random.randint(-480,480))

finestra.exitonclick()




