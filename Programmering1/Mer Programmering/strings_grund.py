# Strings in Python
# Index Operator []
# Slice Operator :
# Concatenation
# Escape Sequences
# String manipulation functions

"""
# Concatenation (Adding strings)

firstname = "Vincent"
lastname = "Sinclair"
age = "17"
address = "Lägenhet"
phone = 112

fullname = firstname + " " + lastname

personuppg = "Namn: " + fullname + "\n" + "Age: " + str(age) + "\n" + "Phone Number: " + str(phone) + "\n" + "Home: " + address
print(personuppg)
"""
"""
#Indexing

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

# len funktion
print(f"Alfabetet innehåller {len(alfabet)} bokstäver")

print(f"Bokstav på index 0: {alfabet[0]}")
print(f"Bokstav på index -2: {alfabet[-2]}")
print(f"Bokstav på index 6: {alfabet[6]}")
print(f"Alfabetet baklänges: {alfabet[::-1]}")
"""
"""
#split()

favoritämnen = "Matematik programmering teknik webbutveckling fysik"
favoritmat = "lasagne, korv, grönsaker, kebab, ris"

favoritämnen = favoritämnen.split()
favoritmat = favoritmat.split(", ")

print(favoritämnen)
print(favoritmat)

for i in favoritmat:
    print("I love to eat " + i)
"""