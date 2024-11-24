def Pluschere(T):
    # V=[]
    # max=0
    # for i in T:
    #     if i.get("prix")>=max:
    #         max = i.get("prix")
    # for i in T:
    #     if  i["prix"]==max:
    #         V.append(i)
    # return V

    V=[]
    max=0
    for i in T:
        if i.get("prix")>max:
            max=i.get("prix")
    for i in T:
        if i.get("prix")==max:
            V.append(i)
    return V
    




v=[{"Matricule":"E1","Marque":"bmw","modele":"2018","prix":200000},{"Matricule":"E2","Marque":"golf","modele":"2020","prix":300000},{"Matricule":"E3","Marque":"seat","modele":"2015","prix":150000},{"Matricule":"E2","Marque":"amg cls","modele":"2019","prix":300000}]
voiture=[]
# for i in range(2):
#     D={}
#     D["Matricule"]=input("donner la Matricule de voiture")
#     D["Marque"]=input("donner la Marque de voiture")
#     D["Modele"]=input("donner le Modele de voiture")
#     D["prix"]=float(input("donner le prix de voiture"))
#     voiture.append(D)

# for i in voiture:
#     print(i)
# for i in range(1):
#     D={}
#     D['Matricule']=input("donner la Matricule de voiture")
#     D["Marque"]=input("donner la Marque de voiture")
#     D["Modele"]=input("donner le Modele de voiture")
#     D["prix"]=float(input("donner le prix de voiture"))
#     voiture.append(D)
for i in v:
    print(i)






print( "les voiture Pluschere :",Pluschere(v))



