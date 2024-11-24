class Rectangle:
    def __init__(self,Lon=0,Lar=0):
        self.longureur=Lon
        self.largueur=Lar
    def Perimetre(self):
        P=2*(self.longureur + self.largueur)
        return P
    def Aire(self):
        A=(self.largueur * self.largueur)
        return A
    def EstCarre(self):
        if (self.largueur == self.longureur) and (self.largueur != 0 and self.longureur !=0 ):
            return("Il s'agit d'un carre")
        else:
            return("Il ne s'agit pas un carre")

    def AfficherRectangle(self):
        print(f"Longueur [{self.longureur}] - Largueur [{self.largueur}] - Perimetre [{self.Perimetre()}] - Aire [{self.Aire()}] - {self.EstCarre()}")
    
P=Rectangle(5,5)
P.AfficherRectangle()
P1=Rectangle()
P1.AfficherRectangle()