import pygame
# import random
from Player import Player
from Meteor import Meteor
from Explosion import Explosion
import sys
from os import path
from TekkiePygameLib import Label, Button
from ShieldBar import ShieldBar

WIN_WIDTH = 500
WIN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

img_dir = path.join(path.dirname(__file__), 'img')
explosions_img_dir = path.join(path.dirname(__file__), 'img/Explosions')
extra_explosions_img_dir = path.join(path.dirname(__file__), 'img/extraExplosions')
new_img_dir = path.join(path.dirname(__file__), 'img/new_img')
sound_dir = path.join(path.dirname(__file__), 'sounds')

pygame.mixer.init()
pygame.mixer.music.load(path.join(sound_dir, 'through_space.ogg'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'spaceBG.png')).convert()
background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))
# my_player_img = pygame.image.load(path.join(img_dir, 'spaceship.png')).convert()
my_meteor_img = pygame.image.load(path.join(img_dir, 'meteor.png')).convert()
# my_bullet_image = pygame.image.load(path.join(img_dir, 'bullet.png')).convert()
trophy = pygame.image.load(path.join(img_dir, 'trophy.jpg')).convert()
trophy = pygame.transform.scale(trophy, (60, 60))
trophy.set_colorkey(WHITE)

user_score = Label(x=240, y=40, text="0", color=WHITE, size=40)
my_player_img = pygame.image.load(path.join(new_img_dir, 'spaceship.png')).convert()
my_bullet_image = pygame.image.load(path.join(new_img_dir, 'bullet.png')).convert()
play_stop_bg_music = Button(x=80, y=40, width=100, height=23, text='stop sound', outline_color=BLACK)

shooting_sound = pygame.mixer.Sound(path.join(sound_dir, 'pew.wav'))

meteor_images = []
meteor_list = ["meteor1.png", "meteor2.png", "meteor3.png", "meteor4.png",
               "meteor5.png", "meteor6.png", "meteor7.png", "meteor8.png", "meteor9.png"]
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)))
# my_second_player = Player(win, RED, 20, 20)
my_shieldBar = ShieldBar(win, 10, 10)
my_player = Player(win, my_player_img, my_bullet_image, shooting_sound)
all_sprites = pygame.sprite.Group()
all_sprites.add(my_player)
meteors = pygame.sprite.Group()
# print(list(all_sprites))

explosion_animation_dict = {'large': [], 'small': []}

for i in range(9):
    # img_name = 'regularExplosion0{}.png'.format(i)
    # img = pygame.image.load(path.join(explosions_img_dir, img_name)).convert()
    img_name = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(extra_explosions_img_dir, img_name)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_animation_dict['large'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_animation_dict['small'].append(img_sm)

explosion_sounds_dict = {'large': pygame.mixer.Sound(path.join(sound_dir, 'expl2.wav')),
                         'small': pygame.mixer.Sound(path.join(sound_dir, 'expl1.wav'))}


# explosion_sounds = []
# for sound in ['expl1.wav', 'expl2.wav']:
#     explosion_sounds.append(pygame.mixer.Sound(path.join(sound_dir, sound)))


def create_explosion(p_explosion_loc, p_explosion_size):
    my_explosion = Explosion(p_explosion_loc, p_explosion_size, explosion_animation_dict[p_explosion_size],
                             explosion_sounds_dict[p_explosion_size])
    all_sprites.add(my_explosion)


def create_meteor():
    # r_color = random.randint(0, 255)
    # g_color = random.randint(0, 255)
    # b_color = random.randint(0, 255)
    meteor = Meteor(win, meteor_images)
    all_sprites.add(meteor)
    meteors.add(meteor)


for i in range(8):
    create_meteor()


def stop_play_button():
    if play_stop_bg_music.text == "stop sound":
        play_stop_bg_music.text = "play sound"
        stop_sounds()
    else:
        play_stop_bg_music.text = "stop sound"
        play_sounds()


def stop_sounds():
    pygame.mixer.music.pause()
    explosion_sounds_dict['small'].set_volume(0)
    explosion_sounds_dict['large'].set_volume(0)
    shooting_sound.set_volume(0)


def play_sounds():
    pygame.mixer.music.unpause()
    explosion_sounds_dict['small'].set_volume(0.4)
    explosion_sounds_dict['large'].set_volume(0.4)
    shooting_sound.set_volume(0.4)


def show_game_over_screen(p_message):
    win.blit(background, (0, 0))
    title = Label(x=250, y=200, text='Game Over', color=WHITE, size=65)
    start_over_button = Button(x=250, y=300, width=200, height=30, text='Play again', color=WHITE)
    title.draw(win)
    start_over_button.draw(win)
    message = Label(x=250, y=280, text=p_message, color=WHITE, size=32)
    message.draw(win)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if start_over_button.is_clicked():
                return False


def show_opening_screen():
    waiting = True
    game_name = Label(x=250, y=60, text="Space Invaders", color=WHITE, size=60)
    creator_name = Label(x=250, y=120, text="Ido Pony", color=WHITE, size=50)
    instructions1 = Label(x=250, y=200, text="In this game, you'll have to ", color=WHITE, size=32)
    instructions12 = Label(x=250, y=250, text="avoid the meteors as long as you can.", color=WHITE, size=32)
    instructions2 = Label(x=250, y=300, text="Crushing into a meteor will decrease", color=WHITE, size=32)
    instructions22 = Label(x=250, y=350, text="your final score by 2 points.", color=WHITE, size=32)
    instructions3 = Label(x=250, y=400, text="Shooting at meteors will increase", color=WHITE, size=32)
    instructions32 = Label(x=250, y=450, text="your final score by 1 point.", color=WHITE, size=32)
    resume_game = Label(x=250, y=500, text="Press the enter button to start playing", color=RED, size=32)

    while waiting:
        clock.tick(30)
        win.fill(BLACK)
        win.blit(background, (0, 0))
        game_name.draw(win)
        creator_name.draw(win)
        instructions1.draw(win)
        instructions12.draw(win)
        instructions2.draw(win)
        instructions22.draw(win)
        instructions3.draw(win)
        instructions32.draw(win)
        resume_game.draw(win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
