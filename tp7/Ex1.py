class Stagiare:
    def __init__(self,c,n,p):
        self.__CIN=c
        self.__nom=n
        self.__prenom=p
    
    @property
    def CIN(self):
        return self.__CIN
    
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

    def __str__(self):
        return f"CIN de stagiare est {self.CIN} le Nom : {self.nom} est prenom :{self.prenom}"

class Groupe:
    def __init__(self,ng,f):
        self.__nom_groupe=ng
        self.__filiere=f
        self.__liste_de_stagiare=[Stagiare("E112233","nom1","prenom1"),Stagiare("E17288","nom2","prenom2"),Stagiare("E92618","nom3","prenom3")]

    @property
    def nom_groupe(self):
        return self.__nom_groupe
    @nom_groupe.setter
    def nom_groupe(self,n):
        self.__nom_groupe=n

    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self,f):
        self.__filiere=f

    @property
    def liste_de_stagiare(self):
        return self.__liste_de_stagiare
    
    @liste_de_stagiare.setter
    def liste_de_stagiare(self,lis):
        if len(lis)>=25:
            self.__liste_de_stagiare =lis
        else:
            raise Exception(f"The provided list of trainees exceeds the limit 25.")
    
    def __str__(self):
        c=""
        for i in self.liste_de_stagiare:
            c+= str(i) +"\n"

        return f" Nom de groupe : {self.nom_groupe} filiere : {self.filiere} \n la liste des stagiare est :\n {c} "
    
    def rechercher_stagiaire(self,c):
        stagi=None
        for i in self.liste_de_stagiare:
            if i.CIN==c:
                stagi=i
                break
        return stagi
    
    def stagiaire_existe(self,c):
        if self.rechercher_stagiaire(c)==None:
            return False
        else:
            return True
        
    def stagiaire_existe_nom_prenom(self,nom,prenom):
        for i in self.liste_de_stagiare:
            if i.nom==nom and i.prenom==prenom:
                return True
        return False
    
    def ajouter_un_stagiare(self,Stagiare):
        if not self.stagiaire_existe(Stagiare.CIN) and len(self.liste_de_stagiare)<25:
            self.liste_de_stagiare.append(Stagiare)
            return True
        else:
            return False
    
    def afficher_liste_stagiaires(self):
        print("la liste des stagiaires dans le groupe")
        for i in self.liste_de_stagiare:
            print(i)

    def retirer_stagiaire_par_cne(self,cin):
        if self.stagiaire_existe(cin):
            self.liste_de_stagiare.remove(self.rechercher_stagiaire(cin))
            return True
        else:
            return False

print("cree le groupe")
G=input("donner le nom du groupe")
F=input("donner la filière")
dev103=Groupe(G,F)

while True:
    while True:
        print("""
        1- rechercher un stagiaire par son CNE dans le groupe.
        2- vérifie si un stagiaire spécifique (CNE) existe dans le groupe.
        3- vérifie si un stagiaire spécifique ( Nom et prénom) existe dans le groupe.
        4- ajouter un stagiaire au groupe 
        5- afficher la liste des stagiaires dans le groupe.
        6- retirer un stagiaire du groupe à partir de son CNE.
        7- quitter le programme
""")
        a=int(input("donner un operation"))
        if a==1 or a==2 or a==3 or a==4 or a==5 or a==6:
            break
        else:
            print("doit entre 1 a 7")
    
    if a==1:
        ci=input("donner la CNE de stagiaire")
        c=dev103.rechercher_stagiaire(ci)
        if c==None:
            print("CNE n'existe pas")
        else:
            print(c)
    elif a==2:
        ci=input("donner la CNE de stagiaire")
        c=dev103.stagiaire_existe(ci)
        if c==True:
            print("stagiaire existe dans le groupe")
        else:
            print("N'existe pas dans le groupe")
    elif a==3:
        nom=input("donner le nom")
        prenom=input("donner le prenom")
        if dev103.stagiaire_existe_nom_prenom(nom,prenom):
            print("stagiaire existe dans le groupe")
        else:
            print("N'existe pas dans le groupe")
    elif a==4:
            a = input("enter cne stagiare:")
            b = input("enter nom stagiare:")
            c = input("enter prenom stagiare:")
            p=Stagiare(a,b,c)
            if dev103.ajouter_un_stagiare(p):
                print("added")
            else:
                print("not added")
    elif a==5:
        dev103.afficher_liste_stagiaires()

    elif a==6:
            ci=input("donner la CNE de stagiaire")
            if dev103.retirer_stagiaire_par_cne(ci):
               print("le stagiaire retirer avec succee")
            else:
                print("cin n'existe pas ")

    elif a==7:
        print("vous quitter le groupe")
        break              


    v=input("voulez-vous continue O/N")
    if v.lower()!='o':
        break