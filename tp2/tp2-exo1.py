# exo1


try:
    tva = float(input("Merci de saisir le taux de tva: "))
except ValueError:
    print (" saisissez une valeure valable: ")

prices = [14,100,30,10,8]

for n in prices:
    print( n + tva)
    