colors = [] # liste vide
print(colors)

colors.append("vert")
print(colors)

colors.append("blanc")
print(colors)

colors.append("rouge")
print(colors)

colors.clear() # suprime tous les élément de la liste
print(colors)

colors.append("vert")
print(colors)

colors.append("blanc")
print(colors)

colors.append("rouge")
print(colors)

colors[0] = "bleu"
print(colors)

colors.remove("blanc") # parcour la liste, dès que tu trouve bc, tu le suprime
print(colors)