# raise  Exception("blabla")  # arrête net l'execution

def check(x):
    if x < 0:
        #print("négatif")
        raise Exception("Negative number forbidden")

try:
   check(-4)
except:
    print("Problème")

print(" *** The End ***") # ça ne s'execute pas car raise fait sortir de l'execution