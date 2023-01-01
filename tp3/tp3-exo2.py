import csv

# j'initalise la liste scores qui contiendera tous les scores, histoire d'avoir un itérable
# j'initialise la liste filmsName qui contiendera tous les noms des films
# j'initialise la liste years qui contiendera toutes les années de sortie de filsm
# la variable filmsCount, pour compter le nombre des films entre 2000 et 2010

scores = []
filmsName = []
years = []
filmsCount = 0

# j'ouvre le fichier deniro.csv:

with open('deniro.csv', 'r') as f:

    # je lis le contenu du fichier csv.
    
    myReader = csv.reader(f)
    # j'invoque la méthode next() pour sauter la première ligne contenant le nom des colonnes.
    next(myReader)
    
    # j'appele la méthode append() pour alimenter toutes mes listes précedement initialisées.
    for line in myReader:

       years.append(int(line[0]))
       scores.append(int(line[1]))
       filmsName.append(line[2])


# je récupère l'index du film ayant le score max
index = scores.index(max(scores))

# je compte le nombre des films sorti entre [2000,2010]          
for year in years:
       if year >= 2000 and year <= 2010:
              filmsCount += 1


# je crée un nouveau fichoer txt ou je récupère le nom du film ayant le meilleur score et 
#le nombre des films sortis entre 2000 et 2010
filepath = "deniro-report.txt"
f = open(filepath, "w")
f.write("Nom du film le mieux noté est: " + filmsName[index][2:-2] + "\n" + "Nombre de films entre 2000 et 2010 est: " + str(filmsCount))
f.close()       


#-------------------------------------------- The End ----------------------------------------------------------       
             
            
           