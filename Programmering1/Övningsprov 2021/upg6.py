"""
Lista multiplikations problem random
Låt användaren sätta svårehetsgrad alltså tid
countdown
score
title screen maybe


classer
"""

#Not done here yet

import sys
import random
import time
from threading import Thread #For use with timer

class Game:
    score = 0
    answered = 0
    timer: classmethod

    def __init__ (self):
        self.timer = Timer() #This works but idk if it's the best way to do it might be better to set it direcly or approuching it some other way
        #Title thingy? Press Start etc
        self.setup() #Gameplay settings setup
        self.play_game()
        #self.start_game() etc

    def setup (self):
        print("Set time limit for each problem!")
        time_limit = int(input("Time Limit: "))
        self.timer.set_timer(time_limit)

        print("Ready to start?")
        if input("(Y/n): ") == "n":
            self.exit_game()

    def play_game (self):        
        self.timer.start_timer()

        while True:
            problem = Problem()
            print("What is: ", problem.Text)

            if problem.Answer == int(input("Answer: ")):
                print("Nice job! Next question,")
                self.timer.reset_timer()
                self.calc_score()
            else:
                print("Correct answer was:", problem.Answer)
                print("What was that? Game over!")
                self.exit_game()
            
            if self.timer.time_left < 1:
                print("You ran out of time before you managed to answer! Game over!")
                self.exit_game()


    def calc_score(self):
        self.answered += 1
        self.score += self.timer.time_left #Placeholder score will be calc using time left for each question

    def exit_game(self):
        print("Score:", self.score, "Questions Answered:", self.answered)
        sys.exit(0)
    
class Timer:
    time_limit = 0
    time_left = 0

    def set_timer (self, time):
        self.time_limit = time
        self.time_left = self.time_limit

    def start_timer (self):
        clock = Thread(target=self.timer)
        clock.daemon = True #Allows us too exit the program while this is active
        clock.start()
        
    def reset_timer (self):
        self.time_left = self.time_limit

    def timer (self):
        while self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            print("Time left:", self.time_left, end="\r") #Not required to print this out but it would be fun

    

class Problem:
    Text = ""
    Answer: int
    def __init__ (self):
        x = random.randint(0,10)
        y = random.randint(0,10)

        self.Text = str(x) + " * " + str(y)
        self.Answer = x * y
        
game = Game()
