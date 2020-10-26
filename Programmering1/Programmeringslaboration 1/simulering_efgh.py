import math
import random
import matplotlib.pyplot as plt

class Board:
    circle_radius = 1

    Points = []
    
    hits = 0
    misses = 0
    total_throws = 0
    hit_ratio = 0.0

    def __init__ (self, throw_amount):
        for _ in range(0, throw_amount):
            self.Points.append(Point())
        self.total_throws = throw_amount

        print(self.total_throws) #Debug

    def check_board (self):
        for point in self.Points:
            distance = self.calc_distance(point.x, point.y)
            if self.in_circle(distance):
                self.hits += 1
                point.hit == True
            else:
                self.misses += 1
                point.hit == False
        self.hit_ratio = self.hits / self.total_throws

    def calc_distance(self, x,y):
        return math.sqrt(x**2 + y**2)

    def in_circle(self, distance):
        if distance <= self.circle_radius:
            return True
        else:
            return False
    
    def results (self):
        print("Total Throws: ", self.total_throws)
        print("Hits: ", self.hits)
        print("Misses: ", self.misses)
        print("Hit ratio: ", self.hit_ratio, "%")

        #The reason the hit ratio multiplied by 4 gives us something close to pi is because of...
        print("Hit radio multiplied by 4: ", self.hit_ratio * 4) 
    
    def display_board(self):
        plt.Circle((0,0), self.circle_radius)
        for point in self.Points:
            if point.hit:
                circle = plt.Circle((point.x, point.y), 0.1, color="green")
            else:
                circle = plt.Circle((point.x, point.y), 0.1, color="red")
        plt.title("potato")
        fig, ax = plt.subplots()
        ax.add_artist(circle)
        plt.show()
class Point:
    x: int
    y: int
    hit = False

    def __init__ (self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)

random.seed() #Idk if necessary prob not (gonna remove it later)

board = Board(1000000)
board.check_board()
board.results()
board.display_board()

