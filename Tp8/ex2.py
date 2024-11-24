etudiants ={"etudiant 1 " : 13 , "etudiant 2" : 17 , "etudiant 3" : 9 , "etudiant 4" : 15 , "etudiant 5" : 8 , "etudiant 6" : 14 , "etudiant 7" : 16 , "etudiant 8" : 12 }

etudiantsadmis={}
etudiantsnoadmis={}
for i,j in etudiants.items():
    if j>=10:
        etudiantsadmis[i]=j
    else:
        etudiantsnoadmis[i]=j

print("etudiant admis",etudiantsadmis)
print("etudiant no admis",etudiantsnoadmis)