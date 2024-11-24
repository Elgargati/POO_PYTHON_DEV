class Client:
    def __init__(self, cin, nom, prenom, tel):
        self.CIN = cin
        self.Nom = nom
        self.Prenom = prenom
        self.Tel = tel

    def afficher(self):
        print(f"Client {self.Nom} {self.Prenom} (CIN: {self.CIN}, Tél: {self.Tel})")
    


class Compte:
    nombre_comptes = 0

    def __init__(self, proprietaire, solde=0):
        Compte.nombre_comptes += 1
        self.__numero_compte = Compte.nombre_comptes
        self.__solde = solde

    @property
    def numero_compte(self):
        return self.__numero_compte

    @property
    def solde(self):
        return self.__solde

    def crediter(self, montant):
        self.__solde += montant
        print(f"Compte {self.numero_compte} crédité de {montant} DH. Nouveau solde : {self.solde} DH.")

    def debiter(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
            print(f"Compte {self.numero_compte} débité de {montant} DH. Nouveau solde : {self.solde} DH.")
        else:
            print("Solde insuffisant.")

    def afficher_resume(self):
        print(f"Résumé du compte {self.numero_compte} - Solde : {self.solde} DH - Propriétaire : {self.proprietaire.Nom} {self.proprietaire.Prenom}")

    @staticmethod
    def afficher_nombre_comptes():
        print(f"Nombre total de comptes créés : {Compte.nombre_comptes}")


# Programme de test
client1 = Client("ABC123", "Doe", "John", "123456789")
client1.afficher()

compte1 = Compte(client1, 1000)
compte2 = Compte(client1, 500)

compte1.crediter(200)
compte1.debiter(50)

compte2.crediter(100)
compte2.debiter(700)

compte1.afficher_resume()
compte2.afficher_resume()

Compte.afficher_nombre_comptes()
