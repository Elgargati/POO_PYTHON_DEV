class BaseProduit:
    def __init__(self, n, p):
        self.__nom=n
        self.prix=p

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,p):
        if p>=0:
            self.__prix=p

    def __str__(self):
        return f"Le nom : {self.nom} \n Le prix : {self.prix}"

    def calculer_prix_final(self):
        return self.__prix
    
class Produit_electronique(BaseProduit):
    def __init__(self, n, p, ma, ga):
        super().__init__(n, p)
        self.__marque=ma
        self.__garantie=ga

    @property
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self,ma):
        self.__marque=ma

    @property
    def garantie(self):
        return self.__garantie
    @garantie.setter
    def garantie(self,ga):
        self.__garantie=ga

    def prolonger_garantie(self,pg):
        self.__garantie+=pg
    def __str__(self):
        return super().__str__()+f"\n la marque est {self.marque} \n la garantie est {self.garantie} ans"
    
class ProduitEnPromotion(BaseProduit):
    def __init__(self, n, p, pd):
        super().__init__(n, p)
        self.__pourcentage_red = pd

    @property
    def pourcentage_red(self):
        return self.__pourcentage_red
    @pourcentage_red.setter
    def pourcentage_red(self,pd):
        self.__pourcentage_red = pd

    def calculer_reduction(self):
        p = self.prix * (self.pourcentage_red /100)
        return p
    def calculer_prix_final(self):
        return super().calculer_prix_final() - self.calculer_reduction()
    def __str__(self):
        return super().__str__()+ f"  et le pourcentage de reduction : {self.pourcentage_red }"
    
k1=ProduitEnPromotion("phone a3",2500,10)
print(k1)
print(k1.calculer_reduction())
print(k1.calculer_prix_final())




    

