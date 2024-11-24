import time
class InvalidCINException(Exception):
        pass

class Stagiaire:
    def __init__(self,c,n,p,f,no):
        self.cin = c
        self.nom = n
        self.__prenom = p
        self.__filiere = f
        self.note = no

    @property
    def cin(self):
        return self.__cin
    @cin.setter
    def cin(self,c):
        if (len(c)==7 and c[2:].isdigit() ):
            self.__cin = c
        else:
            raise InvalidCINException("Le CIN est invalide")
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom = n

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,p):
        self.__prenom = p

    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self,f):
        self.__filiere = f

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self,no):
        if (isinstance(no,float) or isinstance(no,int) and no>=0 and no<=20):
            self.__note = no
        else:
            raise Exception("note must be between 0 and 20")

    def __str__(self):
        return f" CIN {self.__cin} le prenom : {self.__prenom} le Nom : {self.__nom} le Filiere {self.__filiere} la note de stagiare est {self.__note}"

L= [ Stagiaire("EE11223",123,"el gargati","dev",16),Stagiaire("EE11224","nom1","el prenom1","dev",12),Stagiaire("EE11225","nom2","el prenom2","dev2",14)]
# L=[]



while True:
        while True:
            print("****************")
            print("******** MENU ********")
            print("1. Affiche tous les stagiaire")
            print("2. Afficher les notes de tous les stagiaire")
            print("3. Afficher les stagiaire ayant une note superieure  ou egale a une note donne")
            print("4. Ajouter un stagiaire ")
            print("5. Recherche un stagiaire par CIN donne")
            print("6. Recherche un stagiaire D'une filiere")
            print("7. supremer un stagiaire dans le cin ")
            print("8. Quitter")
            try:
                operation=int(input("donner un operation "))
                if (operation==1 or operation==2 or operation==3 or operation==4 or operation==5 or operation==6 or operation==7 or operation==8 ):
                    break
                else:
                    print(" doit entre un nombre de 1 a 8")
            except Exception as a:
                print(a)

        if operation==8:
                print("Vous avez quitter le programme")
                break 
        

        elif operation==1:
            if (L==[]):
                print("Aucun stagiaire")
            else:
                for i in L:
                    print(i)


        elif operation==2:
            if(L==[]):
                print("Aucun stagiaire ")
            else:
                for n in L:
                    print(n.note)


        elif operation==3:
                if(L==[]):
                    print("Aucun stagiaire")
                else:
                    try:
                        N=float(input("donner la note :"))
                    except Exception as e:
                        print(e)

                    K=[]
                    for x in L:
                        if (x.note>=N):
                            K.append(x)

                    if (L==[]):
                            print("cela n'existe pas ")
                    else:
                        for i in K:
                            print(i)
                    


        elif operation==4:
                cin=input("donner le CIN")
                a=[]
                for i in L:
                    if (i.cin==cin):
                        a.append(cin)
                        break
                if(a!=[]):
                    print("le CIN deja existe")
                else:
                    n=input("donner le nom ")
                    p=input("donner le prenom ")
                    f=input("donner la filier")
                    no=float(input("donner la note"))
                    L.append(Stagiaire(cin,n,p,f,no))
                    print("Stagiaire ajouter avec succès.")

        elif operation==5:
            
                cin=input("donner le CIN")
                c=None
                for x in L:
                    if (x.cin==cin):
                        c=x
                        break
                if (c!=None):
                    print("cin deja existe")
                else:
                    n  = input("Entrez le nom : ")
                    p = input("Entrez le prénom : ")
                    f = input("Entrez la filière : ")
                    no= int(input("Entrez la note : "))
                    L.append(Stagiaire(cin,n,p,f,no))
                    print("Stagiaire ajouter avec succès.")

            

        elif operation==6:
                f=input("donner la filiere")
                T=[]
                for x in L:
                    if(x.filiere==f):
                        T.append(x)
                if(T==[]):
                    print("la filiere N'existe pas")
                else:
                    for i in T:
                        print(i)

            
            
        elif operation==7:
              
                cin=input("donner le CIN")
                T=False
                for i in L:
                    if (cin==i.cin):
                        L.remove(i)
                        T=True
                if T :
                    print("Stagiaire suprimer avec succès.")
                else :
                    print ("CIN entrer n'existe pas. ")
                            
            
           
    
        try:
            v=input("voullez vous continuez")
        except Exception as e:
            print(e)
        if v!="oui" and v!="OUI":
            break

            







    