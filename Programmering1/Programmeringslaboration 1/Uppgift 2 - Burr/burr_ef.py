import random

class Iterator:
    start: int
    end: int
    
    def __init__(self):
        self.take_input()

    def take_input(self):
        #Takes input and checks if it's acceptable if not have the user try again.
        try:
            self.start = int(input("Start värde: "))
            self.end = int(input("Slut värde: "))
            self.end += 1

            if (self.end < self.start):
                print("Error: No iterating backwards!")
                self.take_input()
        except:
            print("Error: That was not a positive whole number!")
            self.take_input()

print("-Input positive whole numbers to iterate upon -")
iterator = Iterator() #Initialize the iterator object

for number in range(iterator.start, iterator.end):
    burr = number % 5 == 0
    birr = number % 3 == 0

    output = "Burr Birr" if burr and birr else "burr" if burr else "birr" #Sets the variable output to either Burr or Birr or both.

    if burr or birr: 
        print(output) 
    else:
        print(number)


#F Note: Man skulle kunna kontrollera ifall det användaren skriver in är okej
# Vi kan använda oss av en try och except för att lösa detta

