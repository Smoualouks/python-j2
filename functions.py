# on définit une fct avec le mot clé def:
def hello():
    print("hello") #  hello() fct impure car elle appele une autre fct en l'occurence print içi

# return en réalité None même s'il est invisible, retour implicit
#hello()


def hello2():
    return "Hello again !"

def addTwo(n):
    return n+2

def square(n):
    return n*n

def sum(a,b):
    return a + b


r = hello() # le retour de hello() est assigné à la variable r et reçoi donc None
print(r)
hello2()
print(hello2())

print(addTwo(5))
finalValue = addTwo(addTwo(addTwo(5)))
print(finalValue)

print(square(5))
print(sum(4, 1) + sum(6, 4))

#Affichage de carré pour toutes les valeurs de tab

numbers = [6, 4, 40, 10, 8, 15]
for n in numbers:
    if n >= 10:
        print(n, "=>", square(n))