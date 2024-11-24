class Client:
    def __init__(self, CIN, Nom, Prenom, Tel=None):
        self.__CIN = CIN
        self.__Nom = Nom
        self.__Prenom = Prenom
        self.__Tel = Tel

    def get_CIN(self):
        return self.__CIN
        
    def set_CIN(self, CIN):
        self.__CIN = CIN

    
    def get_Nom(self):
        return self.__Nom

    
    def set_Nom(self, Nom):
        self.__Nom = Nom

    def get_Prenom(self):
        return self.__Prenom

    
    def set_Prenom(self, Prenom):
        self.__Prenom = Prenom

    def get_Tel(self):
        return self.__Tel

    def set_Tel(self, Tel):
        self.__Tel = Tel

    def Afficher(self):
        print(f"CLIENT(CIN={self.__CIN}, Nom={self.__Nom}, Prenom={self.__Prenom}, Tel={self.__Tel})")

class Compte:
    __count = 0

    def __init__(self, proprietaire, so):
        self.__proprietaire = proprietaire
        self.__solde = so
        Compte.__count += 1
        self.__numero = Compte.__count 


    
    def get_proprietaire(self):
        return self.__proprietaire

    
    def set_proprietaire(self, proprietaire):
        self.__proprietaire = proprietaire

    def get_solde(self):
        return self.__solde

    
    def get_numeroCompte(self):
        return self.__numero

    def Crediter(self, somme):
        self.__solde += somme

    def Debiter(self, somme):
        if self.__solde >= somme:
            self.__solde -= somme
        else:
            print("Insufficient balance")

    def Afficher(self):
        print(f"COMPTE(Numero={self.__numero}, Solde={self.__solde}, Proprietaire={self.__proprietaire.get_Nom()}, {self.__proprietaire.get_Prenom()}, {self.__proprietaire.get_CIN()}, {self.__proprietaire.get_Tel()})")

    @staticmethod
    def getNombreComptes():
        return(Compte.__count)
    


client1 = Client("1234", "Ali", "Mohamed", "0606060606")
client1.Afficher()

compte1 = Compte(client1, 100)
compte1.Afficher()

compte1.Crediter(500)
compte1.Afficher()
compte1.Debiter(200)
compte1.Afficher()

compte2 = Compte(client1, 200)
compte2.Afficher()

print(Compte.getNombreComptes())












# compte = Compte(client)
# compte1 = Compte(client1)
# compte.Afficher()
# compte.Crediter(100)
# compte.Afficher()
# compte.Debiter(50)
# compte.Afficher() 
# compte1.Afficher() 

Compte.getNombreComptes()
