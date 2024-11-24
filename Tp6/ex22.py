class InvalidePrix(Exception):
    pass
class InvalideQuantite(Exception):
    pass
class InvalideReference(Exception):
    pass

import time

class Article :
    def __init__(self,r,n,p,q):
        self.reference=r
        self.__nom=n
        self.prix=p
        self.quantite=q
        
    @property 
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n
        
    @property
    def reference(self):
        return self.__reference
    @reference.setter
    def reference(self,q):
        if q>0 :
            self.__reference=q
        else :
            raise InvalideQuantite  ("La quantite invalide")
    
    @property 
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,p):
        if p>0 :
            self.__prix=p
        else :
           raise InvalidePrix ("Le prix Invalide")    
        
    @property
    def quantite(self):
        return self.__quantite
    @quantite.setter
    def quantite(self,q):
        if q >= 0 :
            self.__quantite=q
        else :
            raise InvalideQuantite  ("La quantite invalide")  
        
        
    def __str__(self):
        return f"Le nom d'article : {self.__nom} , son quantite en stock :{self.__quantite} pieces , son numero de reference {self.__reference} et son prix : {self.__prix} dh"  
    
    
    
L=[Article(1,"article1",300,10),Article(2,"article2",200,16),Article(3,"article3",400,34),Article(4,"article4",280,0)]
    
        
while True :
    print("         Menu :      ")
    print("1-Afficher tous les articles")
    print("2-Afficher les articles en rupture de stock")
    print("3-Rechercher un article par reference") 
    print("4-Rechercher un article par nom")
    print("5-Rechercher un article par intervalle de prix de vente")
    print("6-Verifier la disponabilite d'un article")
    print("7-Ajouter un article au stock")
    print("8-Supprimer un article par reference")
    print("9-Modifier un article par reference")
    print("10-Quitter")
    try:
        n=int(input("Donner le nombre qui represente votre choix : "))
    except Exception as a:
            print(a)
            
    if n==1 :
        for i in L :
            print(i)
            
    elif n==2 :
       for i in L :
           if i.quantite == 0 :
               print(i)
               
    elif n==3 :
        try:
           r=int(input("Donner le reference d'article : "))
        except Exception as a :
            print(a)
        for i in L :
            if i.reference == r :
                print(i)
                break
        if i.reference != r :
                print("cet article n'exciste pas")
    
    elif n==4 :
        try:
           nom=input("Donner le nom d'article : ")
        except Exception as a :
            print(a)
        for i in L :
            if i.nom == nom :
                print(i)
                break
        if i.nom != nom :
                print("cet article n'exciste pas")
            
    elif n==5 :
        try:
           p1=float(input("La 1er valeur : "))
           p2=float(input("La 2eme valeur : "))
        except Exception as a :
            print(a)
        if  p2 < p1 :
            p3=p1
            p1=p2
            p2=p3
        for i in L :
            if i.prix > p1 and i.prix < p2 :
                print(i)
                
    elif n==6 :
        try:
           nom=input("Donner le nom d'article : ")
        except Exception as a :
            print(a)
        for i in L :
            if i.nom == nom and i.quantite > 0:
                print("cet article disponible pour le moment . ")
                break
        if i.nom == nom and i.quantite == 0:
            print("cet article indisponible pour le moment . ")
        if i.nom != nom :
                print("cet article n'exciste pas")
                
    elif n==7 :
        try :
            n=input("Donner le nom d'article : ")
            r=int(input("Donner le num de reference : "))
            p=float(input("Donner le prix : "))
            q=int(input("Donner la quantite "))
        except Exception as a :
            print(a)
        L.append(Article(r,n,p,q))
        time.sleep(1)
        print("L'article est ajouter avec success")
        
    elif n==8 :
        try:
           r=int(input("Donner le reference d'article : "))
        except Exception as a :
            print(a)
        for i in L :
            if i.reference == r :
                L.remove(i)
                break
        if i.reference != r :
                print("cet article n'exciste pas")
                
    elif n==9 :
        try:
           r=int(input("Donner le reference d'article : "))
        except Exception as a :
            print(a)
        try:
           a=int(input("Vous voulez modifie quoi [1.nom / 2.ref / 3.prix /4.quntite / 5.tous]"))
        except Exception as a :
            print(a)
        if a==5 :
            try :
                n=input("Donner le nom d'article : ")
                r=int(input("Donner le num de reference : "))
                p=float(input("Donner le prix : "))
                q=int(input("Donner la quantite "))
            except Exception as a :
                print(a)
        for i in L :
            if i.reference == r :
                print(i)
                i.nom=n
                i.reference=r
                i.quantite=q
                i.prix=p
            if a==1 :
                n=input("Donner le nom d'article : ")
                for i in L :
                    if i.reference == r :
                        i.nom=n
        try:   
            if a==2 :
                r=int(input("Donner le num de reference : "))
                for i in L :
                    if i.reference == r :
                        i.reference=r
                        
            if a==3 :
                p=float(input("Donner le prix : "))
                for i in L :
                    if i.reference == r :
                        i.quantite=q
                        
            if a==4 :
                q=int(input("Donner la quantite "))
                for i in L :
                    if i.reference == r :
                        i.prix=p
        except Exception as a :
            print(a)                
        
    else :
        print("Au revoire !!")
        break
       