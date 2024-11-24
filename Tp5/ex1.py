
try:
    a =float(input("entrer un nombre reel"))
    print("votre nombre est", a)
except ValueError:
    print("nombre reel invalide!")
except:
    print("Erreur!")

print("reste du programme") 