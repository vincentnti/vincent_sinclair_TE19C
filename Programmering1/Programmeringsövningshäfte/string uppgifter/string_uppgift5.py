#a)
"""
alfabet="abcdefghijklmnopqrstuvwxyzåäö"

word = input("Word: ")
word = list(word)

for i in range(len(word)):
    word[i] = alfabet[alfabet.find(word[i]) + 1]

print(''.join(word))
"""
#b)
"""
alfabet="abcdefghijklmnopqrstuvwxyzåäö"

word = input("Encrypted Word: ")
word = list(word)

for i in range(len(word)):
    word[i] = alfabet[alfabet.find(word[i]) - 1]

print(''.join(word))
"""
#c)
alfabet="abcdefghijklmnopqrstuvwxyzåäö"

word = input("Word: ")
encrypt = input("Encrypt/Decrypt? (en/de): ")
if encrypt == "en": 
    encrypt = 1
elif encrypt == "de":
    encrypt = -1

word = list(word)

for i in range(len(word)):
    word[i] = alfabet[alfabet.find(word[i]) + encrypt ]

print(''.join(word))
