kurser = {
    'Matte' : 100,
    'Engelska' : 100,
    'Svenska' : 100,
    'Programmering' : 100,
    'Webbutveckling' : 100,
    'Fysk' : 150,
    'Daodac' : 100,
    'Idrott' : 100
}

result = 0
for key, item in kurser.items():
   result += item 

print(result)