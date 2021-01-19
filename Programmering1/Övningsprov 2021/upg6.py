"""
Todo list:
---------
Lista multiplikations problem random CHECK
Låt användaren sätta svårehetsgrad alltså tid CHECK
countdown CHECK 
score CHECK
title screen CHECK
classer CHECK

Optional extras:
Live countdown
Set timer instance as attribute directly if that is possible
"""
import sys
import random
import time
from threading import Thread #For use with timer

class Game:
    score = 0
    answered = 0
    timer: classmethod

    def __init__ (self):
        self.timer = Timer()
        self.print_title()
        self.setup()
        self.play_game()

    def print_title(self):
        title = """
        :::   :::   :::    ::: :::    ::::::::::: ::::::::::: :::::::::     :::     ::::::::::: ::::    ::: 
      :+:+: :+:+:  :+:    :+: :+:        :+:         :+:     :+:    :+:  :+: :+:       :+:     :+:+:   :+:  
    +:+ +:+:+ +:+ +:+    +:+ +:+        +:+         +:+     +:+    +:+ +:+   +:+      +:+     :+:+:+  +:+   
   +#+  +:+  +#+ +#+    +:+ +#+        +#+         +#+     +#++:++#+ +#++:++#++:     +#+     +#+ +:+ +#+    
  +#+       +#+ +#+    +#+ +#+        +#+         +#+     +#+       +#+     +#+     +#+     +#+  +#+#+#     
 #+#       #+# #+#    #+# #+#        #+#         #+#     #+#       #+#     #+#     #+#     #+#   #+#+#      
###       ###  ########  ########## ###     ########### ###       ###     ### ########### ###    ####
            """
        print(title)       

    def setup (self):
        print("Set time limit for each problem!")
        time_limit = int(input("Time limit (in seconds): "))
        self.timer.set_timer(time_limit)

        if input("Ready to start [Y/n]!? ") == "n":
            self.exit_game()

    def play_game (self):        
        prompt = Thread(target=self.get_answer)
        prompt.daemon = True #Allows us too exit the program while this is active
        prompt.start()
        while True:
            if self.timer.times_up:
                print("\nYou ran out of time before you managed to answer! Game over!")
                self.exit_game()
            else:
                time.sleep(0.1)

    def get_answer(self):
        self.timer.start_timer()

        while True:
            problem = Problem()
            
            print(f"What is {problem.Text}?")

            if problem.Answer == int(input("Answer: ")):
                print("Nice job! Next question,")
                self.timer.reset_timer()
                self.calc_score()
            else:
                print("Correct answer was:", problem.Answer)
                print("What was that? Game over!")
                self.exit_game()

    def calc_score(self):
        self.answered += 1
        self.score += self.timer.time_left * (self.timer.time_limit**-1 + 1)
    def exit_game(self):
        print("Score:", self.score, "Questions Answered:", self.answered)
        sys.exit(0)
    
class Timer:
    time_limit = 0
    time_left = 0
    times_up = False

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
            print("Hello")
            print("\033[%d;%dH" % (1,1))
        self.times_up = True

class Problem:
    Text = ""
    Answer: int
    def __init__ (self):
        x = random.randint(0,10)
        y = random.randint(0,10)

        self.Text = str(x) + " * " + str(y)
        self.Answer = x * y
        
game = Game()
