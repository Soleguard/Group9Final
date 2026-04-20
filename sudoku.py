# Import pygame and sys modules
import pygame
# import sys

# Import Board and SudokuGenerator classes and start_screen function
from board import Board
from sudoku_generator import SudokuGenerator
from board import start_screen

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
board_data = SudokuGenerator.generate_sudoku(9, removed_cells)

# Call Board class from board [dot] py
board = Board(540, 540, win, difficulty, board_data)

# Loop through Sudoku game
while True:

    board.draw()

    # # Event loop
    # for event in pygame.event.get():
    #
    #     # Manage player exit
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()

    pygame.display.update()
