class Client:
    def __init__(self, c='inkonnu', n='sans', p='sans', t='*********'):
        self.__Cin = c
        self.__Nom = n
        self.__Prenom = p
        self.__Tel = t

    
    def afficher(self):
        print(f"{self.Nom} {self.__Prenom} / CIN : {self.__Cin} / N°TEL : {self.__Tel}")

    @property
    def Cin(self):
        return self.__Cin
    @Cin.setter
    def Cin(self,c):
        self.__Cin = c

    @property
    def Nom(self):
        return self.__Nom
    @Nom.setter
    def Nom(self,n):
        self.__Nom = n

    @property
    def Prenom(self):
        return self.__Prenom
    @Prenom.setter
    def Prenom(self,p):
        self.__Prenom = p

    @property
    def Tel(self):
        return self.__Tel
    @Tel.setter
    def Tel(self,t):
        self.__Tel = t

class CompteBancaire:
    __count=0
    def __init__(self, s):
        self.__solde = s
        CompteBancaire.__count += 1
        self.__code= CompteBancaire.__count

    @property
    def solde(self):
        return self.__solde
    
    @property
    def code(self):
        return self.__code
    
    def Crediter(self,mt):
        if mt>0:
            self.__solde +=mt

    def Debiter(self,mt):
            self.__solde -=mt
   
    def __str__(self):
        return f", le numero de compte {self.__code}:  , le solde : {self.__solde} "

class CompteEpargne(CompteBancaire):
    __taux_interet= None
    def __init__(self, s=0):
        super().__init__(s)


    def calculer_interets(self):
        interet = self.__solde * CompteEpargne.__taux_interet
        self.Crediter(interet)

    @staticmethod
    def taux_interet():
        return CompteEpargne.__taux_interet
    
    @staticmethod
    def definir_taux_interet(t):
        if isinstance(t,float) and t<=1 and t>0:
            CompteEpargne.__taux_interet= t
        else:
            print("le taux d'interet est invalide")

    def __str__(self):
        return super().__str__()+ f"Le taux d'interet est {CompteEpargne.__taux_interet}"
    
class ComptePayant(CompteBancaire):
    def __init__(self, s):
        super().__init__(s)

    def Debiter(self, somme):
        super().Debiter(somme)
        super().Debiter(1)
        # super().Debiter(somme + 1)

    def Crediter(self, somme):
        super().Crediter(somme)
        super().Debiter(1)
    #     super().Crediter(somme - 1)
        
    
    def __str__(self):
        return super().__str__()

    



    
        


    

    
