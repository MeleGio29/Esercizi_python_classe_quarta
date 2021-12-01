import turtle
snow = turtle.Turtle()
finestra = turtle.Screen()

f = open("./testo.txt", "w")

for riga in range(9):
    snow.forward(100)
    f.write("forward:" + str(100) + "\n")

    snow.back(20)
    f.write("back:" + str(20) + "\n")

    snow.left(45)
    f.write("left:" + str(45) + "\n")

    snow.forward(20)
    f.write("forward:" + str(20) + "\n")

    snow.back(20)
    f.write("back:" + str(20) + "\n")

    snow.right(45)
    f.write("right:" + str(45) + "\n")

    snow.forward(20)
    f.write("forward:" + str(20) + "\n")

    snow.goto(0,0)
    f.write("goto:(0,0) \n")

    snow.right(45)
    f.write("right:" + str(45) + "\n")

    snow.speed(0)
    f.write("speed:" + str(0) + "\n")

finestra.exitonclick()

f.close()