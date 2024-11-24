
L=[]
for i in range(3):
    voiture={}
    matricul=input(f"Donner le matricule de la voiture {i+1} :  ")
    marque=input(f"Donner la marque de la voiture {i+1} :  ")
    modele=input(f"Donner le module de la voiture {i+1} :  ")
    prix=float(input(f"Donner le prix de la voiture {i+1} :  "))
    voiture["matricul"]=matricul
    voiture["marque"]=marque
    voiture["modele"]=modele
    voiture["prix"]=prix
    L.append(voiture)

max=L[0].get("prix")
for j in range (len(L)):
        if max<L[j].get("prix"):
            max=L[j].get("prix")
            v=L[j]

print("La liste des voitures est :")
for i in L :
     print(i)
     
print("Les informations sur la voiture la plus chere : ",v)
