# Import pygame and sys modules
import pygame
import sys

# Import Board class and start_screen and generate_sudoku functions
from board import Board
from board import start_screen
from sudoku_generator import generate_sudoku

# Main
if __name__ == "__main__":

    # Initialize pygame
    pygame.init()

    # Screen display
    screen_display = pygame.display

    # Form screen
    screen = screen_display.set_mode()

    # Get default size
    x, y = screen.get_size()

    # Store screen size
    z = [x, y]

    # Set size of window
    win = screen_display.set_mode(z)

    # Difficulty
    difficulty = start_screen(win)

    # Determine number of removed cells
    if difficulty == "easy":
        removed_cells = 30

    elif difficulty == "medium":
        removed_cells = 40

    elif difficulty == "hard":
        removed_cells = 50

    # Board data
    board_data = generate_sudoku(9, removed_cells)

    # Call Board class from board [dot] py
    board = Board(540, 540, win, difficulty, board_data)

    # Loop through Sudoku game
    while True:

        board.draw()

        # Event loop
        for event in pygame.event.get():

            # Manage player exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Click event
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # Get position
                # x, y = event.pos
                #
                # # Check if player selects 1 - Easy
                # if (x == 180) and (y == 250):
                #     print("Generate Sudoku Board")

            # Key input event
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_1:
            #         # 1
            #     elif event.key == pygame.K_2:
            #         # 2
            #     elif event.key == pygame.K_3:
            #         # 3
            #     elif event.key == pygame.K_4:
            #         # 4
            #     elif event.key == pygame.K_5:
            #         # 5
            #     elif event.key == pygame.K_6:
            #         # 6
            #     elif event.key == pygame.K_7:
            #         # 7
            #     elif event.key == pygame.K_8:
            #         # 8
            #     elif event.key == pygame.K_9:
            #         # 9
            #     # Return/enter key
            #     elif event.key == pygame.K_RETURN:
            #         # Return

            # Win/loss condition

            # End game screen

        pygame.display.update()
