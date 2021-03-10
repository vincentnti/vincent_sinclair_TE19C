translator = {}
with open('morse.txt', 'r+') as file:
    for line in file:
        line = line.replace('\n', '')
        translator[line[0]] = line[3::]

def translate(string):
    translated = ''
    for char in string:
        if char != ' ':
            translated += translator[char.upper()]
    return translated
        
print('Type the text you wish to convert into Morse Code')
input_string = input("Text: ")
print(translate(input_string))