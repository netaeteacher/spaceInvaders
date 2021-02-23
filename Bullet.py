import pygame

WHITE = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, p_win, p_x, p_y, p_bullet_img, p_sound):
        pygame.sprite.Sprite.__init__(self)
        p_sound.play()
        self.winWidth = p_win.get_width()
        self.winHeight = p_win.get_height()
        self.image = pygame.transform.scale(p_bullet_img, (9, 54))
        self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((p_width, p_height))
        # self.image.fill(p_color)
        self.rect = self.image.get_rect()
        self.rect.bottom = p_y
        self.rect.centerx = p_x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
