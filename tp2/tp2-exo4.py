dict = {'a': 100, 'b': 200, 'c': 300}

valeure = input( "saisissez la valeur à chercher: ")

for x in dict:
    if dict[x] == valeure:
       print(valeure, "exist in dict")
    exit(1) 

    

