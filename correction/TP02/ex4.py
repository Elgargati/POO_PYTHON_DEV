class Produit:
    __total_ventes = 0
    def __init__(self, nom='nom', pr=0, qu=0 ):
        self.__nom = nom
        self.__prix = pr
        self.__quantite_stock = qu
    def afficher(self):
        print("****", Produit.__total_ventes)
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix):
        self.__prix = prix
    @property
    def quantite_stock(self):
        return self.__quantite_stock
    @quantite_stock.setter
    def quantite_stock(self, quantite):
        self.__quantite_stock = quantite
    @staticmethod
    def get_total():
        return Produit.__total_ventes


    def vendre(self, quantite):
        if quantite <= self.__quantite_stock and quantite>=0 :
            self.__quantite_stock -= quantite
            Produit.__total_ventes += 1
        else:
            print("error")
    def afficher_details(self):
        print(f'***{self.__nom}*** {self.__prix}****{self.__quantite_stock}')


print(Produit.get_total())
pro1 = Produit("s",12,300)
pro1.afficher_details()


pro1.vendre(40)
print(Produit.get_total())
pro1.afficher_details()


pro2 = Produit("saw",15,4300)
pro2.afficher_details()


pro2.vendre(230)
print(Produit.get_total())
pro2.afficher_details()