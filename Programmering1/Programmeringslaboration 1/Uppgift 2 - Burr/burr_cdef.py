import random

class Handler:
    iterator_start: int
    iterator_end: int

    chosen_burr: int
    chosen_birr: int

    def __init__ (self):
        print("-Input whole numbers to iterate upon-")
        self.set_iterator_values() 

        print("-Input whole numbers for Burr and Birr-")
        self.set_burrbirr_values()

    def set_iterator_values(self):
        #Takes input and checks if it's acceptable if not have the user try again.
        try:
            self.iterator_start = int(input("Start värde: "))
            self.iterator_end = int(input("Slut värde: "))
            self.iterator_end += 1
            
            if (self.iterator_end < self.iterator_start):
                print("Error: No iterating backwards!")
                self.set_iterator_values()
        except:
            print("Error: That was not a whole number!")
            self.set_iterator_values()

    def set_burrbirr_values (self):
         #Takes input and checks if it's acceptable if not have the user try again.
        try:
            self.chosen_burr = int(input("Set Burr: "))
            self.chosen_birr = int(input("Set Birr: "))
        except:
            print("Error: That was not a whole number")
            self.set_burrbirr_values()
       


handler = Handler() #Initialize the Handler object

for number in range(handler.iterator_start, handler.iterator_end):
    burr = number % handler.chosen_burr == 0
    birr = number % handler.chosen_birr == 0

    output = "Burr Birr" if burr and birr else "burr" if burr else "birr" #Sets the variable output to either Burr or Birr or both.

    if burr or birr: 
        print(output) 
    else:
        print(number)


#F Note: Man skulle kunna kontrollera ifall det användaren skriver in är okej
# Vi kan använda oss av en try och except för att lösa detta

