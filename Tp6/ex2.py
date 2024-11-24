class Article:
    def __init__(self, nr, n, p, q ):
        self.__numero=nr
        self.__nom= n
        self.__prix=p
        self.__quantite=q

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,nr):
        self.__numero = nr
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom = n
    
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,p):
        self.__prix = p
    
    @property
    def quantite(self):
        return self.__quantite
    @quantite.setter
    def quantite(self,q):
        self.__quantite = q
    
    def __str__(self):
        return f" le numero de reference est : {self.numero} le nom : {self.nom} le prix : {self.prix} quantite en stock est : {self.quantite} "

L=[Article(1,'article1',100,0),Article(2,'article3',300,20),Article(3,'article1',300,30),Article(4,'article3',400,40),Article(5,'article3',500,50)]

def search(T,a):
    c=None
    for i in T:
        if i.numero==a:
            c=i
            break
    return c

while True:
    while True:
        print("""

            1.Afficher tous les articles.
                
            2.Afficher les articles en rupture de stock.

            3.Rechercher un article par reference.
            
            4.Rechercher un article par nom.

            5.Rechercher un article par intervalle de prix de vente.

            6.Verifier la disponibilite d'un article.

            7.Ajouter un article au stock.

            8.Supprimer un article par reference.

            9.Modifier un article par reference.

            10.Quitter.
                    """)
        a=int(input("donner un operation"))
        if (a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 or a==8 or a==9 or a==10):
            break
        else:
            print("vous devez entrer de 1 a 10")

    if a==10:
        break

    if a==1:
        if L==[]:
            print("aucun article")
        else:
            for i in L:
                print(i)

    elif a==2:
        p=[i for i in L if i.quantite==0]
        # for i in L:
        #     if i.quantite==0:
        #         P.append(i)
        if len(p)!=0:
            for i in p:
                print(i)
        else:
            print(f'Aucune quantite est en rupture de stock.')

    elif a==3:
        a=int(input("donner reference article"))
        d=search(L,a)
        if d==None:
            print("aucun article")

        else:
            print(d)

    elif a==4:
        n=input("donner un nom")
        P=[i for i in L if i.nom==n ]
        # for i in L:
        #     if i.nom==n:
        #         p.append(i)
        if len(P)!=0:
            for i in P:
                print(i)
        else:
            print("aucun nom cette article")

    elif a==5:
        p=int(input("donner prix de vente"))
        k=[i for i in L if i.prix==p]
        if len(k)!=0:
            for i in k:
                print(i)
        else:
            print("aucun prix de vente cette article")

    elif a==6:
        a = int(input("Donner le code reference d'article: "))
        c=search(L,a)
        if c==None:
            print("reference introuvable")
        elif c.quantite!=0:
            print("disponible")
        else:
            print("pas disponible")

    elif a==7:
        a1=int(input("donner la reference"))
        c=search(L,a1)
        if c != None:
            print("Numero reference double.")
        else:
            a2 = input("Donner le nom d'article: ")
            a3 = float(input("Donner le prix d'article: "))
            a4 = int(input("Donner sa quantite: "))
            L.append(Article(a1,a2,a3,a4))
            print("Article ajouter.")

    elif a==8:
        a=int(input("donner la reference"))
        c=search(L,a)
        if c==None:
            print("aucun article")
        else:
            L.remove(c)
            print("Article supprimered")

    elif a==9:
        a=int(input("donner la reference article"))
        c=search(L,a)
        if c==None:
            print("aucun article")
        else:
            while True:
                v=int(input(" modifier le nom (1) ou le prix (2) ou quantite (3) ou quitter (4): "))
                if v==1:
                    a1=input("donner nouveau nom")
                    c.nom=a1
                    print("article modifier.")
                elif v==2:
                    a2=int(input("donner nouveau prix"))
                    c.prix=a2
                    print("article modifier.")

                elif v==3:
                    a3=int(input("donner nouveau quantite"))
                    print("article modifier.")
                elif v==4:
                    break
                else:
                    print("Choix invalide")



    v=input("vous voulez continuer O/N :")
    if (v!="O" and v!="o"):
        print("merci")
        break 
