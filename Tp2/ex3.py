class CompteBancaire:

    __taux_interet = 0.02

    def __init__(self, titulaire, solde):
        self.__titulaire = titulaire
        self.__solde = solde

    @staticmethod
    def get_taux_interet():
        return CompteBancaire.__taux_interet

    @staticmethod
    def definir_taux_interet(nouveau_taux):
        CompteBancaire.__taux_interet = nouveau_taux

    @property
    def titulaire(self):
        return self.__titulaire

    @titulaire.setter
    def titulaire(self, nouveau_titulaire):
        self.__titulaire = nouveau_titulaire

    @property
    def solde(self):
        return self.__solde
# add a check for type instance float

    @solde.setter
    def solde(self, nouveau_solde):
        self.__solde = nouveau_solde

    def calculer_interets(self):
        interets = self.solde * CompteBancaire.__taux_interet
        print(f"Intérêts pour le compte de {self.titulaire}: {interets}")




compte1 = CompteBancaire("Hamid", 5000)
compte2 = CompteBancaire("simo", 10000)

compte1.calculer_interets()

CompteBancaire.definir_taux_interet(0.04)



compte2.solde = 12000
compte2.calculer_interets()
print(CompteBancaire.get_taux_interet())
