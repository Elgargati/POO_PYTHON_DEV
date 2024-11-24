try:
    nChaine = ''
    print("entrer une chaine de characteres")
    s = str(input())
    print("entrer le premier indice")
    i1 = int(input())
    print("entrer la deuxieme indice")
    i2 = int(input())
    if i2 < i1:
        i1, i2 = i2, i1
    for i in range(i1, i2+1):
        nChaine += s[i]

    print(nChaine) 

except ValueError as e:
    print(f"erreur de valeur: {e}")
except IndexError as e:
    print(f"erreur d'indice: {e}")
except Exception as e:
    print(f"erreur: {e}")