liste_de_produit=[{"Nom":"produit1","Prix":200,"Quantite":30},{"Nom":"produit2","Prix":250,"Quantite":20},{"Nom":"produit3","Prix":500,"Quantite":50}]
def searchnom(D,nom):
    c=None
    for i in D:
        if i["Nom"]==nom:
            c=i
            break
    return c
          
while True:
    while True:
        print("""
 	1-Ajouter un nouveau produit à la liste avec son nom, son prix unitaire et sa quantité en stock.
 	2-Rechercher un produit en utilisant son nom, et afficher toutes ses informations.
 	3-Afficher la liste de tous les produits avec leurs informations.
 	4-Mettre à jour les informations d'un produit existant en utilisant son nom.
 	5-Supprimer un produit de la liste en utilisant son nom.
    6-Quitter
""")
        a=int(input("donner un operation"))
        if (a==1 or a==2 or a==3 or a==4 or a==5 or a==6):
            break
    
    if a==1:
        nom=input("donner le nom de produit")
        b=searchnom(liste_de_produit,nom)
        if b!=None:
            print("Le produit deja dans la list")
        else:
            prix=float(input("donner le prix"))
            quantite=int(input("donner la quantite"))
            D={"Nom":nom,"Prix":prix,"Quantite":quantite}
            liste_de_produit.append(D)
            print("le produite ajouter avec succee")

    elif a==2:
        nom=input("donner le nom de produit")
        b=searchnom(liste_de_produit,nom)
        if b==None:
            print("aucun produit a cette nom")
        else:
            print(b)
    elif a==3:
        for i in liste_de_produit:
            print(i)
    elif a==4:
        nom=input("donner le nom de produit")
        b=searchnom(liste_de_produit,nom)
        if b==None:
             print("aucun produit a cette nom")
        else:
            b["Prix"]=float(input("donner nouveau prix"))
            b["Quantite"]=int(input("donner nouveau quantite"))
            print("Mettre à jour les informations d'un produit avec succee ")
    elif a==5:
        nom=input("donner le nom de produit")
        b=searchnom(liste_de_produit,nom)
        if b==None:
            print("aucun produit")
        else:
            liste_de_produit.remove(b)
            print("Produit supprimer avec succee")    
    elif a==6:
        break
        

    v=input("voulez-vous continue O/N")
    if v.lower()!="o":
        break

