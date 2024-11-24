class Personne :
    def __init__(self, n, a):
        self.__nom = n
        self.__age = a
    
    def get_nom(self):
        return self.__nom
    def set_nom(self, n):
        self.__nom = n
    
    def get_age(self):
        return self.__age
    def set_age(self, a):
        if a>0:
            self.__age=a

    def afficher_infos(self):
        print(f"mon nom est {self.__nom}, et mon age est {self.__age}", end = " ")


class Etudiant(Personne):
    def __init__(self, n, a, f):
        super().__init__(n, a)
        self.__filiere = f
    
    def get_filiere(self):
        return self.__filiere
    def set_filiere(self, f):
        self.__filiere = f
    
    def afficher_infos(self):
        super().afficher_infos()
        print(f" et ma filiere est {self.__filiere}")


class Employe(Personne):
    def __init__(self, n, a, p):
        super().__init__(n, a)
        self.__poste = p

    def get_poste(self):
        return self.__poste
    def set_filiere(self, p):
        self.__poste = p
    def afficher_infos(self):
        super().afficher_infos()
        print(f" et mon poste est {self.__poste}")
    
Pers1 = Personne("Mohamed", 20)
print("")
Pers1.afficher_infos()
print("")

Etud1 = Etudiant("Hamid", 30, "Development Digitale")
Etud1.afficher_infos()

Emp1 = Employe("Said", 31, "Directeur")
Emp1.afficher_infos()
    