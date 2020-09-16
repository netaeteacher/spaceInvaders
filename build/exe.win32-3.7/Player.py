import pygame
# import random
from Bullet import Bullet
from os import path


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
sound_dir = path.join(path.dirname(__file__), 'sounds')

class Player(pygame.sprite.Sprite):
    def __init__(self, p_win, p_player_img, p_bullet_image, p_shoot_sound):
        pygame.sprite.Sprite.__init__(self)
        self.win = p_win
        self.winWidth = p_win.get_width()
        self.winHeight = p_win.get_height()
        # self.s_width = p_width
        # self.s_height = p_height

        self.shoot_sound = p_shoot_sound
        # הגדרת המאפיין image ל- sprite שנוצר
        self.image = pygame.Surface((70, 70))

        # הגדרת המאפיין color ל- sprite שנוצר
        # self.color = self.image.fill(p_color)

        self.image = pygame.transform.scale(p_player_img, (70, 70))
        self.image.set_colorkey(BLACK)
        # הגדרת המאפיין rect ל- sprite שנוצר
        self.rect = self.image.get_rect()

        # הגדרת המיקום ההתחלתי של ה- sprite הנוצר, להיות באמצע החלק התחתון שבמסך
        self.rect.centerx = self.winWidth / 2
        self.rect.bottom = self.winHeight - 10

        # הגדרת המהירות של ה- sprite  הנוצר, להשאר במקום בתנועה על ציר ה-x
        self.speedX = 0
        self.bullet_image = p_bullet_image
        self.bullets = pygame.sprite.Group()

        self.last_shot = 0

    def update(self):
        self.speedX = 0
        # הגדרת המהירות של ה- sprite  הנוצר, בהתאם ללחיצת הכפתור ימינה או שמאלה
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speedX = -10
        if key_state[pygame.K_RIGHT]:
            self.speedX = 10

        # הזזת האובייקט על ציר ה-x, לפי למהירות שנקבעה
        self.rect.x += self.speedX

        # חוקים שמגדירים מה יקרה במצב בו האובייקט יצא מגבולות המסך
        if self.rect.right > self.winWidth:
            self.rect.right = self.winWidth
        if self.rect.left < 0:
            self.rect.left = 0

        self.bullets.draw(self.win)

        self.bullets.update()

    def shoot(self):
        bullet = Bullet(self.win, self.rect.centerx, self.rect.top, self.bullet_image, self.shoot_sound)
        self.bullets.add(bullet)
    # def change_color(self):
        # r_color = random.randint(0, 255)
        # g_color = random.randint(0, 255)
        # b_color = random.randint(0, 255)
        # self.color = self.image.fill(r_color, g_color, b_color)
