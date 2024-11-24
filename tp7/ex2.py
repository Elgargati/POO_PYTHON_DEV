class Client:
    def __init__(self,c,n,p,a,t):
        self.__cin=c
        self.__nom=n
        self.__prenom=p
        self.__adresse=a
        self.__telephone=t
    
    @property
    def cin(self):
        return self.__cin
    @cin.setter
    def cin(self,c):
        self.__cin=c

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,p):
        self.__prenom=p

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self,a):
        self.__adresse=a

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self,t):
        self.__telephone=t
    
    def __str__(self):
        return f" Le cin :-- {self.cin} -- Le Nom et prenom  :-- {self.nom , self.prenom}--  Adresse-- {self.adresse}-- Le Telephone -- {self.telephone}-- "
    

class Compte:
    __count=0
    def __init__(self,s,t,c):
        Compte.__count+=1
        self.__numero=Compte.__count
        self.__solde=s
        self.__type=t
        self.__client=c
    @property
    def numero(self):
        return self.__numero
    @property
    def solde(self):
        return self.__solde
    
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,t):
        if t=='C' or t=='T':
            self.__type=t
        else:
            raise Exception("Type Invalid")
        
    @property
    def client(self):
        return self.__client
    @client.setter
    def client(self,c):
        self.__client=c
    
    def __str__(self):
        return f" Le numero de compte -- {self.numero} -- de client -- { self.client} -- le type -- {self.type} -- le solde -- {self.solde} "
    
class Banque:
    def __init__(self,n,s):
        self.__nomb=n
        self.__siege=s
        self.__liste_de_compte=[Compte(6000,"E",Client("ee12","nom1","prenom1","adresse1","0771440465")),Compte(1000,"C",Client("ee40","nom2","prenom2","adresse2","0983992")),Compte(6000,"E",Client("ew32","nom3","prenom3","adresse3","09839282"))]
    @property
    def nomb(self):
        return self.__nomb
    
    @nomb.setter
    def nomb(self,n):
        self.__nomb=n

    @property 
    def siege(self):
        return self.__siege
    @siege.setter
    def siege(self,s):
        self.__siege=s

    @property
    def liste_de_compte(self):
        return self.__liste_de_compte
    
    def __str__(self):
        C=""
        for i in self.liste_de_compte:
            C+= str(i) + "\n"
        return f" Nom de banque -- {self.nomb} -- le siege -- {self.siege} -- \n Liste de compte : \n {C}"
    
    def RechercherCompte(self,n):
        c=None
        for i in self.liste_de_compte:
            if n==i.numero:
                c=i
                break
        return c 
    
    def AjouterCompte(self,compte):
        b=False
        self.liste_de_compte.append(compte)
        if compte in self.liste_de_compte:
            b=True
        return b
    def SupprimerCompte(self,num):
        a=self.RechercherCompte(num)
        if a!=None:
            if a.solde==0:
                self.liste_de_compte.remove(a)
                return True
            else:
                return False
    def ModifierTelClient(self,num,tel):
        a=self.RechercherCompte(num)
        if a!=None:
            a.client.telephone=tel
            return True
        else:
            return False
        
    def ReteurnCompte(self):
        c=""
        for i in self.liste_de_compte:
            c+=str(i) +"\n"
        return c
    
    def ReteurnCompteE(self):
        c=[]
        for i in self.liste_de_compte:
            if i.type=="E":
                c.append(i)
        return c
    
    def ReteurnCompteC(self,min,max):
        c=""
        for i in self.liste_de_compte:
            if i.solde<=max and i.solde>=min:
                c+=str(i) +"\n"
        return c

    def returnCompteCin(self,cin):
        c=[]
        for i in self.liste_de_compte:
            if i.client.cin==cin:
                c.append(i)
        return c

    def CompteMax(self):
        M=[]
        for i in self.liste_de_compte:
            M.append(i.solde)
        c=""
        for i in self.liste_de_compte:
            if i.solde==max(M) :
                c+=str(i)
        return c



b=Banque("BP","CASA")


while True:
    while True:
        print("""
 	1-Ajouter un compte à la banque.
 	2-Supprimer un compte à partir de son code (si son solde est égal à zéro).
 	3-Modifier le numéro de téléphone du client d'un compte donné.
 	4-Rechercher un compte à partir de son Numéro.
 	5-Afficher toutes les informations de la banque.
 	6-Afficher tous les comptes de la banque
 	7-Afficher tous les comptes d'épargnes de la banque
 	8-Afficher les comptes courants qui ont un solde entre deux valeurs données.
 	9-Rechercher le(s) compte(s) à partir de son Client (CIN).
 	10-Afficher la somme de tous les comptes d'épargne de la banque.
 	11-Afficher la somme de tous les comptes d'un client donné (CIN) 
    12-Afficher les comptes ayant le solde maximal.
    13-Quitter
""")
        a=int(input("donner un operation"))
        if (a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 or a==8 or a==9 or a==10 or a==11 or a==12 or a==13):
            break
        else:
            print("doit entre 1 a 13 ")
    if a==1:
        s=float(input("Donner le solde"))
        t=input("Donner le type du compte (E/C) : ")
        cin=input("donner la cin")
        n=input("donner le nom")
        p=input("donner le prenom")
        a=input("donner adresse")
        t=input("donner le telephone")
        if b.AjouterCompte(Compte(s,t,Client(cin,n,p,a,t)))==True:
            print("votre compte ajouter avec succee")
        else:
            print("Erreur !!")
    elif a==2:
        code=input("donner le code de compte")
        if b.SupprimerCompte(code)==True:
            print("le compte a supprimer avec succee ")
        else:
            print("Erreur !!")
    elif a==3:
        num=input("donner le numero de compte")
        tel=input("donner le numero de telephone nouveau")
        if b.ModifierTelClient(num,tel)==True:
            print("le telephone a modifier avec succee")
        else:
            print("Errour")
    elif a==4:
        num=int(input("donner le num de compte"))
        if b.RechercherCompte(num)==None:
            print("aucun compte")
        else:
            print(b.RechercherCompte(num))

    elif a==5:
        print(b)

    elif a==6:
      print(b.ReteurnCompte())

    elif a==7:
        print(b.ReteurnCompteE())

    elif a==8:
        min=float(input("Donner la 1er valeur : "))
        max=float(input("Donner la 2eme valeur : "))
        print(b.ReteurnCompteC(min,max))

    elif a==9:
        cin=input("donner le cin")
        c=b.returnCompteCin(cin)
        if a=="":
            print("aucun cin")
        else:
            print(b.returnCompteCin(cin))
    
    elif a==10:
        d=b.ReteurnCompteE()
        s=0
        for i in d:
           s+=i.solde
        print(s) 

    elif a==11:
        cin=input("donner le cin")
        L=b.returnCompteCin(cin)
        s=0
        for i in L:
            s+= i.solde
        print(s)

    elif a==12:
        print(b.CompteMax())    
    elif a==13:
        break



    
 
    v=input("voulez-vous continue O/N")
    if v.lower()!='o':
        break


