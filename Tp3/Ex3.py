import time
class Livre:
    def __init__(self, t, a, an):
        self.__titre=t
        self.__auteur=t
        self.__annee_publication=an
        self.__disponible=True

    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self,t):
        self.__titre=t

    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self,a):
        self.__auteur=a

    @property
    def annee_publication(self):
        return self.__annee_publication
    @annee_publication.setter
    def annee_publication(self,an):
        self.__annee_publication=an

    def emprunter(self):
        if self.__disponible==True:
            self.__disponible=False
            print("le livre est emprunte avec succes")
        else:
            print("no disponible")

    def rendre(self):
        if self.__disponible==False:
            self.__disponible=True
            print("le livre est rendu avec succes")
          
    def check_disponibilite(self):
        if self.__disponible==True:
            return f"oui disponible"
        else:
            return f"No disponible"
        
    def __str__(self):
        return f"Le titre de livre est : {self.__titre} \n L'auteur est {self.__auteur} \n annee de publication {self.__annee_publication} \n la disponibilite : {self.check_disponibilite()}"

class LivreNumerique(Livre):
    def __init__(self, t, a, an, f):
        super().__init__(t, a, an)
        self.__format=f

    @property
    def format(self):
        return self.__format
    
    @format.setter
    def format(self,f):
        self.__format = f


    def telecharger(self):
            print("telechargement en cours...")
            time.sleep(3)
            print("telechargement termine!")

    def convertir_format(self, toFormat):
        print(f"Conversion de {self.titre} de {self.__format} vers {toFormat} en cours...")
        time.sleep(3)
        self.__format = toFormat
        print(f"convertee correctement au format {toFormat}")

    def __str__(self):
        return super().__str__()+ f" \n et il a le format {self.format}"
    
L1=LivreNumerique("simo","ahmed",2004,"pdf")
print(L1)
L1.telecharger()
L1.convertir_format("doc")
print(L1)
print(L1.check_disponibilite())
    
