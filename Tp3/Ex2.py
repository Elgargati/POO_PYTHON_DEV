class Employe:
    def __init__(self,n,s):
        self.__nom = n
        self.__salaire=s

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n

    @property
    def salaire(self):
        return self.__salaire
    @salaire.setter
    def salaire(self,s):
        self.__salaire=s

    def calculer_salaire_annuel(self):
        c=self.__salaire*12
        return c
    def __str__(self):
        return f"Nom de l'employe : {self.nom} est le salaire est {self.salaire}"
    
class Dericteur(Employe):
    def __init__(self, n, s, p, a):
        super().__init__(n, s)
        self.__prime=p
        self.action=a

    
    @property
    def prime(self):
        return self.__prime
    @prime.setter
    def prime(self,p):
        self.__prime=p

    
    @property
    def action(self):
        return self.__action
    @action.setter
    def action(self,a):
        self.__action=a

    def calculer_salaire_annuel(self):
        return super().calculer_salaire_annuel()+ self.prime
    
    def __str__(self):
        return super().__str__()+f" le prime est : {self.prime} est action {self.action} est le salaire annuel {self.calculer_salaire_annuel()}"
    
d1=Dericteur('simo',10000,3000,"12")
print(d1)


