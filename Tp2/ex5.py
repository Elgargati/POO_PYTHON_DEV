import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"POINT({self.x},{self.y})")

# if (  isinstance(x,float))

class Cercle:
    def __init__(self, centre, rayon):
        self.centre = centre
        self.rayon = rayon

    def get_perimetre(self):
        return 2 * math.pi * self.rayon

    def get_surface(self):
        return math.pi * self.rayon**2

    def appartient(self, point):
        distance_centre_point = math.sqrt((point.x - self.centre.x)**2 + (point.y - self.centre.y)**2)
        return distance_centre_point <= self.rayon

    def afficher(self):
        print(f"CERCLE({self.centre.x},{self.centre.y},{self.rayon})")


point1 = Point(0, 0)
point1.afficher()



cercle1 = Cercle(point1, 1)
cercle1.afficher()


print("Périmètre du cercle:", cercle1.get_perimetre())
print("Surface du cercle:", cercle1.get_surface())


point2 = Point(3, 4)
print("Le point appartient au cercle:", cercle1.appartient(point2))
