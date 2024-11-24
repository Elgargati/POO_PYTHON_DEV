class Etudiant:
    def __init__(self,n,a,m):
        self.__nom=n
        self.set_age(a)
        self.set_moyenne(m)
    def get_nom(self):
        return self.__nom
    def set_nom(self,n):
        self.__nom = n

    def get_age(self):
        return self.__age
    def set_age(self,a):
        if (isinstance(a,int) and a>=18 and a<=26):
            self.__age = a
        else:
            raise Exception("age not valid")
            

    def get_moyenne(self):
        return self.__moyenne
    def set_moyenne(self,m):
        if (isinstance(m,float) and m>=0 and m<=20 ):
            self.__moyenne = m
        else:
            raise Exception("la entre 0 et 20")
    def __str__(self):
        return f"le nom est {self.__nom} le age est {self.__age} la moyenne est {self.__moyenne}"
        
p=Etudiant('simo',10,2)
print(p)
