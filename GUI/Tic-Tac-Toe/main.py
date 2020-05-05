import pygame as pg
from grid import Grid

# Initializing pygame
pg.init()

# Dimensions of the Game Window
WIDTH = 400
HEIGHT = 400
GAME_RESET = False

# Creating the game window
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe")
clock = pg.time.Clock()
# Grid
grid = Grid(WIDTH, HEIGHT, window)
game_font, background = None, None


def main_loop():
    # Run the game until clicked close
    GAME_OVER = False
    while not GAME_OVER:
        # Check for the events in the game.
        for event in pg.event.get():
            # Close the game if close button is clicked
            if event.type == pg.QUIT:
                exit()
            # Check for a mouse click event
            if event.type == pg.MOUSEBUTTONDOWN:
                # Get the coordinates of click.
                if pg.mouse.get_pos()[0]:
                    pos = pg.mouse.get_pos()
                    # convert the coordinates to rows and columns
                    col = pos[0] // (WIDTH // 3)  # yields a value between 0-2 inclusively
                    row = pos[1] // (WIDTH // 3)  # yields a value between 0-2 inclusively
                    # Check if that location is available on the board.
                    if grid.check_location(row, col):
                        # Add the player on the board
                        grid.add_to_board(row, col)
                        # grid.draw_on_board(row, col, grid.player)
                        # Check for a winner
                        result = grid.check_state(grid.board)
                        if result is not None:
                            # Print the result in console and Game Screen
                            # grid.print_result(result)
                            GAME_OVER = grid.game_over(result)

        # Update the changes every frame.
        pg.display.update()
        clock.tick(60)
    game_reset()


def game_init():
    # Fill the background of the Game Window
    window.fill((255, 255, 255))
    # Draw the grid
    grid.draw_grid()
    # grid.get_board()
    main_loop()


def get_text(message, font, colors=(255, 255, 255)):
    text = font.render(message, True, colors)
    text_rect = text.get_rect()
    return text, text_rect


def load_assets():
    global game_font, background
    game_icon = pg.image.load('assets/images/icon.png')
    background = pg.image.load('assets/images/back.jpg')
    game_font = [pg.font.Font('assets/fonts/IndieFlower-Regular.ttf', WIDTH // 7),  # Font for Game Title
                 pg.font.Font('assets/fonts/IndieFlower-Regular.ttf', WIDTH // 20),
                 pg.font.Font('assets/fonts/IndieFlower-Regular.ttf', WIDTH // 24)]
    pg.display.set_icon(game_icon)
    background = pg.transform.scale(background, (WIDTH, HEIGHT))


def game_intro():
    # load game assets
    load_assets()
    # Game Heading text
    heading_text, heading_rect = get_text("Tic Tac Toe", game_font[0])
    heading_rect.center = (WIDTH // 2, HEIGHT // 3)

    # Start the game text
    start_text, start_rect = get_text("Press any key to start", game_font[1])
    start_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Exit game text
    exit_text, exit_rect = get_text("Press Esc or Right mouse to exit.", game_font[2], colors=(128, 128, 128))
    exit_rect.center = (WIDTH // 2, HEIGHT - 20)

    RUNNING = True
    while RUNNING:
        window.fill((255, 255, 255))
        window.blit(background, (0, 0))

        # Add text to screen
        window.blit(heading_text, heading_rect)
        window.blit(start_text, start_rect)
        window.blit(exit_text, exit_rect)
        for event_ in pg.event.get():
            if event_.type == pg.QUIT:
                RUNNING = False

            # Check for keypress or mouse click to start the game
            if event_.type == pg.KEYDOWN:
                # If Esc key is pressed, exit the game.
                if event_.key == pg.K_ESCAPE:
                    exit()
                game_init()
            if event_.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[2] == 1:
                    exit()
                game_init()

        pg.display.update()
        clock.tick(60)


def game_reset():
    global window, game_font, background, grid
    window = pg.display.set_mode((WIDTH, HEIGHT))
    game_font, background = None, None
    grid = Grid(WIDTH, HEIGHT, window)
    game_intro()


if __name__ == "__main__":
    # Start the game
    game_intro()
    pg.quit()
