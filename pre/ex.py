# class Personne:
#     __pays='maroc'
#     def __init__(self,n,p,a):
#         self.__nom=n
#         self.__prenom=p
#         self.__age=a
#     @staticmethod
#     def getpays():
#         return Personne.__pays
#     @staticmethod
#     def setpays(p):
#         Personne.__pays=p


#     @property
#     def nom(self):
#         return self.__nom
#     @nom.setter
#     def nom(self,n):
#         self.__nom=n
#     @property
#     def prenom(self):
#         return self.__prenom
#     @prenom.setter
#     def prenom(self,p):
#         self.__prenom=p
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,n):
#         self.__age=n

#     def  __str__(self):
#         return f"Je mappele {self.nom} ,{self.prenom} el mon age {self.age} le pays {Personne.__pays}"
    
# P1=Personne('simo','el gargati',20)
# print(P1)
# Personne.setpays('france')
# print(Personne.getpays())
# class Client:
#     def __init__(self, cin, nom, prenom, tel):
#         self.CIN = cin
#         self.Nom = nom
#         self.Prenom = prenom
#         self.Tel = tel

#     def afficher(self):
#         print(f"Client {self.Nom} {self.Prenom} (CIN: {self.CIN}, Tél: {self.Tel})")
    


# class Compte:
#     nombre_comptes = 0

#     def __init__(self, proprietaire, solde=0):
#         Compte.nombre_comptes += 1
#         self.__numero_compte = Compte.nombre_comptes
#         self.__solde = solde

#     @property
#     def numero_compte(self):
#         return self.__numero_compte

#     @property
#     def solde(self):
#         return self.__solde

#     def crediter(self, montant):
#         self.__solde += montant
#         print(f"Compte {self.numero_compte} crédité de {montant} DH. Nouveau solde : {self.solde} DH.")

#     def debiter(self, montant):
#         if montant <= self.__solde:
#             self.__solde -= montant
#             print(f"Compte {self.numero_compte} débité de {montant} DH. Nouveau solde : {self.solde} DH.")
#         else:
#             print("Solde insuffisant.")

#     def afficher_resume(self):
#         print(f"Résumé du compte {self.numero_compte} - Solde : {self.solde} DH - Propriétaire : {self.proprietaire.Nom} {self.proprietaire.Prenom}")

#     @staticmethod
#     def afficher_nombre_comptes():
#         print(f"Nombre total de comptes créés : {Compte.nombre_comptes}")


# # Programme de test
# client1 = Client("ABC123", "Doe", "John", "123456789")
# client1.afficher()

# compte1 = Compte(client1, 1000)
# compte3 = Compte(client1, 500)
# compte4 = Compte(client1, 500)
# compte5 = Compte(client1, 500)


# compte1.afficher_nombre_comptes()


# class Produit:
#     def __init__(self,n,p):
#         self.__nom=n
#         self.prix=p
#     @property
#     def nom(self):
#         return self.__nom
#     @nom.setter
#     def nom(self,n):
#         self._nom=n
#     @property
#     def prix(self):
#         return self.__prix
#     @prix.setter
#     def prix(self,p):
#         if p>0 :
#             self.__prix=p
#         else :
#             raise Exception("prix invalide")
            
#     def __str__(self):
#         return f"le nom : {self.__nom} , le prix : {self.__prix}"
    
#     def calcule_prix_final(self):
#         return self.__prix
    
# class ProduitElectronique(Produit):
#     def __init__(self, n, p,m,g):
#         super().__init__(n, p)
#         self.__marque=m
#         self.__garantie=p

#     @property
#     def marque(self):
#         return self.__marque
#     @marque.setter
#     def marque(self,m):
#         self._marque=m

#     @property
#     def garantie(self):
#         return self.__garantie
#     @garantie.setter
#     def garantie(self,g):
#         if g>0:
#             self.__garantie = g
#         else :
#             raise Exception("la duree est invalide")
    
#     def prolonger_garantie(self,duree):
#          self.__garantie+=duree
    
#     def __str__(self):
#         return super().__str__()+f"La Marque :{self.marque} la garantie : {self.garantie}"
    
# class ProduitEnPromotion(Produit):

#     def __init__(self, n, p, pr):
#         super().__init__(n, p)
#         self.__pourcentage_red=pr

#     @property
#     def pourcentage(self):
#         return self.__pourcentage_red
    
#     @pourcentage.setter
#     def pourcentage(self,pr):
#         self.__pourcentage_red=pr

#     def calcule_reduction(self):
#         return self.prix * (self.__pourcentage_red / 100)

    
#     def calcule_prix_final(self):
#         return self.prix - self.calcule_reduction()

    
#     def __str__(self):
#         return super().__str__() + f" et le pourcentage de reduction : {self.__pourcentage_red} "

# pp=ProduitEnPromotion('oppo',500,20)
# print(pp.calcule_reduction())
# print(pp.calcule_prix_final())

# produit=Produit('oppo',2000)
# print(produit)

# from abc import ABC,abstractmethod
# from datetime import date,datetime
# class Employe(ABC):
#     def __init__(self, m, n, p, D):
#         self.__Matricule = m
#         self.__Nom = n
#         self.__Prenom = p
#         self.__Date = D

#     @property
#     def Matricule(self):
#         return self.__Matricule
#     @Matricule.setter
#     def Matricule(self, m):
#         self.__Matricule = m

#     @property
#     def Nom(self):
#         return self.__Nom
#     @Nom.setter
#     def Nom(self, n):
#         self.__Nom = n

#     @property
#     def Prenom(self):
#         return self.__Prenom
#     @Prenom.setter
#     def Prenom(self, p):
#         self.__Prenom = p

#     @property
#     def Date(self):
#         return self.__Date
#     @Date.setter
#     def Date(self, d):
#         self.__Date =d

#     def __str__(self):
#         return f"matricule: {self.Matricule}, nom: {self.Nom}, prenom: {self.Matricule}, date de naissance: {self.Date}"
    
#     @abstractmethod
#     def GetSalaire(self):
#         pass

# class Ouvrier(Employe):
#     __smig=3000
#     def __init__(self, m, n, p, D,De):
#         super().__init__(m, n, p, D)
#         self.__date_entree=De

#     @property
#     def date_entree(self):
#         return self.__date_entree
#     @date_entree.setter
#     def date_entree(self, de):
#         self.__date_entree =de

#     def GetSalaire(self):
#         anciente = int((date.today() - self.__DateEntree).days /365.25)
#         S = Ouvrier.__Smig +(anciente * 100)
#         if S >Ouvrier.__Smig*2:
#             S = Ouvrier.__Smig *2
#         return S
#     def __str__(self):
#         return str(super().__str__() + f" Date d'entree: {self.__DateEntree} ")
    
# class Cadre(Employe):
#     def __init__(self, m, n, p, D, I):
#         super().__init__(m, n, p, D)
#         self.__indice = I
    
#     def get_indice(self):
#         return self.__indice
#     def set_indice(self, I):
#             self.__indice = I

#     def GetSalaire(self):
#         if self.__indice ==1: 
#             return round(130000/12)
#         elif self.__indice == 2:
#             return round(150000/12)
#         elif self.__indice == 3:
#             return round(170000/12)
#         elif self.__indice == 4:
#             return round(200000/12)
#         else : 
#             print("entrer une indice valide (entre 1 et 4)")
#     def __str__(self):
#         return str(super().__str__() + f" indice: {self.__indice} le salaire {self.GetSalaire()}")
    
# # C1 = Cadre(10, "Nom1", "Prenom1", 1997, 4)
# # print(C1)
# # print(C1.GetSalaire())

# class patron(Employe):
#     __chiffre_Affaire = None
#     def __init__(self, m, n, p, D, po):
#         super().__init__(m, n, p, D)
#         self.__pourcentage = po
    
#     def get_pourcentage(self):
#         return self.__pourcentage
#     def set_pourcentage(self, po):
#         self.__pourcentage = po

#     def GetSalaire(self):
#         salaire = (patron.__chiffre_Affaire *self.__pourcentage/100) /12
#         return salaire
#     def __str__(self):
#         return str(super().__str__() + f" pourcentage: {self.__pourcentage} ")
#     @staticmethod
#     def get_CA():
#         return patron.__chiffre_Affaire
#     @staticmethod
#     def set_CA(CA):
#         patron.__chiffre_Affaire= CA

# P1 = patron(3, "nom3", "Prenom3", date(1997, 12,12), 10)
# P1.set_CA(0.2)
# print(P1)
# print(P1.GetSalaire())





# from abc import ABC,abstractmethod
# class Ouvrage(ABC):
#     __count=0
#     def __init__(self,t):
#         Ouvrage.__count+=1
#         self.__code=Ouvrage.__count
#         self.__titre=t
#         self.__etat=True
#         self.__nombre_emprunt=0
    
#     @property
#     def code(self):
#         return self.__code

#     @property
#     def titre(self):
#         return self.__titre
#     @titre.setter
#     def titre(self,t):
#         self.__titre=t

#     @property
#     def etat(self):
#         return self.__etat
#     @etat.setter
#     def etat(self,e):
#         self.__etat=e
    
#     @property
#     def nombre_emprunt(self):
#         return self.__nombre_emprunt
#     @nombre_emprunt.setter
#     def nombre_emprunt(self,nb):
#         self.__nombre_emprunt=nb
    
#     def check_desponible(self):
#         if(self.__etat):
#             return"Oui Disponible"
#         else:
#             return"No Disponible "
    
#     @abstractmethod
#     def Emprunter(self):
#         pass
#     def Restitue(self):
#         pass

    
#     def __str__(self):
#         return f"Le code De Ouvrage {self.code} de  Titre de Ouvrage :{self.titre} il est :{self.check_desponible()} est le nombre d'emprunte : {self.nombre_emprunt}  "
    
# class Livre(Ouvrage):
#     def __init__(self, t,a,ed):
#         super().__init__(t)
#         self.__auteur=a
#         self.__editeur=ed

#     @property
#     def auteur(self):
#         return self.__auteur
#     @auteur.setter
#     def auteur(self,a):
#         self.__auteur=a

#     @property
#     def editeur(self):
#         return self.__editeur
#     @editeur.setter
#     def editeur(self,ed):
#         self.__editeur=ed

#     def Emprunter(self):
#         if(self.etat):
#             self.nombre_emprunt+=1
#             self.etat=False
#             print(f"le livre {self.titre} et auteur {self.auteur} a ete emprunte avec succes ")
#         else:
#             print(f"Le livre n'est pas disponible pour emprunter.")

#     def Restitue(self):
#         if(self.etat==False):
#             self.etat=True
#             print(f" livre {self.titre} et auteur {self.auteur} a ete Restitue avec succes ")
#         else:
#             print(f" livre deja restituer")
    
#     def __str__(self):
#         return "Livre : "+super().__str__()+f"auteur : {self.auteur} , l'editeur  : {self.editeur} \n ************************************** "

# class CD(Ouvrage):
#     def __init__(self, t,ar,nb_p):
#         super().__init__(t)
#         self.__artiste=ar
#         self.__Nombre_pistes=nb_p

#     @property
#     def artiste(self):
#         return self.__artiste
#     @artiste.setter
#     def artiste(self,a):
#         self.__artiste=a

#     @property
#     def Nombre_pistes(self):
#         return self.__Nombre_pistes
#     @Nombre_pistes.setter
#     def Nombre_pistes(self,nb_p):
#         self.__Nombre_pistes=nb_p

    
#     def Emprunter(self):
#         if(self.etat):
#             self.nombre_emprunt+=1
#             self.etat=False
#             print(f" CD {self.artiste} et le nomber de pistes {self.Nombre_pistes} a ete emprunte avec succes ")
#         else:
#             print(f" CD n'est pas disponible pour emprunter.")
    
#     def Restitue(self):
#         if(self.etat!=True):
#             self.etat=True
#             print(f"le CD {self.artiste} et le nomber de pistes {self.Nombre_pistes} a ete restituer avec succes")
#         else:
#             print(f"le CD deja restituer")

#     def __str__(self):
#         return f"CD "+ super().__str__()+f"l'artiste : {self.artiste} , Nombre de pistes est  : {self.Nombre_pistes} \n ******************************************* "

# L=[Livre("livre1","auteur1","editeur1"),Livre("livre3","auteur2","editeur2"),Livre("livre3","auteur3","editeur3"),CD("cd3","artiste3",34),CD("cd4","artiste4",44),Livre("livre4","auteur4","editeur4"),CD("cd1","artiste1",17),CD("cd2","artiste2",93)]

# def search(list,code):
#     c=None
#     for i in list:
#         if(i.code==code):
#             c=i
#             break
#     return c

# while True:
#     while True:
#         print("""
#                 1.  Afficher tous les ouvrages.
#                 2.	Afficher les ouvrages disponibles seulement.
#                 3.	Afficher tous les Livres.
#                 4.	Afficher tous les CDS.
#                 5.	Afficher les auteurs de tous les livres.
#                 6.	Afficher les artistes de tous les CDS.
#                 7.	Ajouter un ouvrage (Livre ou CD) à la bibliothèque.
#                 8.	Supprimer un ouvrage (par code)
#                 9.	Modifier le titre d'un ouvrage.
#                 10.	Rechercher un ouvrage par code. (Afficher également son type)
#                 11. Rechercher un Livre par code.
#                 12.	Rechercher un CD par code.
#                 13.	Rechercher un ouvrage par titre.
#                 14.	Rechercher un CD par artiste.
#                 15.	Rechercher un Livre par auteur.
#                 16.	Afficher tous les ouvrages classés par type.
#                 17.	Afficher les ouvrages triés par ordre croissant de nombres d'emprunt.
#                 18.	Emprunter un ouvrage par code.
#                 19.	Restituer un ouvrage par code.
#                 20.	Quitter.
# """)
#         a=int(input("donner un operation"))
#         if (a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 or a==8 or a==9 or a==10 or a==11 or a==12 or a==13 or a==14 or a==15 or a==16 or a==17 or a==18 or a==19 or a==20):
#             break
#         else:
#             print("choix invalid")
#     if a==1:
#         [print(i) for i in L] if L else print("la bibliotheque vide")
    
#     elif a==2:
#         k=[ i for i in L if i.etat]
#         [print(i) for i in L if i.etat] if k else print("la bibliotheque vide")
#     elif a==3:

#         liv=[i for i in L if (isinstance(i,Livre))]
#         [print(i) for i in liv] if liv else print("aucun livre dans la liste")
    
#     elif a==4:
#         cd=[i for i in L if (isinstance(i,CD))]
#         [print(i) for i in cd] if cd else print("aucun CD dans la liste")
    
#     elif a==5:
#         liv=[i for i in L if (isinstance(i,Livre))]
#         [print(i.auteur) for i in liv ]if liv else print("aucun livre dans la liste")

#     elif a==6:
#         cd=[i for i in L if (isinstance(i,CD))]
#         [print(i.artiste) for i in cd] if cd else print("aucun CD dans la liste")
    
#     elif a==7:
#         b=input("vous ajouter Livre ou CD ?")
#         if b.lower()=='livre':
#             titre=input("donner le titre de livre")
#             auteur=input("donner auteur de livre")
#             editeur=input("donner editeur de livre")
#             L.append(Livre(titre,auteur,editeur))
#             print("livre ajouter avec succee")
#         elif b.lower()=='cd':
#             titre=input("donner le titre de CD")
#             artiste=input("donner artiste de CD")
#             nb=int(input("donner le nombre pistes de CD"))
#             L.append(CD(titre,artiste,nb))
#             print("CD ajouter avec succee")
#         else:
#             print("invalide") 
#     elif a==8:
#         code=int(input("donner le code"))
#         D=search(L,code)
#         if(D==None):
#             print("code n'existe pas")
#         else:
#             L.remove(D)
#             print("ouvrage a supprimer")
    
#     elif a==9:
#         code=int(input("donner le code"))
#         D=search(L,code)
#         if(D==None):
#             print("code n'existe pas")
#         else:
#             D.titre = input("donner une nouvelle titre ")
#             print("titre modifie avec succes")

#     elif a==10:
#         code=int(input("donner le code"))
#         D=search(L,code)
#         if(isinstance(D,Livre)):
#             print("Le type de Ouvrage Livre")
#         elif (isinstance(D,CD)):
#             print("Le type de Ouvrage CD")

#     elif a==11:
#         code=int(input("donner le code"))
#         D=search(L,code) 
#         if(D==None):
#             print("code n'existe pas")
#         else:
#             if(isinstance(D,Livre)):
#                 print(D)
#             else:
#                 print("l'ouvrage est pas un Livre")

#     elif a==12:
#         code=int(input("donner le code"))
#         D=search(L,code) 
#         if(D==None):
#             print("code n'existe pas")
#         else:
#             if(isinstance(D,CD)):
#                 print(D)
#             else:
#                 print("l'ouvrage est pas un CD")

#     elif a==13:
#         tit=input('donner le titre de livre')
#         D=[]
#         for i in L:
#             if(i.titre.lower()==tit.lower()):
#                 D.append(i)
#         [print(i) for i in D] if D else print('aucun titre de set livre ')

#     elif a==14:
#         tit=input('donner le titre de CD')
#         D=[]
#         for i in L:
#             if(i.titre.lower()==tit.lower()):
#                 D.append(i)
#         [print(i) for i in D] if D else print('aucun titre de set livre ')

#     elif a==15:
#         aut=input("donner le nom de auteur")
#         D=[i for i in L if(isinstance(i,Livre)) if (i.auteur.lower()==aut.lower())]
#         # for i in L:
#         #     if (isinstance(i,Livre)):
#         #         if i.auteur.lower()==aut.lower():
#         #    
#         #          D.append(i)

#         [print(i) for i in D] if D else print("Aucun auteur")
#         # if D:
#         #     for i in D:
#         #         print(i)
#         # else:
#         #     print("Aucun auteur")

#     elif a==16:
#         [print(i) for i in L if (isinstance(i,Livre))]
#         [print(i) for i in L if (isinstance(i,CD))]
#         # for i in L:
#         #     if isinstance(i,Livre):
#         #         print(i)
#         # for i in L:
#         #     if isinstance(i,CD):
#         #         print(i)

#     elif a==17:
#         c = sorted(L, key=lambda x:x.nombre_emprunt,reverse=True)
#         [print(p) for p in c]

#     elif a==18:
#         c=int(input("donner un code de ouvrage"))
#         D=search(L,c)
#         if D==None:
#             print("le code n'existe pas")
#         else:
#             D.Emprunter()
#     elif a==19:
#         c=int(input("donner un code de ouvrage"))
#         D=search(L,c)
#         [print("le code n'existe pas")] if D==None else  D.Restitue()


           

#     if(a==20):
#         print("vous quitter le programme ")
#         break


#     v=input("voulez-vous continue O/N")
#     if v.lower()!='o':
#         print("vous quitter le programme ")
#         break



















# class Client:
#     def __init__(self,c,n,p,a,t):
#         self.__cin=c
#         self.__nom=n
#         self.__prenom=p
#         self.__adresse=a
#         self.__telephone=t
    
#     @property
#     def cin(self):
#         return self.__cin
#     @cin.setter
#     def cin(self,c):
#         self.__cin=c

#     @property
#     def nom(self):
#         return self.__nom
#     @nom.setter
#     def nom(self,n):
#         self.__nom=n

#     @property
#     def prenom(self):
#         return self.__prenom
#     @prenom.setter
#     def prenom(self,p):
#         self.__prenom=p

#     @property
#     def adresse(self):
#         return self.__adresse
#     @adresse.setter
#     def adresse(self,a):
#         self.__adresse=a

#     @property
#     def telephone(self):
#         return self.__telephone
#     @telephone.setter
#     def telephone(self,t):
#         self.__telephone=t
    
#     def __str__(self):
#         return f" Le cin :-- {self.cin} -- Le Nom et prenom  :-- {self.nom , self.prenom}--  Adresse-- {self.adresse}-- Le Telephone -- {self.telephone}-- "


# class Compte:
#     __count=0
#     def __init__(self,s,t,c):
#         Compte.__count+=1
#         self.__numero=Compte.__count
#         self.__solde=s
#         self.__type=t
#         self.__client=c
#     @property
#     def numero(self):
#         return self.__numero
#     @property
#     def solde(self):
#         return self.__solde
    
#     @property
#     def type(self):
#         return self.__type
#     @type.setter
#     def type(self,t):
#         if t=='C' or t=='T':
#             self.__type=t
#         else:
#             raise Exception("Type Invalid")
        
#     @property
#     def client(self):
#         return self.__client
#     @client.setter
#     def client(self,c):
#         self.__client=c
    
#     def __str__(self):
#         return f" Le numero de compte -- {self.numero} -- de client -- { self.client} -- le type -- {self.type} -- le solde -- {self.solde} "
    

# class Banque:
#     def __init__(self,n,s):
#         self.__nomb=n
#         self.__siege=s
#         self.__liste_de_compte=[Compte(6000,"E",Client("ee12","nom1","prenom1","adresse1","0771440465")),Compte(1000,"C",Client("ee40","nom2","prenom2","adresse2","0983992")),Compte(6000,"E",Client("ew32","nom3","prenom3","adresse3","09839282"))]
#     @property
#     def nomb(self):
#         return self.__nomb
    
#     @nomb.setter
#     def nomb(self,n):
#         self.__nomb=n

#     @property 
#     def siege(self):
#         return self.__siege
#     @siege.setter
#     def siege(self,s):
#         self.__siege=s

#     @property
#     def liste_de_compte(self):
#         return self.__liste_de_compte
    
#     def __str__(self):
#         C=""
#         for i in self.liste_de_compte:
#             C+= str(i) + "\n"
#         return f" Nom de banque -- {self.nomb} -- le siege -- {self.siege} -- \n Liste de compte : \n {C}"
    
#     def RechercherCompte(self,num):
#         C=None
#         for i in self.liste_de_compte:
#             if i.numero==num:
#                 C=i
#         return C
    
#     def AjouterCompte(self,compte):
#         b=False
#         if self.liste_de_compte.append(compte):
#             b=True
#         return b
    
#     def SupprimerCompte(self,num):
#         c=self.RechercherCompte(num)
#         if c!=None:
#             self.liste_de_compte.remove(c)
#             return True
#         else:
#             return False
        
#     def ModifierTelClient(self,num,tel):
#         c=self.RechercherCompte(num)
#         if c!=None:
#             c.numero=tel
#             return True
#         else:
#             return False
        
#     def ReteurnCompte(self):
#         C=""
#         for i in self.liste_de_compte:
#             C+=str(i)+"\n"
#         return C
    
#     def ReteurnCompteE(self):
#         C=""
#         for i in self.liste_de_compte:
#             if(i.type=='E'):
#                 C+=str(i)+"\n"
#         return C
    
#     def ReteurnCompteC(self,max,min):
#         C=""
#         for i in self.liste_de_compte:
#             if (i.solde>=min and i.solde<=max):
#                 C+=str(i)+"\n"
#         return C
    
#     def returnCompteCin(self,cin):
#         C=[]
#         for i in self.liste_de_compte:
#             if(i.client.cin==cin):
#                 C.append(i)
#         return C
    
#     def CompteMax(self):
#         M=[]
#         for i in self.liste_de_compte:
#             M.append(i.solde)
#         C=""
#         for i in self.liste_de_compte:
#             if(i.solde==max(M)):
#                 C+=str(i)+"\n"
#         return C
    

# b=Banque('BP','CASA')

# while True:
#     while True:
#         print("""
#             1-Ajouter un compte à la banque.
#             2-Supprimer un compte à partir de son code (si son solde est égal à zéro).
#             3-Modifier le numéro de téléphone du client d'un compte donné.
#             4-Rechercher un compte à partir de son Numéro.
#             5-Afficher toutes les informations de la banque.
#             6-Afficher tous les comptes de la banque
#             7-Afficher tous les comptes d'épargnes de la banque
#             8-Afficher les comptes courants qui ont un solde entre deux valeurs données.
#             9-Rechercher le(s) compte(s) à partir de son Client (CIN).
#             10-Afficher la somme de tous les comptes d'épargne de la banque.
#             11-Afficher la somme de tous les comptes d'un client donné (CIN) 
#             12-Afficher les comptes ayant le solde maximal.
#             13-Quitter
# """)
#         a=int(input("donner un operation"))
#         if (a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 or a==8 or a==9 or a==10 or a==11 or a==12 or a==13):
#             break
#         else:
#             print("doit entre 1 a 13 ")
        
        
#     if(a==1):
#         s=float(input("Donner le solde"))
#         t=input("Donner le type du compte (E/C) : ")
#         cin=input("donner la cin")
#         n=input("donner le nom")
#         p=input("donner le prenom")
#         a=input("donner adresse")
#         t=input("donner le telephone")
#         if b.AjouterCompte(Compte(s,t,Client(cin,n,p,a,t)))==True:
#             print("votre compte ajouter avec succee")
#         else:
#             print("Erreur !!")
    
#     elif(a==2):
#         code=input("donner le code de compte")
#         if b.SupprimerCompte(code)==True:
#             print("le compte a supprimer avec succee ")
#         else:
#             print("Erreur !!")

#     elif(a==3):
#         num=int(input("donner le numero de compte"))
#         tel=input("donner le numero de telephone nouveau")
#         if b.ModifierTelClient(num,tel)==True:
#             print("le telephone a modifier avec succee")
#         else:
#             print("Errour")

#     elif(a==4):
#         num=int(input("donner le num de compte"))
#         if b.RechercherCompte(num)==None:
#             print("aucun compte")
#         else:
#             print(b.RechercherCompte(num))

#     elif a==5:
#         print(b)

#     elif a==6:
#         print(b.ReteurnCompte())

#     elif a==7:
#         print(b.ReteurnCompteE())
    
#     elif a==8:
#         max=float(input("Donner la 2eme valeur : "))
#         min=float(input("Donner la 1er valeur : "))
#         print(b.ReteurnCompteC(max,min))

#     elif a==9:
#         cin=input("donner le cin")
#         c=b.returnCompteCin(cin)
#         if c=="":
#             print("aucun cin")
#         else:
#             print(c)

#     elif a==10:
#         d=b.ReteurnCompteE()
#         s=0
#         for i in d:
#            s+=i.solde
#         print(s)

#     elif a==11:
#         cin=input("donner le cin")
#         L=b.returnCompteCin(cin)
#         s=0
#         for i in L:
#             s+= i.solde
#         print(s)

#     elif a==12:
#         print(b.CompteMax())    

#     elif a==13:
#         break

    
     
#     v=input("voulez-vous continue O/N")
#     if v.lower()!='o':
#         break























# liste_de_produit=[{"Nom":"produit1","Prix":200,"Quantite":30},{"Nom":"produit2","Prix":250,"Quantite":20},{"Nom":"produit3","Prix":500,"Quantite":50}]

# def searchnom(list,nom):
#     C=None
#     for i in list:
#         if i['Nom']==nom:
#             C=i
#     return C

# while True:
#     while True:
#         print("""
#             1-Ajouter un nouveau produit à la liste avec son nom, son prix unitaire et sa quantité en stock.
#             2-Rechercher un produit en utilisant son nom, et afficher toutes ses informations.
#             3-Afficher la liste de tous les produits avec leurs informations.
#             4-Mettre à jour les informations d'un produit existant en utilisant son nom.
#             5-Supprimer un produit de la liste en utilisant son nom.
#             6-Quitter
# """)
#         a=int(input("donner un operation"))
#         if (a==1 or a==2 or a==3 or a==4 or a==5 or a==6):
#             break
#     if a==1:
#         nom=input("donner le nom de produit")
#         b=searchnom(liste_de_produit,nom)
#         if b!=None:
#             print("Le produit deja dans la list")
#         else:
#             prix=float(input("donner le prix"))
#             quantite=int(input("donner la quantite"))
#             liste_de_produit.append({"Nom":nom,"Prix":prix,"Quantite":quantite})
#             print("le produite ajouter avec succee")
#     elif a==2:
#         nom=input("donner le nom de produit")
#         b=searchnom(liste_de_produit,nom)
#         if b==None:
#             print("aucun produit a cette nom")
#         else:
#             print(b)
#     elif a==3:
#         for i in liste_de_produit:
#             print(i)

#     elif a==4:
#         nom=input("donner le nom de produit")
#         b=searchnom(liste_de_produit,nom)  
#         if b==None:
#             print("aucun produit a cette nom")
#         else:
#             b['Prix']=float(input("donner nouveau prix"))
#             b['Quantite']=int(input("donner nouveau quantite"))
#             print("Mettre à jour les informations d'un produit avec succee ")
    
#     elif a==5:
#         nom=input("donner le nom de produit")
#         b=searchnom(liste_de_produit,nom)  
#         if b==None:
#             print("aucun produit a cette nom")
#         else:
#             liste_de_produit.remove(b)
#             print("Produit supprimer avec succee")    


#     elif a==6:
#         break

#     v=input("voulez-vous continue O/N")
#     if v.lower()!='o':
#         break


# class Client:
#     def __init__(self, c, n, p, t='*********'):
#         self.__Cin = c
#         self.__Nom = n
#         self.__Prenom = p
#         self.__Tel = t

    
#     def afficher(self):
#         print(f"{self.Nom} {self.__Prenom} / CIN : {self.__Cin} / N°TEL : {self.__Tel}")

#     @property
#     def Cin(self):
#         return self.__Cin
#     @Cin.setter
#     def Cin(self,c):
#         self.__Cin = c

#     @property
#     def Nom(self):
#         return self.__Nom
#     @Nom.setter
#     def Nom(self,n):
#         self.__Nom = n

#     @property
#     def Prenom(self):
#         return self.__Prenom
#     @Prenom.setter
#     def Prenom(self,p):
#         self.__Prenom = p

#     @property
#     def Tel(self):
#         return self.__Tel
#     @Tel.setter
#     def Tel(self,t):
#         self.__Tel = t

# class CompteBancaire:
#     __count=0
#     def __init__(self, P):
#         self.__solde = 0
#         CompteBancaire.__count += 1
#         self.__code= CompteBancaire.__count
#         self.__prop=P

#     @property
#     def prop(self):
#         return self.__prop
#     @prop.setter
#     def prop(self,p):
#         self.__prop =p

#     @property
#     def solde(self):
#         return self.__solde
    
#     @property
#     def code(self):
#         return self.__code
    
#     def Crediter(self,mt):
#         if mt>0:
#             self.__solde +=mt

#     def Debiter(self,mt):
#             self.__solde -=mt
   
#     def __str__(self):
#         return f", le numero de compte {self.__code}:  , le solde : {self.__solde} prop : {self.prop} "
        
# P=CompteBancaire(Client(12,'nom1','prenom1','03998383'))
# print(P) 















