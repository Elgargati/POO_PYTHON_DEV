import time
class Livre :
    def __init__(self, ti, au, an,di):
        self.__titre = ti
        self.__auteur = au
        self.__annee = an
        self.__disponible = di
    
    def get_titre(self):
        return self.__titre
    def set_titre(self, t):
        self.__titre = t

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, au):
        self.__auteur = au
    
    def get_annee(self):
        return self.__annee
    def set_anne(self, an):
        self.__annee = an
    
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self, di):
        self.__disponible = di
    
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("le livre est emprunte avec succes")
    
    def rendre(self):
        if self.__disponible == False:
           self.__disponible = True
           print("le livre est rendu avec succes")

    def CheckDispo(self):
        if self.__disponible:
            return "disponible a le moment"
        else :
            return "pas disponible a le moment"
        

    def __str__(self):
        return f"le livre a le titre: {self.__titre}, le nom d'auteur: {self.__auteur}, l'annee de publication: {self.__annee}, et il est {self.CheckDispo()}"
    

class LivreNumerique(Livre):
    def __init__(self, ti, au, an, di, fo):
        super().__init__(ti, au, an, di)
        self.__format = fo
    

    def get_format(self):
        return self.__format
    def set_format(self, fo):
        self.__format = fo

    
    def Telecharger(self):
        print("telechargement en cours...")
        time.sleep(3)
        print("telechargement termine!")

    def convertir_format(self, toFormat):
        print(f"Conversion de {self.get_titre()} de {self.__format} vers {toFormat} en cours...")
        time.sleep(3)
        self.__format = toFormat
        print(f"convertee correctement au format {toFormat}")

    def __str__(self):

        return  super().__str__() + f", et il a le format {self.__format}"



# Livre1 = Livre("titre1", "auteur1", 2000, True)
# print(Livre1)
# Livre1.emprunter()
# print(Livre1)
# Livre1.rendre()
# print(Livre1)

Livre2 = LivreNumerique("titre02", "auteur02", 2003, True, "PDF")
print(Livre2)
Livre2.Telecharger()
print(Livre2)
Livre2.convertir_format("Docx")
print(Livre2)






# L1 = Livre("Titre01", "Auteur01", "2002", True)
# print(L1)

# L2 = LivreNumerique("Titre02", "Auteur02", "2003", True, "PDF")
# # print(L2.__str__())
# L2.Telecharger()

# L2.convertir_format("PDF")
# print(L2)