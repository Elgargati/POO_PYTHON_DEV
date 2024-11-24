class Vehicule:
    def __init__(self, marque, modele, annee):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, N_Modele):
        self.__marque = N_Modele

    @property
    def modele(self):
        return self.__modele

    @modele.setter
    def modele(self, N_Modele):
        self.__modele = N_Modele

    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, N_Modele):
        if N_Modele > 0:
            self.__annee = N_Modele
        else:
            print("L'année doit être positive.")

    def afficher_details(self):
        print(f"Véhicule: {self.marque} {self.modele}, Année: {self.annee}")




vehicule1 = Vehicule("BMW", "M5", 2022)
vehicule2 = Vehicule("Golf", "8 GTD", 2022)

vehicule1.afficher_details()
vehicule2.afficher_details()

vehicule1.marque = "Amg A45s"
vehicule1.annee = 2022

vehicule1.afficher_details()
