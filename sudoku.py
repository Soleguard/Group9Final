# Import pygame and sys modules
import pygame
import sys

# Import Board class and start_screen and generate_sudoku functions
from board import Board
from board import start_screen
from sudoku_generator import generate_sudoku

# ── Colour palette
WHITE = (255, 255, 255)
LIGHT_RED = (220,  80,  80)   # main background colour
DARK_RED = (180,  40,  40)   # deeper red for button hover
BTN_COLOR = (255, 255, 255)   # white buttons
BTN_HVR = (220, 220, 220)   # light grey on hover
BTN_TEXT = (0,   0,   0)     # black button text
LINE_COLOR = (180,  60,  60)   # reddish separator line
 
BOARD_SIZE = 540
SCREEN_HEIGHT = 660   # 540 board + 120 for button bar

# Button settings
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100


# Draw button
def draw_button(surface, text, rect, font, color=BTN_COLOR, hover_color=BTN_HVR, text_color=BTN_TEXT):
    mouse = pygame.mouse.get_pos()
    current_color = hover_color if rect.collidepoint(mouse) else color
    pygame.draw.rect(surface, current_color, rect, border_radius=8)
    pygame.draw.rect(surface, DARK_RED, rect, 2, border_radius=8)
    label = font.render(text, True, text_color)
    lx = rect.x + (rect.width - label.get_width()) // 2
    ly = rect.y + (rect.height - label.get_height()) // 2
    surface.blit(label, (lx, ly))
    return rect


def main():

    # Initialize pygame
    pygame.init()

    # Create font settings for button
    button_font = pygame.font.Font(None, 30)

    # Create rectangle for reset, restart, and exit buttons
    # Format: pygame.Rect(x (left), y (top), width, height)
    reset_rect = pygame.Rect(60, 600, BUTTON_WIDTH, BUTTON_HEIGHT)
    restart_rect = pygame.Rect(60, 600, BUTTON_WIDTH, BUTTON_HEIGHT)
    exit_rect = pygame.Rect(60, 600, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Screen display
    screen_display = pygame.display

    # Set screen size
    x, y = BOARD_SIZE, SCREEN_HEIGHT

    # Store screen size
    z = [x, y]

    # Set size of window
    win = screen_display.set_mode(z)

    # Difficulty
    difficulty = start_screen(win)

    # 1. Remove start screen after difficulty screen
    # 2. Fill screen with white
    win.fill((255, 255, 255))

    # Update screen
    pygame.display.update()

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
    board = Board(BOARD_SIZE, BOARD_SIZE, win, difficulty, board_data)
    # board = Board(x, y, win, difficulty, board_data)

    # Create reset, restart, and exit buttons
    draw_button(win, "RESET", reset_rect, button_font)
    draw_button(win, "RESTART", restart_rect, button_font)
    draw_button(win, "EXIT", exit_rect, button_font)

    # Loop through Sudoku game
    while True:

        # Clear screen to begin game session
        win.fill((255, 255, 255))

        # Draw board
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

        pygame.display.update()

        # Win/loss condition

        # End game screen
        # if game_result in ("won", "lost"):
        #     end = game_over_screen(win, game_result)
        #
        #     if end == "restart":
        #         # Back to start screen
        #         continue


# Main
if __name__ == "__main__":

    main()
