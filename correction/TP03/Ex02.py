class Employe :
    def __init__(self, n, s):
        self.__nom = n
        self.__salaire = s
    
    def get_nom(self):
        return self.__nom
    def set_nom(self, n):
        self.__nom = n
    
    def get_salaire(self):
        return self.__salaire
    def set_salaire(self, s):
        if s>0:
            self.__salaire=s


    def Calculer_Salaire_annuel(self):
        annuel = self.__salaire * 12
        return annuel
    
    def __str__(self):
        return f"je m'appele {self.__nom}, mon salaire est {self.__salaire}"

class Directeur(Employe):
    def __init__(self, n, s, p, a):
        super().__init__(n, s)
        self.__prime = p
        self.__actions = a
    
    def get_prime(self):
        return self.__prime
    def set_prime(self, p):
        self.__prime = p
    
    def get_action(self):
        return self.__actions
    def set_actions(self, a):
            self.__actions=a
    
    def Calculer_Salaire_annuel(self):
        return super().Calculer_Salaire_annuel() + self.__prime 
    
    def __str__(self):
        return super().__str__() + f" mon Prime est {self.__prime}, mon nombre d'action est {self.__actions}, et mon salaire annuel est {self.Calculer_Salaire_annuel()} "

    
D1 = Directeur("Said", 10000, 2000, 10)

print(D1)
D1.set_actions(400)
print(D1)


