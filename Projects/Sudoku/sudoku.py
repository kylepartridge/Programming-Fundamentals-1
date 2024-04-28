# Research Pygame's documentation and utilized the Rect() class and its methods in order to make mouse events easier to
# handle as well as get_width(), get_height() for sizing and spacing
import pygame
import sys
from board import Board
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")

# Set up a spacing variable so the buttons are evenly spaced
spacing = (SCREEN_WIDTH - BUTTON_WIDTH * 3) / 4

# Function to welcome the user and choose difficulty
def welcome_screen():
    # Clear the screen, set a font for the welcome screen
    screen.fill(BLUE)
    welcome_screen_font = pygame.font.Font(None, FONT)

    welcome_text = "Welcome to Sudoku!"
    game_mode_text = "Select Game Mode:"

    # Place welcome_text on screen
    welcome_surf = welcome_screen_font.render(welcome_text, 0, BLACK)
    welcome_rect = welcome_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5))
    screen.blit(welcome_surf, welcome_rect)

    # Place game_mode_text on screen
    mode_surf = welcome_screen_font.render(game_mode_text, 0, BLACK)
    mode_rect = mode_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.75))
    screen.blit(mode_surf, mode_rect)

    # Instantiate a Rect instance with each difficulty button
    easy_button = pygame.Rect(spacing, SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    medium_button = pygame.Rect(2 * spacing + BUTTON_WIDTH, SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    hard_button = pygame.Rect(3 * spacing + 2 * BUTTON_WIDTH, SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Draw buttons
    pygame.draw.rect(screen, ORANGE, easy_button)
    pygame.draw.rect(screen, ORANGE, medium_button)
    pygame.draw.rect(screen, ORANGE, hard_button)

    # Add text to buttons
    easy_text = welcome_screen_font.render("Easy", 0, BLACK)
    medium_text = welcome_screen_font.render("Medium", 0, BLACK)
    hard_text = welcome_screen_font.render("Hard", 0, BLACK)
    screen.blit(easy_text,(easy_button.centerx - easy_text.get_width() // 2, easy_button.centery - easy_text.get_height() // 2))
    screen.blit(medium_text, (medium_button.centerx - medium_text.get_width() // 2, medium_button.centery - medium_text.get_height() // 2))
    screen.blit(hard_text,(hard_button.centerx - hard_text.get_width() // 2, hard_button.centery - hard_text.get_height() // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(mouse_pos):
                    return 30
                elif medium_button.collidepoint(mouse_pos):
                    return 40
                elif hard_button.collidepoint(mouse_pos):
                    return 50
        pygame.display.update()
def game_over_screen(screen, winner):
    screen.fill(BLUE)
    # Display winning or losing message
    game_over_screen_font = pygame.font.Font(None, FONT)
    if winner:
        message = "Game Won!"
        option_message = "EXIT"
    else:
        message = "Game Over :("
        option_message = "RESTART"
    message_surf = game_over_screen_font.render(message, 0, BLACK)
    message_rect = message_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(message_surf, message_rect)

    # Instantiate Rect for option button
    option_button = pygame.Rect(2 * spacing + BUTTON_WIDTH, SCREEN_HEIGHT // 1.5 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    # Draw button
    pygame.draw.rect(screen, ORANGE, option_button)
    # Add message to button
    option_text = game_over_screen_font.render(option_message, 0, BLACK)
    screen.blit(option_text,(option_button.centerx - option_text.get_width() // 2, option_button.centery - option_text.get_height() // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option_button.collidepoint(mouse_pos) and winner:
                    return False
                else:
                    main()
        pygame.display.update()


# Main function
def main():
    # Call welcome_screen and store user chosen difficulty
    difficulty = welcome_screen()
    # Create a board instance
    board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, screen, difficulty)
    screen.fill(BLUE)

    # Event loop
    running = True
    while running:
        screen.fill(BLUE)
        # Continuously draw the updated 2D board
        board.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                x, y = pygame.mouse.get_pos()
                if board.reset_button.collidepoint(x, y):
                    board.reset_to_original()  # Reset the board to initial state
                elif board.restart_button.collidepoint(x, y):
                    board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, screen, difficulty)  # Restart game
                elif board.exit_button.collidepoint(x, y):
                    running = False  # Exit the game
                # Convert mouse position to row and column
                row, col = board.click(x, y)
                # Check if a cell was clicked
                if row is not None and col is not None:
                    # Select the clicked cell
                    board.select(row, col)
            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    current_number = event.key - pygame.K_0
                    # Input a number
                    if board.selected_cell:
                        board.sketch(current_number)
                elif event.key == pygame.K_RETURN:
                    if board.selected_cell and board.selected_cell.sketched_value != 0:
                        board.place_number(board.selected_cell.sketched_value)  # Confirm the sketched value as permanent
                        board.selected_cell.sketched_value = 0  # Clear the sketched value after placing
                        print(board.board)
                if event.key == pygame.K_BACKSPACE:
                    # Clear the sketched value when Backspace is pressed
                    board.sketch(0)
                if event.key == pygame.K_UP:
                    board.select(board.selected_row - 1, board.selected_col)  # Move up
                if event.key == pygame.K_DOWN:
                    board.select(board.selected_row + 1, board.selected_col)  # Move down
                if event.key == pygame.K_LEFT:
                    board.select(board.selected_row, board.selected_col - 1)  # Move left
                if event.key == pygame.K_RIGHT:
                    board.select(board.selected_row, board.selected_col + 1)  # Move right
            # Update the underlying 2D board
            board.update_board()

        # Check if the board is solved
        if board.is_full():
            if board.check_board():
                winner = True
            else:
                winner = False
            if not game_over_screen(screen, winner):
                running = False
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
