import numpy as np

class Game:
    def __init__(self):
        # Initializing the board
        self.board = np.array(['_']*9)
        self.board = np.reshape(self.board, (3,3))
    

    # Funtion to add the current input to the board.
    def addToBoard(self, x, y, currPlayer):
        # if the location is free, update the board and check for a winner.
        if self.isLocFree(x, y):
            self.board[x][y] = currPlayer
            self.hasWon(currPlayer)
        # If the location is not available
        else:
            print("This location is not available. Try Again!")
            self.getUserInput(currPlayer)

        
    
    # Function to check if the user entered location is free or not.
    def isLocFree(self, x, y):
        return self.board[x][y] == '_'

    
    # Function to check if the board is empty or not.
    def isEmpty(self):
        return '_' in self.board


    # Function to check if a player wins.
    def hasWon(self, player):
        arr = self.board
        
        # Check for the winner.
        if self.isDiagonal(player) or self.isHorizontal(player) or self.isVertical(player):
            self.getBoard()
            print('{} Won!!'.format(player))
            exit()
        
        # If the board is full and no one wins.
        if not self.isEmpty():
            self.getBoard()
            print('No Outcome')
            exit()

    
    # Check for a horizontal combination.
    def isHorizontal(self, player):
        arr = self.board
        for i in range(3):
            if arr[i][0] == arr[i][1] == arr[i][2] == player:
                return True
        return False

    
    # Check for a vertical combination.
    def isVertical(self, player):
        arr = self.board
        for i in range(3):
            if arr[0][i] == arr[1][i] == arr[2][i] == player:
                return True
        return False
    
    
    # Check for a diagonal combination.
    def isDiagonal(self, player):
        arr = self.board
        if arr[0][0] == arr[1][1] == arr[2][2] == player or arr[0][2] == arr[1][1] == arr[2][0] == player:
            return True
        return False


    # Get the current state of the board.
    def getBoard(self):
        print(self.board)


    # Function to get user input.
    def getUserInput(self, player):
        x, y = map(int, input('Enter the coordinates for player {} (comma separated):'.format(player)).split(","))
        self.addToBoard(x,y,player)

game = Game()
RUN = True
player1 = 'X'
player2 = 'O'
game.getBoard()
while RUN:
    X = 1
    O = 0
    if X == 1:
        game.getUserInput(player1)
        X = 0
        O = 1
        game.getBoard()
    if O == 1:
        game.getUserInput(player2)
        X = 1
        O = 0
        game.getBoard()