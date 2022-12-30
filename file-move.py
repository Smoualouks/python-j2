import os    #  ça permet de faire mkdir

# os.mkdir("blala")

# if not  os.path.exists("blala"):
#     os.mkdir("blala")
#     print("[+] dossier blala created")

# try:
#  os.rmdir("blala")
# except FileNotFoundError:
#     print("Le dossier n'existe pas")
#     exit(1)

# Objectif déplacer les fichier log de dossier files:

for f in os.listdir("files"):
    if  f.endsWith(".log"):
        os.rename("files/" + f,"files/logs/" + f)
        print("[+] file %s moved" % f)

print("******** The End ****")
