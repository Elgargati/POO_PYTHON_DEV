#création de la classe ayoub
class Personne:
    __pays="Maroc"
    def __init__(self,n,p,a):        #constructeur d'initialisation et par défault
        self.__nom=n    #initialisation des attributs
        self.__prenom=p  #initialisation des attributs
        self.age=a  #initialisation des attributs
    
    def Sepresenter(self):     #définition d'une méthode (procédure)
        print("Je m'appelle ",self.__nom,self.__prenom, " et j'ai",self.__age," ans")
    
    # def get_age(self):
    #     return self.__age
    
    # def set_age(self,a):
    #     if(isinstance(a,int) and a>0):
    #         self.__age=a
    #     else:
    #         print("L'age doit être un entier positif")
    @staticmethod
    def get_pays():
        return Personne.__pays
    @staticmethod
    def description():
        print("cette classe représente des personnes ...............;")

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,a):
        if(a>0):
            self.__age=a
        else:
            print("L'age doit être positif")

    # def get_nom(self):
    #     return self.__nom
    
    # def get_prenom(self):
    #     return self.__prenom
    
    # def set_prenom(self,p):
    #     self.__prenom=p

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n


#le progarmme : ayman
# p1 = Personne("Mohamed","Ali",20)
# p2 = Personne("Ahmed","Karim",30)

# print(Personne.get_pays())

Personne.description()



# Personne.pays="France"
# print(Personne.pays)

# print(p1.pays)
# print(p2.pays)


#p.Sepresenter()

# print(p.get_age())   #getter de l'attribut age

# p.set_age('a')

# p.Sepresenter()

# print(p.get_prenom())
# print(p.get_nom())

# p.set_prenom("Karim")

# p.Sepresenter()

# print(p.age)
# p.age=40

# p.nom="Ahmed"
# print(p.nom)

# p.Sepresenter()







