class Persone:
    def __init__(self,n,a):
        self.__nom=n
        self.age =a

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom = n

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,a):
        if (a>0):
            self.__age = a
        else:
            print("doit etre age positive")

    def afficher_info(self):
        return(f"le nom est {self.__nom} le age est {self.__age} ")

class Etudiant(Persone):
    def __init__(self, n, a,f ):
        super().__init__(n, a)
        self.__filiere =f

    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filier(self,f):
        self.__filiere = f
    def afficher_info(self):
         print(super().afficher_info() + f"la filiere est {self.__filiere}")

class Employe(Persone):
    def __init__(self, n, a, p):
        super().__init__(n, a)
        self.__post = p

    @property
    def post(self):
        return self.__post
    @post.setter
    def post(self,p):
        self.__post = p

    def afficher_info(self):
        
        print( super().afficher_info()+f"le post {self.__post}")

L=Employe("SIMO ", 20,"cadre")
L.afficher_info()
    