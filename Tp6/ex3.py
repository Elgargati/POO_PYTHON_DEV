from abc import ABC,abstractmethod

class Ouvrage(ABC):
    __count=0
    def __init__(self,t):
        self.__titre=t
        Ouvrage.__count+=1
        self.__code=Ouvrage.__count
        self.__nb_emprunt=0
        self.__etat =True

    @property
    def titre(self):
        return self.__titre
    
    @titre.setter
    def titre(self,t):
        self.__titre=t

    @property
    def code(self):
        return self.__code
    
    @property
    def nb_emprunt(self):
        return self.__nb_emprunt
    @nb_emprunt.setter
    def nb_emprunt(self,n):
        self.__nb_emprunt=n
    @property
    def etat(self):
        return self.__etat
    @etat.setter
    def etat(self,c):
        self.__etat = c
    
    def disponibilite(self):
        if self.__etat== True:
            return f" disponible "
        else:
            return f"pas disponible"
        
    @abstractmethod
    def Emprunter():
        pass
    def Restituer():
        pass
        
    def __str__(self) -> str:
        return f" Le titre de l'ouvrage est :{self.titre} -- Le code {self.code} -- et  il est {self.disponibilite()} pour le moment, et le nombre d'emprunts de cet ouvrage est {self.nb_emprunt} "
            
class Livre(Ouvrage):
    def __init__(self, t,au,ed):
        super().__init__(t)
        self.__auteur=au
        self.__editeur=ed

    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self,au):
        self.__auteur =au

    @property
    def editeur(self):
        return self.__editeur
    @editeur.setter
    def editeur(self,ed):
        self.__editeur =ed

    def Emprunter(self):
        if self.etat:
            self.nb_emprunt+=1
            self.etat=False
            print(f"le livre {self.titre} et auteur {self.auteur} a ete emprunte avec succes ")
        else:
            print(f"Le livre n'est pas disponible pour emprunter.")
    
    def Restituer(self):
        if self.etat!=True:
            self.etat=True
            print(f"le livre {self.titre} et auteur {self.auteur} a ete restituer avec succes")
        else:
            print(f"le livre deja restituer")
    def __str__(self):
        return " livre : " + super().__str__()+ f"auteur : {self.auteur} , l'editeur  : {self.editeur} \n ************************************** "
    
class CD(Ouvrage):
    def __init__(self, t,a,nb):
        super().__init__(t)
        self.__artiste=a
        self.__nomber_pistes=nb

    @property
    def artiste(self):
        return self.__artiste
    @artiste.setter
    def artiste(self,a):
        self.__artiste=a

    @property
    def nomber_pistes(self):
        return self.__nomber_pistes
    @nomber_pistes.setter
    def nomber_pistes(self,a):
        self.__nomber_pistes=a

    def Emprunter(self):
        if self.etat:
            self.nb_emprunt+=1
            self.etat=False
            print(f"le CD {self.artiste} et le nomber de pistes {self.nomber_pistes} a ete emprunte avec succes ")
        else:
            print(f"Le CD n'est pas disponible pour emprunter.")
    
    def Restituer(self):
        if self.etat!=True:
            self.etat=True
            print(f"le CD {self.artiste} et le nomber de pistes {self.nomber_pistes} a ete restituer avec succes")
        else:
            print(f"le CD deja restituer")


    
    
    def __str__(self):
        return " CD :" + super().__str__()+ f"l'artiste : {self.artiste} , Nombre de pistes est  : {self.nomber_pistes} \n ********************************************** "

L=[Livre("livre1","auteur1","editeur1"),Livre("livre2","auteur2","editeur2"),Livre("livre3","auteur3","editeur3"),CD("cd3","artiste3",34),CD("cd4","artiste4",44),Livre("livre4","auteur4","editeur4"),CD("cd1","artiste1",17),CD("cd2","artiste2",93)]

def search(L,code):
    c=None
    for i in L:
        if i.code==code:
            c=i
            break
    return c


while True:
    while True:
        print("""
                1.  Afficher tous les ouvrages.
                2.	Afficher les ouvrages disponibles seulement.
                3.	Afficher tous les Livres.
                4.	Afficher tous les CDS.
                5.	Afficher les auteurs de tous les livres.
                6.	Afficher les artistes de tous les CDS.
                7.	Ajouter un ouvrage (Livre ou CD) à la bibliothèque.
                8.	Supprimer un ouvrage (par code)
                9.	Modifier le titre d'un ouvrage.
                10.	Rechercher un ouvrage par code. (Afficher également son type)
                11. Rechercher un Livre par code.
                12.	Rechercher un CD par code.
                13.	Rechercher un ouvrage par titre.
                14.	Rechercher un CD par artiste.
                15.	Rechercher un Livre par auteur.
                16.	Afficher tous les ouvrages classés par type.
                17.	Afficher les ouvrages triés par ordre croissant de nombres d'emprunt.
                18.	Emprunter un ouvrage par code.
                19.	Restituer un ouvrage par code.
                20.	Quitter.
""")
        a=int(input("donner un operation"))
        if (a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 or a==8 or a==9 or a==10 or a==11 or a==12 or a==13 or a==14 or a==15 or a==16 or a==17 or a==18 or a==19 or a==20):
            break
        else:
            print("doit entre 1 a 18 ")
    
    if a==1:
        if not L:
            print("la bibliotheque vide ")
        else:
            print("Afficher tous les ouvrages.")
            for i in L:
                print(i)

    elif a==2:
        if not L:
            print("la bibliotheque vide")
        else:
            K=[ i for i in L if i.etat]
            # for i in L:
            #     i.etat
            #     K.append(i)
            [print(i) for i in K] if  K else print("Aucun ouvrage n'est disponible")
            # if not K:
            #     for i in K:
            #         print(i)
            # else:
            #     print("Aucun ouvrage n'est disponible")

    elif a==3:
   
        if not L:
            print("la bibliotheque vide")
        else:
            liv=[i for i in L if isinstance(i,Livre)]
            # for i in L:
            #     if isinstance(i,Livre):
            #         liv.append(i)
            [print(i) for i in liv ] if liv else print("Aucun livre dans la bibliotheque")
            # if liv:
            #     for i in liv:
            #         print(i)
            # else:
            #     print("Aucun livre dans la bibliotheque.")
    elif a==4:
        if not L:
            print("la bibliotheque vide")
        else:
            liv=[i for i in L if isinstance(i,CD)]
            [print(i) for i in liv] if liv else print("Aucun CD dans la bibliotheque")

    elif a==5:
        if not L:
            print(" la bibliotheque vide")
        else:
            liv=[i for i in L if isinstance(i,Livre)]
            [print(i.auteur) for i in liv] if liv else print("Aucun auteur trouve")

            # if liv:
            #     for i in liv:
            #         print(i.auteur)
            # else:
            #     print("Aucun auteur trouve")

    elif a==6:
            liv=[i for i in L if isinstance(i,CD)]
            [print(i.artiste) for i in liv] if liv else print("Aucun artiste trouve")
    elif a==7:
        b=input("vous ajouter Livre ou CD ?")
        if b.lower()=='livre':
            titre=input("donner le titre de livre")
            auteur=input("donner auteur de livre")
            editeur=input("donner editeur de livre")
            L.append(Livre(titre,auteur,editeur))
            print("livre ajouter avec succee")
        elif b.lower()=='cd':
            titre=input("donner le titre de CD")
            artiste=input("donner artiste de CD")
            nb=int(input("donner le nombre pistes de CD"))
            L.append(CD(titre,artiste,nb))
            print("CD ajouter avec succee")
        else:
            print("invalide")
    elif a==8:
        c=int(input("donner le code de ouvrage"))
        c=search(L,c)
        if c==None:
            print("Code n'exist pas")
        else:
            L.remove(c)
            print("Ouvrage a ete supprimer")
    elif a==9:
        c=int(input("Donner le code de Ouvrage"))
        b=search(L,c)
        if b==None:
            print("code n'existe pas")
        else:
            b.titre = input("donner une nouvelle titre ")
            print("titre modifie avec succes")
    elif a==10:
        c=int(input("Donner le code de Ouvrage"))
        b=search(L,c)
        if b==None:
            print("code n'existe pas")
        else:
            if isinstance(b,Livre):
                print("Le type de Ouvrage Livre")
            elif isinstance(b,CD):
                print("Le type  de Ouvrage CD")
    elif a==11:
        c=int(input("Donner le code de livre"))
        b=search(L,c)
        if b==None:
            print(" le code n'existe pas")
        else:
            if isinstance(b,Livre):
                print(b)
            else:
                print("l'ouvrage est pas un Livre")

    elif a==12:
            c=int(input("Donner le code de CD"))
            b=search(L,c)
            if b==None:
                print(" le code n'existe pas")
            else:
                if isinstance(b,CD):
                    print(b)
                else:
                    print("l'ouvrage est pas un CD")

    elif a==13:
        tit=input("donner le titre de ouvrage ")
        D=[]
        for i in L:
            if i.titre.lower()==tit.lower():
                D.append(i)
        if D:
            for i in D:
                print(i)
        else:
            print("Aucun Ouvrage de cette titre")
    elif a==14:
        art=input("donner le nom de artiste")
        D=[]
        for i in L:
            if (isinstance(i,CD)):
                if i.artiste.lower()==art.lower():
                    D.append(i)
        if D:
            for i in D:
                print(i)
        else:
            print("Aucun artiste")
    elif a==15:
        aut=input("donner le nom de auteur")
        D=[]
        for i in L:
            if (isinstance(i,Livre)):
                if i.auteur.lower()==aut.lower():
                    D.append(i)
        if D:
            for i in D:
                print(i)
        else:
            print("Aucun auteur")
    elif a==16:
        for i in L:
            if isinstance(i,Livre):
                print(i)
        for i in L:
            if isinstance(i,CD):
                print(i)
    elif a==17:
        ouvrages_tries = sorted(L, key=lambda x: x.nb_emprunt, reverse=True)
        for ouvrage in ouvrages_tries:
                print(f"{ouvrage} - Nombre d'emprunts: {ouvrage.nb_emprunt}")
    elif a==18:
        c=int(input("donner un code de ouvrage"))
        b=search(L,c)
        if b==None:
            print("le code n'existe pas")
        else:
            b.Emprunter()
    elif a==19:
        c=int(input("donner un code de ouvrage"))
        b=search(L,c)
        if b==None:
            print("le code n'existe pas")
        else:
            b.Restituer()
    elif a==20:
        print("vous quitter le programme")
        break




                


    v=input("voulez-vous continue (O/N)")
    if v.lower() != 'o':
        print("vous quitter le program")
        break


    

    
