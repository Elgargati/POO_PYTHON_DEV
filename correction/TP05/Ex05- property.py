class InvalideCINException(Exception):
        pass
class InvalideGradeException(Exception):
        pass

class Employe:
    def __init__(self, cin, n, p, g):
        self.__nom = n
        self.__prenom = p
        self.cin = cin
        self.grade = g
    @property
    def cin(self):
        return self.__cin
    @cin.setter
    def cin(self, cin):
        if len(cin)==7 and cin[0].isalpha()==True and cin[1:7].isdigit()==True:
            self.__cin = cin
        else:
            # raise ValueError (f" le CIN de {self.__nom} est invalide") 
            raise InvalideCINException (f" le CIN de {self.__nom} est invalide") 
             
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, n):
        self.__nom = n
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, p):
            self.__prenom = p
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, g):
            grades_Valides = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
            if g in grades_Valides:
                self.__grade = g
            else:
                raise InvalideGradeException (f"Le Grade de l'employe {self.__nom} est invalide") 
                # raise Exception (f"Le Grade de l'employe {self.__nom} est invalide") 

    def __str__(self):
        return f"L'employe : {self.__nom}, {self.__prenom} qui a la CIN : {self.__cin} a le grade : {self.__grade}"




# E1 = Employe("E188887", "Nom1", "prenom1", 'C')
# print(E1)
# E2 = Employe("G14d6659", "Nom2", "prenom2", 'V')
# print(E2)
# E1 = Employe("E188887", "Nom3", "prenom3", 'B')
# print(E1)



# raise InvalideGradeException ("invalide grade")
    
E1 = Employe("E141214", "nom1", "prenom1", "a")
print(E1) 

