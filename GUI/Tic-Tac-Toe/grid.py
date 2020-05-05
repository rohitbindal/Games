import pygame
import numpy as np


class Grid:
    def __init__(self, width, height, window):
        self.game_window = window  # Game Window
        self.WIDTH = width  # Width of game window
        self.HEIGHT = height  # Height of game window
        self.relative_dimension = width // 3  # Dimension relative to the width of the screen

        # Player Images based on screen size
        if self.WIDTH <= 400:
            self.playerX = pygame.image.load('assets/images/player_s/x.png')  # Image of X
            self.playerO = pygame.image.load('assets/images/player_s/o.png')  # Image of O
            self.PLAYER_WIDTH = 32
        elif self.WIDTH <= 700:
            self.playerX = pygame.image.load('assets/images/player_m/x_m.png')  # Image of X
            self.playerO = pygame.image.load('assets/images/player_m/o_m.png')  # Image of O
            self.PLAYER_WIDTH = 50
        else:
            self.playerX = pygame.image.load('assets/images/player_l/x_l.png')  # Image of X
            self.playerO = pygame.image.load('assets/images/player_l/o_l.png')  # Image of O
            self.PLAYER_WIDTH = 70

        # VISIBLE GRID
        self.grid_lines = [
            ((self.WIDTH // 3, 10), (self.WIDTH // 3, self.HEIGHT - 10)),  # Vertical line 1
            (((self.WIDTH // 3) * 2, 10), ((self.WIDTH // 3) * 2, self.HEIGHT - 10)),  # Vertical line 2
            ((10, self.HEIGHT // 3), (self.WIDTH - 10, self.HEIGHT // 3)),  # Horizontal line 1
            ((10, (self.HEIGHT // 3) * 2), (self.WIDTH - 10, (self.HEIGHT // 3) * 2))  # Horizontal line 2
        ]

        # Fonts used
        self.FONT_1 = pygame.font.Font('assets/fonts/IndieFlower-Regular.ttf', self.WIDTH // 7)
        self.FONT_2 = pygame.font.Font('assets/fonts/IndieFlower-Regular.ttf', self.WIDTH // 20)
        self.FONT_3 = pygame.font.Font('assets/fonts/IndieFlower-Regular.ttf', self.WIDTH // 24)

        # Initializing the board.
        self.board = np.array([''] * 9)
        self.board = np.reshape(self.board, (3, 3))
        self.ai = 'O'
        self.human = 'X'
        self.player = self.ai  # Current Player
        self.winner = None
        self.scores = {'X': -10, 'O': 10, 'TIE': 0}  # A score dictionary to help with our algorithm.

    """ GUI Functions """

    # Draw the GRID on screen
    def draw_grid(self):
        for line in self.grid_lines:
            pygame.draw.line(self.game_window, (0, 0, 0), line[0], line[1], 2)

    # Draw the current on Game Board
    def draw_on_board(self, row, col, player):
        # Get the dimensions of a grid element.
        corner_1_x = row * self.relative_dimension
        corner_1_y = col * self.relative_dimension
        # Calculate the location of image by placing the image at the center of grid element.
        corner_2_x = (corner_1_x + self.relative_dimension // 2) - self.PLAYER_WIDTH
        corner_2_y = (corner_1_y + self.relative_dimension // 2) - self.PLAYER_WIDTH
        # Draw the player on the board.
        if player == 'X':
            self.game_window.blit(self.playerX, (corner_2_y, corner_2_x))
        else:
            self.game_window.blit(self.playerO, (corner_2_y, corner_2_x))

    # Print the result on Game Screen
    def game_over(self, result):
        TEXT = {'o_wins': 'YOU LOST!! XD',
                'tie': 'It\'s a TIE.',
                'retry': 'Wanna give it another go? Hit Enter',
                'exit': 'If you are scared, press Esc or Right mouse to leave.'}

        if result == 'O':
            # render the font
            winnerO = self.FONT_1.render(TEXT['o_wins'], True, (0, 0, 0), (128, 128, 128))
            # Get the rectangle text box
            winnerO_rect = winnerO.get_rect()
            # set the center of the text box to a location
            winnerO_rect.center = (self.WIDTH // 2, self.HEIGHT // 3)
            # Draw the text on GAME WINDOW
            self.game_window.blit(winnerO, winnerO_rect)
        else:
            tie_text = self.FONT_1.render(TEXT['tie'], True, (0, 0, 0), (128, 128, 128))
            tie_text_rect = tie_text.get_rect()
            tie_text_rect.center = (self.WIDTH // 2, self.HEIGHT // 3)
            self.game_window.blit(tie_text, tie_text_rect)

        retry_text = self.FONT_2.render(TEXT['retry'], True, (0, 0, 0), (128, 128, 128))
        retry_text_rect = retry_text.get_rect()
        retry_text_rect.center = (self.WIDTH // 2, self.HEIGHT // 2)
        self.game_window.blit(retry_text, retry_text_rect)

        exit_text = self.FONT_3.render(TEXT['exit'], True, (0, 0, 0), (128, 128, 128))
        exit_text_rect = exit_text.get_rect()
        exit_text_rect.center = (self.WIDTH // 2, self.HEIGHT - 20)
        self.game_window.blit(exit_text, exit_text_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                # Check for keyboard key press events
                if event.type == pygame.KEYDOWN:
                    # If Enter key is pressed, return to game intro.
                    if event.key == pygame.K_RETURN:
                        return True
                    # If escape key is pressed, exit the game
                    if event.key == pygame.K_ESCAPE:
                        exit()
                # Check for mouse events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if Right MouseButton is pressed, exit the game
                    if pygame.mouse.get_pressed()[2] == 1:
                        exit()
                    return True
            pygame.display.update()

    """UTILITY FUNCTIONS"""

    # Check if there is space on the board or not.

    def has_space(self):
        return '' in self.board

    # check if a given location is empty
    def check_location(self, x, y):
        return self.board[x][y] == ''

    @staticmethod
    def equality(a, b, c):
        return a == b and b == c and a != ''

    # Function to check if a player has won or the game is a TIE.
    def check_state(self, board):
        # Check for a winner
        if self.vertical_victory(board) or self.horizontal_victory(board) or self.diagonal_victory(board):
            return self.winner
        # If there is no winner and also the board is full
        if not self.has_space():
            return 'TIE'

    # Function to add current player on the board.
    def add_to_board(self, x, y):
        # Update the board
        self.player = self.human
        self.board[x][y] = self.player
        self.draw_on_board(x, y, self.player)
        # Change the current to AI
        self.player = self.ai
        # Calculate the appropriate position
        comp_x, comp_y = self.AI()
        # Draw AI -> O on Board
        self.draw_on_board(comp_x, comp_y, self.ai)

    # Function to print the result of the game.
    # @staticmethod
    # def print_result(result):
    #     # If the game is TIE.
    #     if result == 'TIE':
    #         print("Well, at least you didn't loose.\n")
    #     # If the computer wins.
    #     if result == 'O':
    #         print("You really suck at this game my friend.\n")
    #     # The 3 lines below are never executed. If they get executed, well, that means you BROKE
    #     # THE GAME.
    #     if result == 'X':
    #         print("CONGRATS!! YOU BROKE THE GAME -_- . \n")

    """ FUNCTIONS TO CHECK FOR VICTORY STATES"""

    # Function to check if a player has won Vertically
    def vertical_victory(self, game_board):
        for index in range(3):
            if self.equality(game_board[0][index], game_board[1][index], game_board[2][index]):
                self.winner = game_board[0][index]
                return True
        return False

    # Function to check horizontal combinations.
    def horizontal_victory(self, game_board):
        for index in range(3):
            if self.equality(game_board[index][0], game_board[index][1], game_board[index][2]):
                self.winner = game_board[index][0]
                return True
        return False

    # Function to check for diagonal wins.
    def diagonal_victory(self, game_board):
        diagonal1 = self.equality(game_board[0][0], game_board[1][1], game_board[2][2])
        diagonal2 = self.equality(game_board[0][2], game_board[1][1], game_board[2][0])
        if diagonal1:
            self.winner = game_board[0, 0]
            return True
        elif diagonal2:
            self.winner = game_board[0, 2]
            return True

        return False

    """ ALPHA-BETA PRUNING ALGORITHM"""

    # IMPLEMENTATION OF ALPHA BETA PRUNING ALGORITHM TO GET THE BEST POSSIBLE SCORE.
    def AI(self):
        optimal_score = np.NINF  # Let's set our optimal score to -infinity.
        x, y = 0, 0
        for i in range(3):
            for j in range(3):
                # Check if the location is available.
                if self.check_location(i, j):
                    # Update the board temporarily to apply ALPHA-BETA Pruning.
                    self.board[i][j] = self.ai
                    # Call the ALPHA_BETA function to generate all the possible outcomes for
                    # the above updated board and prune all the states that are not required.
                    # we set the value of alpha and beta for the worst case scenarios, i.e., -infinity
                    # for alpha and infinity for beta.
                    score = self.ALPHA_BETA(self.board, np.NINF, np.Inf, 0, False)
                    # Reset the board to previous state.
                    self.board[i][j] = ''
                    # if the achieved score is better than optimal score, store the locations
                    # and score values.
                    if score > optimal_score:
                        optimal_score = score
                        x, y = i, j
        # Once we have iterated through all the empty spots, give the best spot on the board
        # to AI, i.e., X
        self.board[x][y] = self.ai
        self.player = self.human
        # Reset winner, because while we are recursively calling the ALPHA_BETA functions, it will
        # eventually reach a terminal point and get a winner. We don't want that temporary
        # values to be decisive in the main game.
        self.winner = None
        return x, y

    # ALPHA BETA PRUNING
    def ALPHA_BETA(self, board, alpha, beta, depth, is_max):

        # Check if we are in the terminal state, i.e., one or the other player
        # has won. This will update the winner entity of the class, we will reset
        # it after the function is terminated.
        winner = self.check_state(board)
        if winner is not None:
            return self.scores[winner]

        # Get the max score for the maximizing player. In our case -> X.
        if is_max:
            # Initialize the best score as -infinity.
            best_score = np.NINF
            for i in range(3):
                for j in range(3):
                    # Check if the location is available.
                    if self.check_location(i, j):
                        self.board[i][j] = self.ai
                        score = self.ALPHA_BETA(board, alpha, beta, depth + 1, False)
                        self.board[i][j] = ''
                        best_score = max(score, best_score)
                        # getting the best value for alpha, in this case, the greater value
                        # between alpha and our best score
                        alpha = max(alpha, best_score)
                        if alpha >= beta:
                            break
            return best_score

        # Get the minimum score for the minimizing player. In our case -> O.
        else:
            # Initialize the best score as infinity.
            best_score = np.Infinity
            for i in range(3):
                for j in range(3):
                    # Check if the location is available.
                    if self.check_location(i, j):
                        board[i][j] = self.human
                        score = self.ALPHA_BETA(board, alpha, beta, depth + 1, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
                        # getting the best value for alpha, in this case, the smaller value
                        # between alpha and our best score
                        alpha = min(alpha, best_score)
                        if alpha >= beta:
                            break
            return best_score


"""END OF FILE"""
