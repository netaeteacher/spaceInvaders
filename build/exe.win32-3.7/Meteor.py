import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR_LIST = [WHITE, RED, GREEN, BLUE]


class Meteor(pygame.sprite.Sprite):
    def __init__(self, p_win, p_meteor_images):
        pygame.sprite.Sprite.__init__(self)

        # קבלת אורך ורוחב החלון
        self.winWidth = p_win.get_width()
        self.winHeight = p_win.get_height()

        # הגדרת המאפיין image ל- sprite שנוצר
        # self.image = pygame.transform.scale(p_meteor_img, (60, 60))
        self.image = random.choice(p_meteor_images).convert()
        self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((p_width, p_height))
        # self.image.fill(p_color)

        # הגדרת המאפיין rect ל- sprite שנוצר
        self.rect = self.image.get_rect()

        # הגדרת המיקום ההתחלתי של ה- sprite הנוצר, להיות בחלק העליון במסך
        self.rect.x = random.randrange(self.winWidth)
        self.rect.y = random.randrange(-100, -40)

        # הגדרת המהירות של ה- sprite  הנוצר, להיות רנדומלית בתנועה על 2 הצירים
        self.speedY = random.randrange(1, 8)
        self.speedX = random.randrange(-3, 3)

    def update(self):
        # הזזת האובייקטים על הצירים, בהתאם למהירות ההתחלתית שנקבעה
        self.rect.x += self.speedX
        self.rect.y += self.speedY

        # חוק שמגדיר מה יקרה במצב בו האובייקט יצא מגבולות המסך
        if self.rect.top > self.winHeight + 10 or self.rect.left < -25 or self.rect.right > self.winWidth + 20:
            self.rect.x = random.randrange(self.winWidth)
            self.rect.y = random.randrange(-100, -40)
            self.speedY = random.randrange(1, 8)
            self.speedX = random.randrange(-3, 3)
