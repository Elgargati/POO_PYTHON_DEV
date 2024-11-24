class Etudiant:
    
    def __init__(self,nom="inconnu",matri="inconnu",cour="inconnu"):
        self.nom=nom
        self.matricule=matri
        self.cours=cour
        self.notes=[]

    def afficher_info(self):
        print(f"le nom de Etudiant {self.nom}" )
        print(f"le matricule {self.matricule}"  ) 
        print(f"le cours {self.cours}" ) 

    def ajouter_notes(self,c):
        self.notes.append(c)

    def calculer_notes(self):
        s=0
        s=sum(self.notes)
        m=s/len(self.notes)
        return m
    
    def afficher_notes(self):
        print(f"les notes est {self.notes}")

# nom=input('donner le nom')
# matri=input('donner le matricule')    
# cour=input('dinner le cour')
etd1=Etudiant("simo","G136154326","Math")
etd1.afficher_info()
etd1.ajouter_notes(12)
etd1.ajouter_notes(14)
etd1.ajouter_notes(16)
etd1.ajouter_notes(16)
etd1.afficher_notes()
print(f" la moyenne est :{etd1.calculer_notes()}")
print("___________________________________")
etd2=Etudiant("ali","G136234354","algo")
etd2.afficher_info()
etd2.ajouter_notes(11)
etd2.ajouter_notes(17)
etd2.ajouter_notes(10)
etd2.ajouter_notes(19)
etd2.afficher_notes()
print(f" la moyenne est :{etd2.calculer_notes()}")


