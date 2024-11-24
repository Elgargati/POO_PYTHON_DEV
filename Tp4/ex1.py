from abc import ABC, abstractmethod
class Media:
    def __init__(self,t):
        self.__titre=t
        self._e = False

    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self,t):
        self.__titre = t

    def emprunte(self):
        return self._e
    
    def eStatus(self):
        if self._e == True:
            return "est pas displonible a le moment"
        elif self._e ==False:
            return "est disponible a le moment"
        
    def __str__(self):
        return f" le titre est {self.titre}"
    
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

    @property
    def auteur(self):
        return self.__auteur
    
    @auteur.setter
    def auteur(self,a):
        self.__auteur = a

    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self,g):
        self.__genre = g

    def __str__(self):
        return super().__str__()+ f" auteur : {self.auteur} le genre : {self.genre} et {self.eStatus()} "
    
    def Emprunter(self):
        if self.emprunte()==False:
            self._e = True
            print(f"le livre {self.titre}, par l'auteur: {self.auteur} a ete emprunte avec succes")

    def Retourner(self):
        if self.emprunte()==True:
            self._e = False
            print(F"le livre {self.titre}, par l'auteur: {self.auteur} a ete restitue avec success")
    

class CD(Media):
    def __init__(self, t, a, d):
        super().__init__(t)
        self.__artiste = a
        self.__duree = d

    @property
    def artiste(self):
        return self.__artiste

    @artiste.setter
    def artiste(self,a):
        self.__artiste = a

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self,d):
        self.__duree = d

    def __str__(self):
        return super().__str__() +f" artiste :{ self.artiste} la duree est {self.duree} min et {self.eStatus()} "
 
    def Emprunter(self):
        if self.emprunte()==False:
            self._e = True
            print(f"le CD {self.titre}, par l'artiste: {self.artiste} a ete emprunte avec succes")

    def Retourner(self):
        if self.emprunte()==True:
            self._e = False
            print(F"le CD {self.titre}, par l'artiste: {self.artiste} a ete restitue avec success")

CC=CD("cd1","artiste1",120)
print(CC)
CC.Emprunter()
print(CC)