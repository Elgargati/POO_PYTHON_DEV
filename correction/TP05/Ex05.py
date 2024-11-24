class Employe:
    def __init__(self, cin, n, p, g):
        self.__nom = n
        self.__prenom = p
        self.set_cin(cin)
        self.set_grade(g)
    def get_cin(self):
        return self.__cin
    def set_cin(self, cin):
        if len(cin)==7 and cin[0].isalpha() and cin[1:6].isdigit():
            self.__cin = cin
        else:
            raise InvalideCINException (f" le CIN de {self.__nom} est invalide") 
            # raise Exception (f" le CIN de {self.__nom} est invalide") 
             

    def get_nom(self):
        return self.__nom
    def set_nom(self, n):
        self.__nom = n

    def get_prenom(self):
        return self.__prenom
    def set_age(self, p):
            self.__prenom = p

    def get_grade(self):
        return self.__grade
    def set_grade(self, g):
            grades_Valides = ['A', 'B', 'C', 'D']
            if g in grades_Valides:
                self.__grade = g
            else:
                raise ValueError (f"Le Grade de l'employe {self.__nom} est invalide") 
                # raise Exception (f"Le Grade de l'employe {self.__nom} est invalide") 

    def __str__(self):
        return f"L'employe : {self.__nom}, {self.__prenom} qui a la CIN : {self.__cin} a le grade : {self.__grade}"
E1 = Employe("E188887", "Nom1", "prenom1", 'C')
print(E1)
E2 = Employe("G1466553", "Nom1", "prenom1", 'B')
print(E2)
E1 = Employe("E188887", "Nom1", "prenom1", 'D')
print(E1)


class InvalideCINException(Exception):
    pass