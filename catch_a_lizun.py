from field import dist
from sprite_movements import sprite_movements
import pygame

pygame.init()

number_of_caught = 0
lizun_ = 0
set_caught = set()

music = pygame.mixer.Sound('Music/зел1.ogg')

music_minus = pygame.mixer.Sound('Music/кр1.ogg')


# громкость
def music_(sound):
    global music_minus, music
    music_minus.set_volume(sound)
    music.set_volume(sound)


# вычитаем лизуна
def time_to_destroy_the_lizun_():
    global number_of_caught
    number_of_caught = max(number_of_caught - 1, 0)


# взаимодействие с лизунами
def catch_a_lizun(x_player, y_player, sprite):
    global number_of_caught
    t = -1
    for lizun in sprite.sprite_types_pos:
        t += 1
        x_lizun, y_lizun = sprite.sprite_types_pos[lizun]
        if 's' in lizun:
            view = 's'
        else:
            view = 'rot'
        if dist(x_player, y_player, x_lizun * 100 + 50, y_lizun * 100 + 50) <= 132 \
                and lizun not in set_caught and view == 'rot' and number_of_caught:
            sprite_movements(1, 1, sprite, sprite_type=(lizun, t), cleaning=True, view=view)
            set_caught.add(lizun)
        elif dist(x_player, y_player, x_lizun * 100 + 50, y_lizun * 100 + 50) <= 80 \
                and lizun not in set_caught and view == 's':
            sprite_movements(1, 1, sprite, sprite_type=(lizun, t), cleaning=True, view=view)
            set_caught.add(lizun)
        else:
            continue
        if view == 'rot':
            time_to_destroy_the_lizun_()
            music_minus.play()
        else:
            number_of_caught += 1
            music.play()


# кол-во баллов
def ball(screen, hall):
    x = 7
    x2 = 4
    if hall == 1:
        x = x2 = 1
    if hall == 2:
        x2 = x = 4
    if hall == 4:
        x2 = 1
    font = pygame.font.Font(None, 100)
    text = font.render(f"/{x}", True, (50, 185, 50))
    text_number_of_caught = font.render(f"{number_of_caught}", True, (250, 100, 50))
    if number_of_caught >= x2:
        text_number_of_caught = font.render(f"{number_of_caught}", True, (50, 185, 50))
    text_x = 960
    text_y = 700
    screen.blit(text, (text_x, text_y))
    screen.blit(text_number_of_caught, (920, text_y))


# лизуны в шарике
def lizun(screen, true):
    global lizun_
    if number_of_caught and true:
        lizun_ += 1
        if lizun_ > 7:
            lizun_ = 1
        sky = pygame.image.load(f'Ball/{lizun_}.png').convert()
        screen.blit(sky, (900, 630))
    elif not number_of_caught:
        sky = pygame.image.load(f'Ball/8.png').convert()
        screen.blit(sky, (900, 630))
    else:
        sky = pygame.image.load(f'Ball/{lizun_}.png').convert()
        screen.blit(sky, (900, 630))


# возвращает кол-во баллов
def number():
    return number_of_caught


# очистка множества пойманных лизунов
def set_caught_():
    global set_caught
    set_caught = set()


# обновление параметров
def number_of_caught_new():
    global number_of_caught, lizun_
    number_of_caught = 0
    lizun_ = 0
    set_caught_()
