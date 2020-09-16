import pygame
# import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, p_center, p_size, p_explosion_animation, p_explosion_sound):
        pygame.sprite.Sprite.__init__(self)
        p_explosion_sound.play()
        self.explosion = p_explosion_animation
        self.size = p_size
        self.image = p_explosion_animation[0]
        self.rect = self.image.get_rect()
        self.rect.center = p_center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
