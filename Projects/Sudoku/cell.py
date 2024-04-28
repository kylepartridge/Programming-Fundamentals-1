import pygame
from constants import *

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.font = pygame.font.Font(None, FONT)  # Font for placed numbers
        self.cell_size = SCREEN_WIDTH // 9
        self.initial_value = value  # Store the initial value to reset to later


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * self.cell_size
        y = self.row * self.cell_size
        pygame.draw.rect(self.screen, BLUE, (x, y, self.cell_size, self.cell_size))  # Cell background
        if self.selected:
            pygame.draw.rect(self.screen, RED, (x, y, self.cell_size, self.cell_size), 4)  # Highlight selected cell

        # Display placed value centrally if available
        if self.value != 0:
            text_surf = self.font.render(str(self.value), 0, BLACK)
            text_rect = text_surf.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
            self.screen.blit(text_surf, text_rect)
        # Display sketched value in the top left corner if available and no placed value
        elif self.sketched_value != 0:
            sketched_text_surface = self.font.render(str(self.sketched_value), 0, GRAY)
            self.screen.blit(sketched_text_surface, (x + 5, y + 5))

        # Draw cell borders
        pygame.draw.rect(self.screen, BLACK, (x, y, self.cell_size, self.cell_size), 1)

        # Draw cell borders
        pygame.draw.rect(self.screen, BLACK, (x, y, self.cell_size, self.cell_size), 1)

    def reset(self):
        # Reset the cell's value to the initial value
        self.value = self.initial_value
        self.sketched_value = 0  # Assuming we want to clear sketches as well
