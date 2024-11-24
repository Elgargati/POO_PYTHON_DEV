try:
    print("entrer un nombre reel")
    a = float(input())
    print("votre nombre est", a)
except ValueError:
    print("nombre reel invalide!")
except:
    print("Erreur!")

print("reste du programme") 
