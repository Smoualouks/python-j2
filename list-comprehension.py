fruits = [ "poire", "pomme", "banane", "kiwi", "mangue"]
newList = [x for x in fruits if "a" in x]

print(newList)

def square(n):
    return n*n

numbers = [6, 4, 40, 10, 8, 15]
squares = [square(x) for x in numbers if x >= 10]
print(squares)