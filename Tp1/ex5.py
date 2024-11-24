class CompteBancaire:
    def __init__(self,tit,sd):
        self.titulaire=tit
        self.solde=sd
    def afficher_info(self):
        print(f"Titulaire :{self.titulaire} le solde du compte bancaire: {self.solde}Dh")
    def depose(self,mt):
        self.solde+=mt
        print(f" sa depose {mt} Dh  . nouveau solde : {self.solde} Dh")
    def retirer (self,mt):
        if (self.solde>=mt):
            self.solde-=mt
        else:
            print("montant not valide")
tit=input("donner le nom :")
sd=float(input("donner le solde"))
P1=CompteBancaire(tit,sd)
P1.afficher_info()
mt=float(input("donner le montant se depose :"))
P1.depose(mt)
mt=float(input("donner le montant se retirer :"))
P1.retirer(mt)
P1.afficher_info()


# P2=CompteBancaire('cdddd',10000)
# P2.afficher_info()
# P2.depose(2000)
# P2.retirer(3992)
# P2.afficher_info()

