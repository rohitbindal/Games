import numpy as np

class Game:
    def __init__(self):
        #Initializing the board.
        self.board = np.array(['']*9)
        self.board = np.reshape(self.board, (3,3))
        self.ai = 'X'
        self.human = 'O'
        self.player = self.ai
        # A score dictionary to help with our algorithm.
        self.scores = {'X': 10, 'O': -10, 'TIE': 0}

    
    # Display the board.
    def getBoard(self):
        print(self.board)

    
    # Check if there is space on the board or not.
    def hasSpace(self):
        return '' in self.board
        
        
    # Check if the current location is available.
    def checkLocation(self, x, y):
        return self.board[x][y] == ''


    # Function to check if a player has won or the game is a tie.
    def checkState(self, board):
        # Check for a winner
        if self.verticalVictory(board) or self.horizontalVictory(board) or self.diagonalVictory(board):
            return self.winner
        # If there is no winner and also the board is full
        if not self.hasSpace():
            return 'TIE'
    
    
    def equals(self, a, b, c):
        return a == b and b == c and a != ''


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
        # Update the board# Check for a winner, if the game is not yet completed, call the AI.
        self.player = self.human
        self.board[x][y] = self.player

        result = self.checkState(self.board)
        if result != None:
            self.printResult(result)
        
        self.player = self.ai
        self.AI()
        self.getBoard()

    
    # Get coordinates for O's turn.
    def getUserInput(self):
        userInput = input('Enter the coordinates for player O (comma separated):').split(",")
        x = int(userInput[0])
        y = int(userInput[1])
        # Set the current player as human ,i.e., O.
        self.player = self.human
        self.addToBoard(x, y)
    

    # IMPLEMENTATION OF ALPHA BETA PRUNING ALGORITHM TO GET THE BEST POSSIBLE SCORE.
    def AI(self):
        optimalScore = np.NINF  # Let's set our optimal score to -infinity.
        x, y = 0, 0
        for i in range(3):
            for j in range(3):
                # Check if the location is available.
                if self.checkLocation(i,j):
                    # Update the board temporarily to apply ALPHA-BETA Pruning.
                    self.board[i][j] = self.ai
                    # Call the ALPHA_BETA function to generate all the possible outcomes for 
                    # the above updated board and prune all the states that are not required.
                    # we set the value of alpha and beta for the worst case scenarios, i.e., -infinity
                    # for alpha and infinity for beta.
                    score = self.ALPHA_BETA(self.board, np.NINF, np.Inf, 0, False)
                    # Reset the board to previous state.
                    self.board[i][j] = ''
                    # if the acheived score is better than optimascore, store the locations
                    # and score values.
                    if score > optimalScore:
                        optimalScore = score
                        x, y = i, j
        # Once we have iterated through all the empty spots, give the best spot on the board
        # to AI, i.e., X
        self.board[x][y] = self.ai
        self.player = self.human
        # Reset winner, because while we are recursively calling the ALPHA_BETA functions, it will
        # eventually reach a terminal point and get a winner. We don't want that temporary 
        # values to be decisive in the main game.
        self.winner = None



    # ALPHA BETA PRUNING
    def ALPHA_BETA(self, board, alpha, beta, depth, isMax):
        
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
                        score = self.ALPHA_BETA(board, alpha, beta, depth + 1, False)
                        self.board[i][j] = ''
                        bestScore = max(score, bestScore)
                        # getting the best value for alpha, in this case, the greater value
                        # between alpha and our betscore
                        alpha = max(alpha, bestScore)
                        if alpha >= beta:
                            break
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
                        score = self.ALPHA_BETA(board, alpha, beta, depth + 1, True)
                        board[i][j] = ''
                        bestScore = min(score, bestScore)
                        # getting the best value for alpha, in this case, the smaller value
                        # between alpha and our betscore
                        alpha = min(alpha, bestScore)
                        if alpha >= beta:
                            break
            return bestScore

    
    # Function to print the result of the game.
    def printResult(self, result):
        # If the game is TIE.
            if result == 'TIE':
                print("\nWell, atleast you didn't loose. Cause that would be embarrassing.\n\n")
                exit()
            # If the computer wins.
            if result == 'X':
                print("\nYou really suck at this game my friend.\n\n")
                exit()
            # The 3 lines below are never excecuted. If they get excecuted, well, that means you are
            # very intelligent.
            if result == 'O':
                print("\nCongrats!! You broke the game -- \n\n")
                exit()