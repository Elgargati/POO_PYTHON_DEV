from abc import ABC, abstractmethod
class Media(ABC):
    def __init__(self, t):
        self.__titre = t
        self._e = False
    
    def get_titre(self):
        return self.__titre
    def set_titre(self, t):
        self.__titre = t
    
    def get_e(self):
        return self._e
    # def set_e(self, e):
    #     self._e = e << _e est "protected", 
    
    def get_eStatus(self):
        if self._e == True:
            return "est pas displonible a le moment"
        elif self._e ==False:
            return "est disponible a le moment"

    def __str__(self):
        return f"titre: {self.__titre}"
    @abstractmethod
    def Emprunter(self):
        pass
    @abstractmethod
    def Retourner(self):
        pass


class Livre(Media):
    def __init__(self, t, a, g):
        super().__init__(t)
        self.__auteur = a
        self.__genre = g

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, a):
        self.__auteur = a
    
    def get_genre(self):
        return self.__genre
    def set_genre(self, g):
        self.__genre = g
    
    def __str__(self):
        return super().__str__() + f", auteur: {self.__auteur}, genre: {self.__genre}, et {self.get_eStatus()} "
    
    def Emprunter(self):
        if(self.get_e() == False):
            self._e = True 
            print(f"le livre {self.get_titre()}, par l'auteur: {self.__auteur} a ete emprunte avec succes")
    def Retourner(self):
        if (self.get_e()):
            self._e = False
            print(f"le livre {self.get_titre()}, par l'auteur: {self.__auteur} a ete restitue avec success")



class CD(Media):
    def __init__(self, t, a, d):
        super().__init__(t)
        self.__artiste = a
        self.__duree = d
    def get_artiste(self):
        return self.__artiste
    def set_aritsite(self, a):
        self.__artiste = a
    
    def get_duree(self):
        return self.__duree
    def set_duree(self, d):
        self.__duree = d
    
    def __str__(self):
        return super().__str__() + f", artiste: {self.__artiste}, duree: {self.__duree}, et {super().get_eStatus()} "
    
    def Emprunter(self):
        if(self._e == False):
            self._e =True  
            print(f"le CD {self.get_titre()}, par l'artiste: {self.__artiste} a ete emprunte avec succes")
        else:
            print("le Cd est deja emprunte")
    def Retourner(self):
        if (self._e):
            self._e = False
            print(f"le CD {self.get_titre()}, par l'artiste: {self.__artiste} a ete restitue avec success")
        else:
            print("Le Cd est deja existent")



# CD1 = CD("titre01", False, "artiste01", "06:40")
# print(CD1)
# CD1.Emprunter()
# print(CD1)
# print(CD1.get_duree())
# CD1.Retourner()
# print(CD1)


# L1 = Livre("shsufhdusfhd", True)
            




L1 = Livre("Titre01", "auteur01", "genre01")
print(L1)
L1.Emprunter()
print(L1)
            









# cd1 = CD("Titre02", "artiste02", "05:40")
# print(cd1.get_e())
# cd1.Emprunter()
# print(cd1)
# print(cd1.get_e())
# cd1.Emprunter()
# # cd1.Retourner()
# # print(cd1)
# # print(cd1.get_e())


