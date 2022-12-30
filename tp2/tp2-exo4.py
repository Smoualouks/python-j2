from sys import argv

sample_dict = {'a': 100, 'b': 200, 'c': 300};

quoi=int(argv[1]);

for k in sample_dict:
    if sample_dict[k] == quoi:
        print (quoi, " est présente dans la case: ", k);


