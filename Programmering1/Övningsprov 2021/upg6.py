"""
Lista multiplikations problem random
Låt användaren sätta svårehetsgrad alltså tid
countdown
score
title screen maybe


classer
"""
import random

class Game:
    time_limit: int

    def __init__ (self):
        #Title thingy? Press Start etc
        #Clear screen function is prob needed
        self.setup() #Gameplay settings setup
        #self.start_game() etc
    def setup (self):
        print("Set time limit for each problem!")
        self.time_limit = int(input("Time Limit: "))
        print("Ready to start?")
        if input("(Y/n): ") == "n":
            exit()
            #self.exit_game() etc ? Might have this
            #Move you back to the title screen or smt

class Problem:
    Text = ""
    Answer: int
    def __init__ (self): #Should is set everything this way?
        x = random.randint(0,10)
        y = random.randint(0,10)

        self.Text = str(x) + " * " + str(y)
        self.Answer = x * y

    def create_problem(self): #Or this way, latter worked doe but idk
        x = random.randint(0,10)
        y = random.randint(0,10)

        self.Text = str(x) + " * " + str(y)
        self.Answer = x * y
        

game = Game()

"""
thing = Problem()
thing.create_problem()
print(thing.Answer)
print(thing.Text)
"""
"""
while True:
    problem = Problem()
    print(problem.Text, problem.Answer)
"""