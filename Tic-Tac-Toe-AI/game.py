'''
Author: Rohit Kumar Bindal
Data: 21/04/2020
Timestamp: 13:02:57

This file contains a console based implementation of Tic Tac Toe using the MINIMAX Algorithm.

Important: By default, the user is set to go first. But, AI can be set to go first by uncommenting
the game.AI() method call on line:201 in main() function. However, it might take a few moments to get an 
output if the AI goes first.

'''


import numpy as np

class Game:
    def __init__(self):
        #initializing the board and giving AI the first chance to play.
        self.board = np.array(['_']*9)
        self.board = np.reshape(self.board, (3,3))
        self.ai = 'X'
        self.human = 'O'
        self.player = self.ai
        # A score dictionary to help with the MINIMAX.
        self.scores = {'X': 10, 'O': -10, 'TIE': 0}

    
    # Display the board.
    def getBoard(self):
        print(self.board)

    
    # Check if there is space on the board or not.
    def hasSpace(self):
        return '_' in self.board
        
        
    # Check if the current location is available.
    def checkLocation(self, x, y):
        return self.board[x][y] == '_'


    # Function to check if a player has won or the game is a tie.
    def checkState(self, board):
        # Check for a winner
        if self.verticalVictory(board) or self.horizontalVictory(board) or self.diagonalVictory(board):
            return self.winner
        # If there is no winner and also the board is full
        if not self.hasSpace():
            return 'TIE'
    
    
    def equals(self, a, b, c):
        return a == b and b == c and a != '_'


    # Funtion to check vertical combinations.
    def verticalVictory(self, state):
        # state = self.board
        for index in range(3):
            if self.equals(state[0][index], state[1][index], state[2][index]):
                self.winner = state[0][index]
                return True
        return False


    # Function to check horizontal combinations.
    def horizontalVictory(self, state):
        for index in range(3):
            if self.equals(state[index][0], state[index][1], state[index][2]):
                self.winner = state[index][0]
                return True
        return False


    # Function to check for diagonal wins.
    def diagonalVictory(self, state):
        diagonal1 = self.equals(state[0][0], state[1][1], state[2][2])
        diagonal2 = self.equals(state[0][2], state[1][1], state[2][0])
        if diagonal1:
            self.winner = state[0,0]
            return True
        elif diagonal2:
            self.winner = state[0,2]
            return True
        
        return False


    # Function to add the current input to the board.
    def addToBoard(self, x, y):
        # If the location is available, update the board, check 
        # for winner and call AI.
        if self.checkLocation(x, y):
            self.board[x][y] = self.player
            result = self.checkState(self.board)
            if result != None:
                if result == 'TIE':
                    print("It's a TIE!")
                    exit()
                print('{} WON!!'.format(result))
                exit()
            self.player = self.ai
            self.AI()
            self.getBoard()
            
        # If the location is not available, try again.
        else:
            print('This location is not available. Try Again!!')
            self.getUserInput()

    
    # Get coordinates for O's turn.
    def getUserInput(self):
        userInput = input('Enter the coordinates for player O (comma separated):').split(",")
        x = int(userInput[0])
        y = int(userInput[1])
        # Set the current player as human ,i.e., O.
        self.player = self.human
        self.addToBoard(x, y)
    

    # IMPLEMENTATION OF MINIMAX ALGORITHM TO GET THE BEST POSSIBLE SCORE.
    def AI(self):
        optimalScore = np.NINF  # Let's set our optimal score to -infinity.
        x, y = 0, 0
        for i in range(3):
            for j in range(3):
                # Check if the location is available.
                if self.checkLocation(i,j):
                    # Update the board temporarily to apply MINIMAX.
                    self.board[i][j] = self.ai
                    # Call the MINIMAX function to generate all the possible outcomes for 
                    # the above updated board.
                    score = self.MINIMAX(self.board, 0, False)
                    # Reset the board to previous state.
                    self.board[i][j] = '_'
                    # if the acheived score is better than optimascore, store the locations
                    # and score values.
                    if score > optimalScore:
                        optimalScore = score
                        x, y = i, j
        # Once we have iterated through all the empty spots, give the best spot on the board
        # to AI, i.e., X
        self.board[x][y] = self.ai
        self.player = self.human
        # Reset winner, because while we are recursively calling the MINIMAX functions, it will
        # eventually reach a terminal point and get a winner. We don't want that temporary 
        # values to be decisive in the main game.
        self.winner = None



    # MINIMAX ALGORITHM
    def MINIMAX(self, board, depth, isMax):
        
        # Check if we are in the terminal state, i.e., one or the other player
        # has won. This will update the winner enitity of the class, we will reset
        # it after the function is terminated.
        winner = self.checkState(board)
        if winner != None:
            return self.scores[winner]

        # Get the max score for the maximizing player. In our case -> X.
        if isMax:
            # Initialize the best score as -infinity.
            bestScore = np.NINF
            for i in range(3):
                for j in range(3):
                    # Check if the location is available.
                    if self.checkLocation(i, j):
                        self.board[i][j] = self.ai
                        score = self.MINIMAX(board, depth + 1, False)
                        self.board[i][j] = '_'
                        bestScore = max(score, bestScore)
            return bestScore

        # Get the minimum score for the minimizing player. In our case -> O.
        else:
            # Initialize the best score as infinity.
            bestScore = np.Infinity
            for i in range(3):
                for j in range(3):
                    # Check if the location is available.
                    if self.checkLocation(i, j):
                        board[i][j] = self.human
                        score = self.MINIMAX(board, depth + 1, True)
                        board[i][j] = '_'
                        bestScore = min(score, bestScore)
            return bestScore


# Driver Code.
def main():
    RUN = True
    game = Game()
    # If we want the AI to go first, we'll just uncomment the line below. It may take a few seconds to 
    # get an output because the minimax algorithm is generating all the possible outcomes. 
    # Here, we'll get a tree with 2*(2^9)-1 nodes -> 1023 nodes.
    
    # game.AI()

    game.getBoard()
    while RUN:
        game.getUserInput()
        # Check for the result.
        result = game.checkState(game.board)
        if result != None:
            if result == 'TIE':
                print("It's a TIE!")
                exit()
            print('{} WON!!'.format(result))
            exit()


if __name__ == "__main__":
    main()