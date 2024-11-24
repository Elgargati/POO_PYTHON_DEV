class Livre:
    def __init__(self,t,a,p):
        self.__titre=t
        self.__auteur=a
        self.set_prix(p)
    def afficher_details(self):
        print(f"le titre est {self.__titre} / auteur est {self.__auteur} / prix est {self.__prix}")

    def get_titre(self):
        return self.__titre
    def set_titre(self,t):
         self.__titre = t
    
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self,a):
        self.__auteur=a

    def get_prix(self):
        return self.__prix
    def set_prix(self,p):
        if (p>0):
            self.__prix=p
        else:
            print("Valeur invalide")
P1=Livre("simo","kacm",100)
P2=Livre("Mehdi","Marrakech",300)
P3=Livre("Mouad","Kechmarra",500)
P1.afficher_details()
P2.afficher_details()
P3.afficher_details()
P1.set_prix(279)
print(P1.get_prix())    
P1.set_auteur("thrones")
print(P1.get_auteur())
P1.afficher_details()

