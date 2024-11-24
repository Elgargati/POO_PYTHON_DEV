class livre:
    def __init__(self,t,a): 
        self.titre=t
        self.auteur=a
    def afficher_details(self):
        print(f"le titre : {self.titre} \n l'auteur est : {self.auteur}")

P1=livre("la boite","ahmed")
P2=livre("Game of thrones","Jhon")
P1.afficher_details()
P2.afficher_details()

        