#TicTacToe
import random

random.seed() # Set new seed for a real random experience
grid = [1,2,3,4,5,6,7,8,9] # Board positions
playerOneMark = "X"
playerTwoMark = "O"
def drawBoard():
    print("—————————————————————————")
    print(f"|   {grid[0]}   |   {grid[1]}   |   {grid[2]}   |")
    print("—————————————————————————")
    print(f"|   {grid[3]}   |   {grid[4]}   |   {grid[5]}   |")
    print("—————————————————————————")
    print(f"|   {grid[6]}   |   {grid[7]}   |   {grid[8]}   |")
    print("—————————————————————————")

def isMovePossible(placePos):
    if grid[placePos] != playerOneMark and grid[placePos] != playerTwoMark:
        return True
    else: 
        return False

def makeMove ():
    placePos = int(input("Choose available grid position: "))
    if isMovePossible(placePos - 1) != True:
        makeMove()
        return
    placePos -= 1
    grid[placePos] = playerOneMark

def computerMove ():
    placePos = random.randint(1,9)
    if isMovePossible(placePos - 1) != True:
        computerMove()
        return
    placePos -= 1
    grid[placePos] = playerTwoMark

def hasWon():
    #Check if there are three in a row then return true or false
    rows = [f"{grid[0]}{grid[1]}{grid[2]}", f"{grid[3]}{grid[4]}{grid[5]}", f"{grid[6]}{grid[7]}{grid[8]}", f"{grid[0]}{grid[4]}{grid[8]}", f"{grid[2]}{grid[4]}{grid[6]}", f"{grid[0]}{grid[3]}{grid[6]}", f"{grid[1]}{grid[4]}{grid[7]}", f"{grid[2]}{grid[5]}{grid[8]}"]
    for i in rows:
        #print(i) #See row values
        if i == playerOneMark * 3:
            print("You Win!")
            return True
        elif i == playerTwoMark * 3:
            print("You Lose!")
            return True

#Methods/Function order
drawBoard()
while hasWon() != True:
    makeMove()
    computerMove()
    drawBoard()