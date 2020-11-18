sentence = "Do not worry about your difficulties in Mathematics. I can assure you mine are still greater."
sentence = sentence.lower()

eng_vowels = ["a", "o", "u", "e", "i"]
total_vowels = 0

for vowel in eng_vowels:
    total_vowels += sentence.count(vowel) 

print(f"The sentence has {total_vowels} vowels")

