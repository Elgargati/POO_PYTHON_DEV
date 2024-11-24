class Etudiant:
    def __init__(self, n, a, M):
        self.__nom = n
        self.set_age(a)
        self.set_moyenne(M)
    def get_nom(self):
        return self.__nom
    def set_nom(self, n):
        self.nom = n

    def get_age(self):
        return self.__age
    
    def set_age(self, a):
        if isinstance(a, int) and a <=26 and a>=18:
            self.__age = a
        else :
            raise Exception ("L'age doit etre entre 18 et 26")
    
    def get_moyenne(self):
        return self.__moyenne
    def set_moyenne(self, M):
        if isinstance(M, int) and M>= 0 and M<=20:
            self.__moyenne = M
        else :
            raise Exception ("La Note doit etre 0 et 20")

    def __str__(self):
        return f"L'etudiant : {self.__nom} qui a {self.__age} a la moyenne : {self.__moyenne}"
    
E1 = Etudiant("Saidi", 19, 20)
print(E1)

E2 = Etudiant("Ouadie", 26, 0)
print(E2)
