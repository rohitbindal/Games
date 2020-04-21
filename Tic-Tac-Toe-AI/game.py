import numpy as np

class Game:
    def __init__(self):
        #initializing the board
        self.board = np.array(['_']*9)
        self.board = np.reshape(self.board, (3,3))

    
    # Display the board:
    def getBoard(self):
        print(self.board)

    
    # Check if there is space on the board or not.
    def hasSpace(self):
        return '_' in self.board
        
    
    # Check if the current location is available.
    def checkLocation(sels, x, y):
        return self.board[x][y] == '_'


    # Function to check if a player has won or the game is a tie.
    def checkState(self, player):
        state = self.board

        # Check for a winner
        if self.verticalVictory(player) or self.horizontalVictory(player) or self.diagonalVictory(player):
            self.getBoard()
            print('{} WON!!'.format(player))
            exit()

        # If there is no winner and also the board is full:
        if not self.hasSpace():
            self.getBoard()
            print("It's a TIE!")
            exit()


    # Funtion to check vertical combinations
    def verticalVictory(self, player):
        state = self.board
        for index in range(3):
            if state[0][index] == state[1][index] == state[2][index] == player:
                return True
        return False


    # Function to check horizontal combinations
    def horizontalVictory(self, player):
        state = self.board
        for index in range(3):
            if state[index][0] == state[index][1] == state[index][2] == player:
                return True
        return False


    # Function to check for diagonal wins
    def diagonalVictory(self, player):
        state = self.board
        diagonal1 = state[0][0] == state[1][1] == state[2][2] == player
        diagonal2 = state[0][2] == state[1][1] == state[2][0] == player
        return diagonal1 or diagonal2
