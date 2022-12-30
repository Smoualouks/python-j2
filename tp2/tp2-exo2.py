
# exo 2:

tableau = []

saisie = 1

while saisie != 0:
    saisie = int(input("Entrer un chiffre svp: "))
    tableau.append(saisie)

print(tableau)
print("la somme des valeurs saisies est:", sum(tableau))
