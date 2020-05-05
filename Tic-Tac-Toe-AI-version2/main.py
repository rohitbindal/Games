'''
Author: Rohit Kumar Bindal
Data: 22/04/2020
Timestamp: 19:34:57

This file contains a console based implementation of Tic Tac Toe using Alpha Beta Pruning.
The Algorithm itself is in a separate file named board.py which also contains the definition of
the tic tac toe board.

Important: By default, the AI is set to go first. But, user can be set to go first by commenting
the game.AI() method call on line:39 in main() function.

'''

import board


def getUserInput(game):
    print('Enter the coordinates for player O (comma separated):')
    
    input_ = True
    # If the recieved location is free, carry ahead, if not, get the user input again.
    while input_:
        userInput = input().split(",")
        x = int(userInput[0])
        y = int(userInput[1])
        if game.checkLocation(x,y):
            return x, y
        else:
            print('This location is not available. Remember, the values should be comma separated. Try Again')
    

# Driver Code.
def main():
    
    RUN = True
    game = board.Game()
    # If you want the AI to be the first to go, uncomment line:39
    game.AI()
    game.getBoard()
    while RUN:

        x, y = getUserInput(game)
        game.addToBoard(x, y)
        game.getBoard()
        # Check for the result.
        result = game.checkState(game.board)
        if result != None:
            game.printResult(result)


if __name__ == "__main__":
    main()