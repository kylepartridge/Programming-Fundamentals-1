from cell import *
from sudoku_generator import *
from constants import *

class Board:

    """
    Constructor for the SudokuGenerator class.
    For the purposes of this project, row_length is always 9.
    removed_cells could vary depending on the difficulty level chosen (see “UI Requirements”)
    """
    spacing = (SCREEN_WIDTH - BUTTON_WIDTH * 3) / 4
    def __init__(self, width, height, screen, difficulty):
        self.selected_cell = None
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, difficulty)
        self.cells = [[Cell(self.board[i][j], i, j, screen) for j in range(9)] for i in range(9)]
        self.font = pygame.font.SysFont(None, FONT)  # Define the font


    def draw(self):
        """
        Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board
        """
        # fill screen with blue color
        self.screen.fill(BLUE)

        # Draw each cell using the Cell class' draw() method
        for row in self.cells:
            for cell in row:
                cell.draw()

        # Drawing thicker lines to separate each 3x3 box
        cell_size = self.width // 9
        # Vertical lines
        for i in range(0, self.width, cell_size * 3):  # Draw vertical lines every 3 cells
            pygame.draw.line(self.screen,
                             BLACK,
                             (i, 0),
                             (i, cell_size * 9),
                             THICK_BORDER)
        # Horizontal lines
        for j in range(0, self.height, cell_size * 3):  # Draw horizontal lines every 3 cells
            pygame.draw.line(self.screen,
                             BLACK,
                             (0, j),
                             (self.width, j),
                             THICK_BORDER)

        # See the last method that displays the reset, restart and exit buttons throughout the game
        self.draw_buttons()
        pygame.display.update()  # Update the display after all cells are drawn

    def select(self, row, col):
        """
        Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value
        """
        # Making sure we don't click too far out of the board
        in_range_row = max(0, min(row, 8))
        in_range_col = max(0, min(col, 8))
        # Unselect the previously selected cell
        if self.selected_cell:
            self.selected_cell.selected = False
        # Update the selected cell based arrow key inputs
        self.selected_cell = self.cells[in_range_row][in_range_col]
        self.selected_cell.selected = True
        self.selected_row = in_range_row
        self.selected_col = in_range_col

    def click(self, x, y):
        """
        If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        of the cell which was clicked. Otherwise, this function returns None.
        """
        cell_size = self.width // 9
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // cell_size
            col = x // cell_size
            if row < 9 and col < 9:
                return row, col
        return None, None

    def clear(self):
        """
        Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves
        """
        if self.selected_cell is not None:
            self.selected_cell.value = 0
            self.selected_cell.sketched_value = 0
    def sketch(self, value):
        """
        Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed at the top left corner of the cell using the draw() function.
        """
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.sketched_value = value
            self.selected_cell.draw()

    def place_number(self, value):
        """
        Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key
        """
        if self.selected_cell and self.selected_cell.value == 0:
            if value in range(1, 10):
                self.selected_cell.value = value
                self.selected_cell.draw()

    def reset_to_original(self):
        """
        Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
        """
        for row in self.cells:
            for cell in row:
                cell.reset()


    def is_full(self):
        """
        Returns a Boolean value indicating whether the board is full or not.
        """
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        """
        Updates the underlying 2D board with the values in all cells.
        """
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    def find_empty(self):
        """
        Finds an empty cell and returns its row and col as a tuple (x, y).
        """
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return i, j
        return None

    def check_board(self):
        """
        Check whether the Sudoku board is solved correctly
        """
        # Check rows. A sorted list from 1 through 10 should match each row if correct
        for row in self.board:
            if sorted(row) != list(range(1, 10)):
                return False
        # Check columns. Same idea for rows.
        for col in range(9):
            if sorted([self.board[row][col] for row in range(9)]) != list(range(1, 10)):
                return False
        # Check 3x3 squares. Start from top left corner and move right
        for i in range(0, 9, 3): # 0, 3, 6
            # Gather all numbers from the square into a list and check the list after sorting
            for j in range(0, 9, 3): # 0, 3, 6
                square = [self.board[a][b] for a in range(i, i + 3) for b in range(j, j + 3)]
                if sorted(square) != list(range(1, 10)):
                    return False

        return True

    def draw_buttons(self):
        '''
        Display a menu throughout the game which include reset, restart and exit
        '''
        # Total width of all buttons and spacings
        total_width = MINI_BUTTON_WIDTH * 3 + Board.spacing * 2

        # Starting x-coordinate so that the buttons group is centered
        start_x = (self.width - total_width) // 2

        # Positioned 10 pixels above the bottom of the screen
        y_position = self.height - MINI_BUTTON_HEIGHT - 10

        # Instantiate Rect() for each button
        self.reset_button = pygame.Rect(start_x, y_position, MINI_BUTTON_WIDTH, MINI_BUTTON_HEIGHT)
        self.restart_button = pygame.Rect(start_x + MINI_BUTTON_WIDTH + Board.spacing, y_position, MINI_BUTTON_WIDTH, MINI_BUTTON_HEIGHT)
        self.exit_button = pygame.Rect(start_x + 2 * (MINI_BUTTON_WIDTH + Board.spacing), y_position, MINI_BUTTON_WIDTH, MINI_BUTTON_HEIGHT)

        # Draw button rectangles
        pygame.draw.rect(self.screen, ORANGE, self.reset_button)
        pygame.draw.rect(self.screen, ORANGE, self.restart_button)
        pygame.draw.rect(self.screen, ORANGE, self.exit_button)

        # Button text
        reset_text = self.font.render('Reset', 0, BLACK)
        restart_text = self.font.render('Restart', 0, BLACK)
        exit_text = self.font.render('Exit', 0, BLACK)

        # Position text in the center of the buttons
        self.screen.blit(reset_text, (self.reset_button.x + (MINI_BUTTON_WIDTH - reset_text.get_width()) // 2, self.reset_button.y + (MINI_BUTTON_HEIGHT - reset_text.get_height()) // 2))
        self.screen.blit(restart_text, (self.restart_button.x + (MINI_BUTTON_WIDTH - restart_text.get_width()) // 2, self.restart_button.y + (MINI_BUTTON_HEIGHT - restart_text.get_height()) // 2))
        self.screen.blit(exit_text, (self.exit_button.x + (MINI_BUTTON_WIDTH - exit_text.get_width()) // 2, self.exit_button.y + (MINI_BUTTON_HEIGHT - exit_text.get_height()) // 2))