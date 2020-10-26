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

        #print(self.total_throws) #Debug

    def check_board (self):
        for point in self.Points:
            distance = self.calc_distance(point.x, point.y)
            if self.in_circle(distance):
                self.hits += 1
                point.hit = True
            else:
                self.misses += 1
                point.hit = False
        self.hit_ratio = self.hits / self.total_throws

    def calc_distance(self, x,y):
        return math.sqrt(abs(x**2) + abs(y**2))

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

        #The reason the hit ratio multiplied by 4 gives us something close to pi is because...
        #What we are doing is getting the ratio in which one dart will hit the dart board.
        #Imagine dividing the board into 4 pieces the ratio we get will apply to all four of the pieces
        #Multiplying the ratio with 4 will instead give us the ratio between the diameter and the distance around the circle
        #Note: Even when changing the radius the answer still gets close to pi
        print("Hit radio multiplied by 4: ", self.hit_ratio * 4) 
    
    def convert_point_to_dart(self, points):
        darts = []

        for point in points:
            if point.hit:
                darts.append(plt.Circle((point.x,point.y), radius=0.01, linewidth=1, color="Green", zorder=0))
            else:
                darts.append(plt.Circle((point.x,point.y), radius=0.01, linewidth=1, color="Red", zorder=0)) 
        
        return darts

    def add_darts_to_board(self, axes, darts):
        for dart in darts:
            axes.add_patch(dart)

    def set_graph_options(self):
        plt.axis("scaled")
        plt.title("Board")
        plt.grid()

    def display_board(self):
        axes = plt.gca() #Setup axis

        dart_board = plt.Circle((0,0), radius=self.circle_radius, fill=False, linewidth=3, zorder=1) # Set dart board
        axes.add_patch(dart_board)

        darts = self.convert_point_to_dart(self.Points)
        self.add_darts_to_board(axes, darts)

        self.set_graph_options()

        plt.show()

class Point:
    x: int
    y: int
    hit = False

    def __init__ (self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)

board = Board(10000)
board.check_board()
board.results()
board.display_board()

