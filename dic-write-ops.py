student1 = {
    "age": 25,
    "lname": "PASCAL",
    "fname": "Blaise",
    "isGoodLearner": True
}

print(student1)

# Ajout d'une clé/valeur

student1["grades"] = [17, 12, 19.5]
print(student1)

#Modif d'une valeur:

student1["age"] = 27

# modi multi-clés

student1.update({"age": 22, "fname": "Blaisou"})
print(student1)

#Supression d'une clé:

student1.pop("grades")
print(student1)

#itération sur les valeurs du dict uniquement
for v in student1.values():
    print(v)

# itération sur les clés:
for k in student1.keys():
    print(k)

for k, v in student1.items():
    print(k, v)