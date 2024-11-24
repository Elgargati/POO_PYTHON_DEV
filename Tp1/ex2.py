class Appelee_Personne:
    def __init__(self,nom='sans',age=0,ville='sans'):
        self.nom= nom
        self.age= age 
        self.ville = ville
    def afficher_infos(self):
        print(self.nom)
        print(self.age)
        print(self.ville)

Personne2=Appelee_Personne('simo',18,"marrakech")
Personne2.afficher_infos()

Personne1=Appelee_Personne()
Personne1.afficher_infos()

