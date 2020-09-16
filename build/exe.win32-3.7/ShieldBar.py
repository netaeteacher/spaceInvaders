import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class ShieldBar:
    def __init__(self, win, x, y):
        self.win = win
        self.bar_width = 90
        self.bar_height = 15
        self.x = x
        self.y = y
        self.shield_pct = 90

    def draw(self, new_pct):
        if new_pct < 0:
            new_pct = 0
        fill = (new_pct / 90) * self.bar_width
        outline_rect = pygame.Rect(self.x, self.y, self.bar_width, self.bar_height)
        fill_rect = pygame.Rect(self.x, self.y, fill, self.bar_height)
        pygame.draw.rect(self.win, GREEN, fill_rect)
        pygame.draw.rect(self.win, WHITE, outline_rect, 2)
