class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def aire(self):
        return self.longueur * self.largeur
    
    def iscarre(self):
        if self.longueur==self.largeur:
          print("il est carre")
        else:
            print("il n'est pas carre")

rect1 = Rectangle(5 ,3)
perimetre = rect1.perimetre()
aire = rect1.aire()


print("Le périmètre du rectangle est:", perimetre)
print("L'aire du rectangle est:", aire)


