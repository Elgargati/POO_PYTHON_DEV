import math as m
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def Norme(self):
        d=m.sqrt(m.pow(self.x,2)+m.pow(self.y,2))
        
        return d 
R1=Point(2,5)
print(R1.Norme())

