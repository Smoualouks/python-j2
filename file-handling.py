f = open("files/demo.txt", "r")   # r veut dire read mode.

# print(type(f))
content = f.read()     # read permet de lire le fichier.
f.close()

newContent = content.replace("démo", "preuve")
print(content)
print(newContent)

f2 = open("files/new","w")     # w pour crée  nouveau fichier 
f2.write(newContent)
f2.close()