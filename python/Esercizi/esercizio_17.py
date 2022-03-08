import turtle

class quadrato():
    def __init__(self, lato, x, y):
        self.lato = lato
        self.x = x
        self.y = y

    def area(self):
        area = self.lato **2
        return area
    
    def perimetro(self):
        perimetro = self.lato * 4
        return perimetro

    def verifica(self, x2, y2):
        ok = True

        if (x2 < self.x or x2 > self.x + self.lato or y2 < self.y or y2 > self.y + self.lato):
            ok = False

        return ok

    def disegna(self):
        pen = turtle.Turtle()
        pen.goto(self.x, self.y)

def main():
    valore = int(input("Inserisci un valore per il lato [cm]: "))
    coordX = int(input("Inserisci un valore per la coordinata X: "))
    coordY = int(input("Inserisci un valore per la coordinata Y: "))

    q = quadrato(valore, coordX, coordY)
    area = q.area()
    print(f"L'area del quadrato è vasta {area}cm")
    perimetro = q.perimetro()
    print(f"Il perimetro del quadrato è lungo {perimetro}cm")
    
    if(q.verifica(10, 10) == True):
        print("Il punto appartiene al quadrato")
    else:
        print("Il punto NON appartiene al quadrato")

if __name__ == "__main__":
    main()