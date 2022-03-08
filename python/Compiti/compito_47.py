import turtle
import random

s = turtle.Turtle()
finestra = turtle.Screen()

class Stella():
    def __init__(self, x, y, dim):
        self.stella = []
        self.x = x
        self.y = y
        self.dim = dim

    def disegna(self):
        s.penup()
        s.setposition(self.x, self.y)
        s.pendown()
        s.speed(100)

        for _ in range(5):
            s.forward(self.dim)
            s.right(144)

def main():
    for _ in range(100):
        s = Stella(random.randint(-480,480),random.randint(-480,480),random.randint(10,30))
        s.disegna()
    finestra.exitonclick()

if __name__ == "__main__":
    main()