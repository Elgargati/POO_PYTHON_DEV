class Employe:
    def __init__(self,c,n,p,g):
        self.__cin=c
        self.__nom=n
        self.prenom=p
        self.grade=g

    @property
    def cin(self):
        return self.__cin
    @cin.setter
    def cin(self,c):
        if len(c)==7 and c[0].isalpha() and c[1,6].isdigit():
            print("sss")
            self.__cin=c

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,p):
        self.__prenom=p

    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def  grade(self,g):
        grade=['A','B','C','D']
        if (g in grade ):
            self.__grade=g
        else:
            raise Exception ("le grade est invalide")
        
    def __str__(self):
        return f"le cin est {self.__cin} le nom est {self.__nom} le prenom est {self.__prenom} le grade est {self.__grade} "

s=Employe()






