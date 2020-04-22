# import numpy as np
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

    # If you want to be the first to go, comment line:28

    game.AI()
    game.getBoard()
    while RUN:

        x, y = getUserInput(game)
        game.addToBoard(x, y)

        # Check for the result.
        result = game.checkState(game.board)
        if result != None:
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
                print("\nCongrats!! You broke the game -_- \n\n")
                exit()


if __name__ == "__main__":
    main()