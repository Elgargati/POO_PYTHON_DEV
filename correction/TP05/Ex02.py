T = [1, 2, 3, 4, 5, 6, 90]
try:
    print("entrer un numero d'indice")
    a = int(input())
    print(f"le nombre qui a l'indice {a} dans le tableau T est {T[a]}")
except ValueError:
    print("numero d'indice invalide!")
except IndexError:
    print(f"numero d'indice non valide, entrer un numero entre {0} et {len(T) - 1}")
except:
    print("Erreur!")
print("reste du programme")