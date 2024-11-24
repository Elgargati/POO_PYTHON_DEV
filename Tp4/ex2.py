from abc import ABC, abstractmethod
from datetime import date,datetime
class Employe:
    def __init__(self, m, n, p, D):
        self.__Matricule = m
        self.__Nom = n
        self.__Prenom = p
        self.__Date = D
    
    def get_Matricule(self):
        return self.__Matricule
    def set_Matricule(self, m):
        self.__Matricule = m

    def get_Nom(self):
        return self.__Nom
    def set_Nom(self, n):
        self.__Nom = n

    def get_Prenom(self):
        return self.__Prenom
    def set_Prenom(self, p):
        self.__Prenom = p
    
    def get_date(self):
        return self.__Date
    def set_date(self, d):
        self.__Date = d

    def __str__(self):
        return f"matricule: {self.__Matricule}, nom: {self.__Nom}, prenom: {self.__Matricule}, date de naissance: {self.__Date}"
    
    @abstractmethod
    def GetSalaire(self):
        pass

class Ouvrier(Employe):
    __Smig=3000
    def __init__(self, m, n, p, D, De):
        super().__init__(m, n, p, D)
        self.__DateEntree = De

    def get_DateEntree(self):
        return self.__DateEntree
    def set_DateEntee(self,De):
        self.__DateEntree = De

    def GetSalaire(self):
        anciente = int((date.today()- self.__DateEntree).days/365.25)
        s = Ouvrier.__Smig + (anciente * 100)
        if s> Ouvrier.__Smig*2:
            s=Ouvrier.__Smig*2
        return s
    
    def __str__(self):
        return str(super().__str__() + f" Date d'entree: {self.__DateEntree}")
    
O1 = Ouvrier(90, "nom1", "prenom1", date(1999, 1,1), date(2004,7,26))
print(O1)
print(O1.GetSalaire())
    
class Cadre(Employe):
    def __init__(self, m, n, p, D, I):
        super().__init__(m, n, p, D)
        self.__indice = I

    def GetSalaire(self):
        if self.__indice ==1: 
            return round(130000/12)
        elif self.__indice == 2:
            return round(150000/12)
        elif self.__indice == 3:
            return round(170000/12)
        elif self.__indice == 4:
            return round(200000/12)
        else : 
            print("entrer une indice valide (entre 1 et 4)")

    def __str__(self):
        return str(super().__str__() + f" indice: {self.__indice}")
    
# ca=Cadre(60,'nom1','prenom1',date(1990,5,12),3)
# print(ca)
# print(ca.GetSalaire())
    
class patron(Employe):
    __chiffre_Affaire = None
    def __init__(self, m, n, p, D, po):
        super().__init__(m, n, p, D)
        self.__pourcentage = po
    
    def get_pourcentage(self):
        return self.__pourcentage
    def set_pourcentage(self, po):
        self.__pourcentage = po

    def GetSalaire(self):
        salaire = (patron.__chiffre_Affaire *self.__pourcentage/100) /12
        return salaire
    def __str__(self):
        return str(super().__str__() + f" pourcentage: {self.__pourcentage}")
    @staticmethod
    def get_CA():
        return patron.__chiffre_Affaire
    @staticmethod
    def set_CA(CA):
        patron.__chiffre_Affaire= CA

# d1 = date(1979, 12, 25)
# d2 = date.today()
# print(int((d2-d1).days/365.25))




# p1=patron(30,'nom1','prenom1',date(1982,3,12),10)
# print(p1)
# print(p1.GetSalaire())



        





    


