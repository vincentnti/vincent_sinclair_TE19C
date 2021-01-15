mening = input("Räkna antalet ord i meningen: ")
split = mening.split(" ")
print(split) #not needed
split = list(filter(None, split))
print(split) #not needed
print(f"{len(split)}")
