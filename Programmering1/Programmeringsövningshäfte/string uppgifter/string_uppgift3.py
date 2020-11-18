#a)
"""
word = input("Input: ")
word = word.lower()
if word == word[::-1]:
    print(f"{word} is a palindrome")
"""
#b)
words = input("Input: ")
old_words = words

words = words.lower()
olagliga_tecken = [" ", ",", ".", "/", "-", "*", "!", "?"]
for tecken in olagliga_tecken:
    words = words.replace(tecken, "")

print(words)
if words == words[::-1]:
    print(f"\"{old_words}\" is a palindrome")