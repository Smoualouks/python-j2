# on définit une fct avec le mot clé def:
def hello():
    print("hello") #  hello() fct impure car elle appele une autre fct en l'occurence print içi

# return en réalité None même s'il est invisible
#hello()


def hello2():
    return "Hello again !"

r = hello() # le retour de hello() est assigné à la variable r
print(r)
hello2()
print(hello2())