pokedex = {}
with open('pokemonlista.txt', 'r+') as file:
    for line in file:
       line = line.split() 
       pokedex[line[1]] = line[0] + " " + line[2]

print(pokedex["Gastly"])
print(pokedex["Pikachu"])