class Produit:

    total_produits_vendus = 0

    def __init__(self, nom, prix, quantite_stock):
        self.__nom = nom
        self.__prix = prix
        self.__quantite_stock = quantite_stock

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, N_Nom):
        self.__nom = N_Nom

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, N_Prix):
        self.__prix = N_Prix

    @property
    def quantite_stock(self):
        return self.__quantite_stock

    @quantite_stock.setter
    def quantite_stock(self, nouvelle_quantite):
        self.__quantite_stock = nouvelle_quantite
        

    def vendre_produit(self, quantite_vendue):

        if quantite_vendue <= self.quantite_stock:
            self.__quantite_stock -= quantite_vendue
            Produit.total_produits_vendus += quantite_vendue
            print(f"{quantite_vendue} unité(s) de {self.nom} vendue(s).")
        else:
            print(f"Quantité insuffisante en stock pour {self.nom}.")

    @staticmethod
    def afficher_total_vendus():
        print(f"Nombre total de produits vendus : {Produit.total_produits_vendus}")

# Exemples
produit1 = Produit("Livre", 15.99, 50)
produit2 = Produit("Ordinateur portable", 899.99, 10)

produit1.vendre_produit(9)
produit2.vendre_produit(1)

Produit.afficher_total_vendus()
