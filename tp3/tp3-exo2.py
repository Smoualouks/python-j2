import csv

# Ouvrir le fichier deniro.csv

bestScore = -1
nombeFilms = 0

with open('deniro.csv', 'r') as f:

       # Créer un objet csv à partir du fichier

       myReader = f.readlines()

       # je suprime la première ligne contenant les noms des colonnes:
       myReaderWithoutFirstLine = myReader[1:]
      
       for line in myReaderWithoutFirstLine:
       

        
        #  for i in line:
        #     if i[1] > bestScore:
        #         bestScore = i[1]
        #     if i[0] >= 2000 and i[0] <= 2010:
        #         nombeFilms += 1
        
             
            
           