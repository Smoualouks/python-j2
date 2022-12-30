try:
    print("toto")
    [1,2,3][6]
except NameError:
    print("Problème de nom")
except:
    print("Erreur")

except IndexError:
    print("problème d'index")
print(toto)  # python 
