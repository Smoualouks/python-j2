import os   

# je crée le dossier flagsBis et je traite l'érreur si le dossier existe:

try:
  os.mkdir("flagsBis")

except:
    print("Le dossier flagsBis existe déjà !!!")
    raise Exception("le dossier existe déjà, sortir du programme")

# je parcour le dossier flags:

for f in os.listdir("flags"):
    if  f.startswith("miss"):
        os.rename("flags/" + f,"flagsBis/" + f)
    else:
        os.rename("flags/" + f,"flagsBis/" + f[:2].upper())
        print("[+] file %s  renamed et replaced in flagsBis folder" % f)

