from player import Player, vision_new, world
from sprite import Sprites, SpriteObject
from time import perf_counter
from menu import Menu
from field import hall_4_, mass, field_, beginning
from transition import transition, transition_4
from catch_a_lizun import *
from random import choice
import sqlite3
import pygame
import pygame_gui
import sys


pygame.init()
clock = pygame.time.Clock()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
TIMER = 30

running = True

screensaver = pygame.image.load(f'Menu/105.png').convert()
batten = pygame.image.load(f'Menu/106.png').convert()
t = False

music_menu = pygame.mixer.Sound('Music/music.ogg')
music_menu.play(-1)

# главное окно "вход"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:

            if 485 <= event.pos[0] <= 690 and 500 <= event.pos[1] <= 630:
                batten = pygame.image.load(f'Menu/107.png').convert()
                t = True

            else:
                batten = pygame.image.load(f'Menu/106.png').convert()
                t = False
        if event.type == pygame.MOUSEBUTTONDOWN and t:
            running = False

    screen.fill((100, 100, 100))

    screen.blit(screensaver, (0, 0))
    screen.blit(batten, (485, 500))

    pygame.display.flip()
    clock.tick(60)
con = sqlite3.connect("game_base.db")
cur = con.cursor()

# создание кнопок с помощью pygame_gui для входа в аккаунт
manage = pygame_gui.UIManager((1200, 800), 'Menu/thema_1.json')
clock_ = pygame.time.Clock()

exit_ = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((520, 620), (150, 50)),
    text='Выход',
    manager=manage
)
entrance = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((430, 400), (150, 50)),
    text='Вход',
    manager=manage
)
registration = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((600, 400), (150, 50)),
    text='Регистрация',
    manager=manage
)
password_ = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((380, 250), (440, 40)),
    manager=manage
)
login_ = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((380, 150), (440, 40)),
    manager=manage
)

font = pygame.font.Font(None, 40)
text = font.render("Пароль: ", True, (200, 200, 200))
font = pygame.font.Font(None, 40)
login = font.render("Логин: ", True, (200, 200, 200))

font = pygame.font.Font(None, 40)
error_ = font.render("Неверный логин или пароль", True, (220, 20, 20))

running_ = True
running_registration = False
password_entrance = ""
login_entrance = ""
er = False
textur = 0
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 1200)
mass_texture = ["303", "304", "305", "306"]
# окно входа в аккаунт
while running_:
    time_delta = clock_.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MYEVENTTYPE:
            textur = (textur + 1) % 4
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_:
                    sys.exit()
                if event.ui_element == entrance:

                    login_ps = cur.execute(f"""SELECT login FROM password
                                               WHERE login = '{login_entrance}' 
                                               AND password = '{password_entrance}'
                    """).fetchall()
                    if not login_ps:
                        er = True
                    else:
                        er = False
                        login_ps = login_ps[0][0]
                        running_ = False
                if event.ui_element == registration:
                    running_ = False
                    running_registration = True
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == password_:
                    password_entrance = event.text
                if event.ui_element == login_:
                    login_entrance = event.text
        manage.process_events(event)

    manage.update(time_delta)
    k = pygame.image.load(f'Menu/{mass_texture[textur]}.png').convert()
    screen.blit(k, (0, 0))
    screen.blit(text, (250, 255))
    screen.blit(login, (250, 155))
    if er:
        screen.blit(error_, (50, 655))
    manage.draw_ui(screen)
    pygame.display.update()

# кнопки для регистрации
manage = pygame_gui.UIManager((1200, 800), 'Menu/thema_2.json')
exit_ = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((520, 620), (150, 50)),
    text='Выход',
    manager=manage
)
registration = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((400, 400), (370, 50)),
    text='Регистрация',
    manager=manage
)
password_ = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((380, 250), (440, 40)),
    manager=manage
)
login_ = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((380, 150), (440, 40)),
    manager=manage
)
font = pygame.font.Font(None, 40)
text = font.render("Пароль: ", True, (200, 200, 200))
font = pygame.font.Font(None, 40)
login = font.render("Логин: ", True, (200, 200, 200))

font = pygame.font.Font(None, 40)
error_ = font.render("Этот логин уже существует", True, (220, 20, 20))

font = pygame.font.Font(None, 40)
error_2 = font.render("Дожно быть не менее 1 символа", True, (220, 20, 20))
er = False
er_2 = False

# окно регистрации
while running_registration:
    time_delta = clock_.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MYEVENTTYPE:
            textur = (textur + 1) % 4
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == exit_:
                    sys.exit()
                if event.ui_element == registration:
                    if not login_entrance or not password_entrance:
                        er_2 = True
                        break
                    er_2 = False
                    login_ps = cur.execute(f"""SELECT login FROM password
                                WHERE login = '{login_entrance}'
                                        """).fetchall()
                    if login_ps:
                        er = True
                    else:
                        er = False
                        login_ps = login_entrance
                        cur.execute(f'''
                        INSERT INTO password(password, login, count)
                         VALUES('{password_entrance}', '{login_entrance}', '0')''')
                        cur.execute(f'''
                                    INSERT INTO settings(mouse, mouse_vision, sens, keyboard, sound)
                                    VALUES('0', '1', '0.005', '1', '1.0')''')
                        running_registration = False
                        con.commit()

            if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == password_:
                    password_entrance = event.text
                if event.ui_element == login_:
                    login_entrance = event.text

        manage.process_events(event)

    manage.update(time_delta)
    k = pygame.image.load(f'Menu/{mass_texture[textur]}.png').convert()
    screen.blit(k, (0, 0))
    screen.blit(text, (250, 255))
    screen.blit(login, (250, 155))
    if er:
        screen.blit(error_, (50, 655))
    if er_2:
        screen.blit(error_2, (50, 655))
    manage.draw_ui(screen)
    pygame.display.update()

# насройки пользователя
result = cur.execute(f"""SELECT mouse, mouse_vision, sens, keyboard, sound, settings.id
                         FROM settings, password
                         WHERE password.id = settings.id AND login = '{login_ps}'
    """).fetchall()[0]
con.close()

menu = Menu(screen, music_menu)
menu.active = False

menu.mouse = int(result[0])
menu.mouse_vision = int(result[1])
menu.settings_sens = float(result[2])
if menu.settings_sens == 0.001:
    menu.mass_setting_sens_index = "Низкая"
elif menu.settings_sens == 0.005:
    menu.mass_setting_sens_index = "Средняя"
else:
    menu.mass_setting_sens_index = "Высокая"
menu.keyboard = int(result[3])
menu.settings_sound = float(result[4])
if menu.settings_sound == 0:
    menu.mass_setting_sound_index = "Нет"
elif menu.settings_sound == 0.1:
    menu.mass_setting_sound_index = "Низкая"
elif menu.settings_sound == 0.5:
    menu.mass_setting_sound_index = "Средняя"
else:
    menu.mass_setting_sound_index = "Высокая"
menu.music.set_volume(menu.settings_sound)

menu.id_ = result[-1]
menu.active = True

player = Player(screen, mass=mass, mouse=True)
sprite = Sprites()
running = True
textures = {
    '1': pygame.image.load('Texture/5.png').convert(),
    '2': pygame.image.load('Texture/15.png').convert(),
    '3': pygame.image.load('Texture/030.png').convert(),
    '4': pygame.image.load('Texture/wall.jpg').convert()
}
textures_ = {
    '1': ['Texture/5.png', 'Texture/15.png'],
    '2': ['Texture/4.png', 'Texture/14.png'],
    '3': ['Texture/6.png', 'Texture/16.png'],
    '4': ['Texture/5.png', 'Texture/200.png']
}

COLOR_ = (69, 71, 48)
MYEVENTTYPE = pygame.USEREVENT + 1
sprite_movements(8, 12, sprite)
sky_ = choice([i for i in range(1, 9)])
pygame.time.set_timer(MYEVENTTYPE, 1500)
true = False
number_sprite = 1
hall = 1
sprite_true = True
sprite_true_2 = True
sprite_true_3 = True
hall_4 = False
clearing_hall_4 = True
color_batten_further = (125, 170, 200)
batten_further_bool = False
color_batten_menu = (125, 170, 200)
batten_menu_bool = False
color_batten_again = (125, 170, 200)
batten_again_bool = False

end = False
color_batten_end = (100, 200, 100)
batten_end_bool = False

time_to_destroy_the_lizun = False
true_timer = False
timer = 0
start = 0

metronome = pygame.mixer.Sound('Music/метроном.ogg')
metronome.stop()

sos = pygame.mixer.Sound('Music/сигнал.ogg')
sos.stop()

result_payer = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYEVENTTYPE:
            true = True

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # пауза
            player.active = False
            player.music_bg.stop()
            player.music_schag.stop()
            player.bg, player.bg_2 = False, False
        # кнопки
        if event.type == pygame.MOUSEMOTION and not player.active and not menu.active:
            if 535 <= event.pos[0] <= 755 and 250 <= event.pos[1] <= 330:
                color_batten_further = (175, 220, 250)
                batten_further_bool = True
            else:
                color_batten_further = (125, 170, 200)
                batten_further_bool = False

        if event.type == pygame.MOUSEBUTTONDOWN and batten_further_bool:
            player.active = True

        if event.type == pygame.MOUSEMOTION and not player.active and not menu.active:
            if 535 <= event.pos[0] <= 755 and 350 <= event.pos[1] <= 430:
                color_batten_menu = (175, 220, 250)
                batten_menu_bool = True
            else:
                color_batten_menu = (125, 170, 200)
                batten_menu_bool = False

        if event.type == pygame.MOUSEBUTTONDOWN and batten_menu_bool and not menu.active:
            menu.active_2 = True
            player.active = False

        if event.type == pygame.MOUSEMOTION and not player.active and not menu.active:
            if 535 <= event.pos[0] <= 755 and 450 <= event.pos[1] <= 530:
                color_batten_again = (175, 220, 250)
                batten_again_bool = True
            else:
                color_batten_again = (125, 170, 200)
                batten_again_bool = False
        if event.type == pygame.MOUSEBUTTONDOWN and batten_again_bool and not menu.active:
            player.x, player.y = 150, 150
            true_timer = False
            timer = 0
            start = 0
            time_to_destroy_the_lizun = False
            player.angle = 0
            sprite = Sprites()
            running = True
            COLOR_ = (69, 71, 48)
            MYEVENTTYPE = pygame.USEREVENT + 1
            sprite_movements(8, 12, sprite)
            sky_ = choice([i for i in range(1, 9)])
            pygame.time.set_timer(MYEVENTTYPE, 1500)
            true = False
            number_sprite = 1
            hall = 1
            sprite_true = True
            sprite_true_2 = True
            sprite_true_3 = True
            hall_4 = False
            clearing_hall_4 = True
            color_batten_further = (125, 170, 200)
            batten_further_bool = False
            color_batten_menu = (125, 170, 200)
            batten_menu_bool = False
            color_batten_again = (125, 170, 200)
            batten_again_bool = False
            number_of_caught_new()
            field_, mass = beginning()
            player.mass = mass
            textures = {
                '1': pygame.image.load('Texture/5.png').convert(),
                '2': pygame.image.load('Texture/15.png').convert(),
                '3': pygame.image.load('Texture/030.png').convert(),
                '4': pygame.image.load('Texture/wall.jpg').convert()
            }
            textures_ = {
                '1': ['Texture/5.png', 'Texture/15.png'],
                '2': ['Texture/4.png', 'Texture/14.png'],
                '3': ['Texture/6.png', 'Texture/16.png'],
                '4': ['Texture/5.png', 'Texture/200.png']
            }

        if event.type == pygame.MOUSEMOTION and end:
            if 940 <= event.pos[0] <= 1160 and 710 <= event.pos[1] <= 790:
                color_batten_end = (200, 0, 0)
                batten_end_bool = True
            else:
                color_batten_end = (100, 200, 100)
                batten_end_bool = False
        if event.type == pygame.MOUSEBUTTONDOWN and batten_end_bool:
            con = sqlite3.connect("game_base.db")
            cur = con.cursor()

            result = cur.execute(f"""SELECT mouse, mouse_vision, sens, keyboard, sound, settings.id
                                     FROM settings, password
                                     WHERE password.id = settings.id AND login = '{login_ps}'
                """).fetchall()[0]
            con.close()

            music_menu.play()

            menu = Menu(screen, music_menu)
            menu.active = False

            menu.mouse = int(result[0])
            menu.mouse_vision = int(result[1])
            menu.settings_sens = float(result[2])
            if menu.settings_sens == 0.001:
                menu.mass_setting_sens_index = "Низкая"
            elif menu.settings_sens == 0.005:
                menu.mass_setting_sens_index = "Средняя"
            else:
                menu.mass_setting_sens_index = "Высокая"
            menu.keyboard = int(result[3])
            menu.settings_sound = float(result[4])
            if menu.settings_sound == 0:
                menu.mass_setting_sound_index = "Нет"
            elif menu.settings_sound == 0.1:
                menu.mass_setting_sound_index = "Низкая"
            elif menu.settings_sound == 0.5:
                menu.mass_setting_sound_index = "Средняя"
            else:
                menu.mass_setting_sound_index = "Высокая"

            menu.id_ = result[-1]
            menu.active = True

            player = Player(screen, mass=mass, mouse=True)
            sprite = Sprites()
            running = True
            textures = {
                '1': pygame.image.load('Texture/5.png').convert(),
                '2': pygame.image.load('Texture/15.png').convert(),
                '3': pygame.image.load('Texture/030.png').convert(),
                '4': pygame.image.load('Texture/wall.jpg').convert()
            }
            textures_ = {
                '1': ['Texture/5.png', 'Texture/15.png'],
                '2': ['Texture/4.png', 'Texture/14.png'],
                '3': ['Texture/6.png', 'Texture/16.png'],
                '4': ['Texture/5.png', 'Texture/200.png']
            }

            COLOR_ = (69, 71, 48)
            MYEVENTTYPE = pygame.USEREVENT + 1
            sprite_movements(8, 12, sprite)
            sky_ = choice([i for i in range(1, 9)])
            pygame.time.set_timer(MYEVENTTYPE, 1500)
            true = False
            number_sprite = 1
            hall = 1
            sprite_true = True
            sprite_true_2 = True
            sprite_true_3 = True
            hall_4 = False
            clearing_hall_4 = True
            color_batten_further = (125, 170, 200)
            batten_further_bool = False
            color_batten_menu = (125, 170, 200)
            batten_menu_bool = False
            color_batten_again = (125, 170, 200)
            batten_again_bool = False

            end = False
            color_batten_end = (100, 200, 100)
            batten_end_bool = False

            time_to_destroy_the_lizun = False
            true_timer = False
            timer = 0
            start = 0

            metronome = pygame.mixer.Sound('Music/метроном.ogg')
            metronome.stop()

            sos = pygame.mixer.Sound('Music/сигнал.ogg')
            sos.stop()

            result_payer = True
            field_, player.mass = beginning()
            number_of_caught_new()

        menu.actions(event)
    # таймер
    if true_timer:
        true_timer = False
        start = perf_counter()

    if timer == 0:
        if start != 0:
            end_time = perf_counter()
            if round(end_time - start) % 31 == 28:
                sos.play()
            if round(end_time - start) % 31 == 30:
                time_to_destroy_the_lizun = True
                start = perf_counter()

    if menu.active_2:
        menu.active = True
    else:
        menu.active = False
    if menu.active:
        screen.fill((0, 0, 0))
        menu.visualization()
        player.sens = menu.settings_sens
        player.mouse = menu.mouse
        player.mouse_vision = menu.mouse_vision
        player.keyboard = menu.keyboard

        player.music_bg.set_volume(menu.settings_sound)
        player.music_fon.set_volume(menu.settings_sound)
        player.music_schag.set_volume(menu.settings_sound)
        music_(menu.settings_sound)

        pygame.display.flip()
        clock.tick(60)
        continue

    else:
        menu_active = False
        music_menu.stop()

    player.motion()  # движение игрока
    screen.fill((0, 0, 0))
    sky = pygame.image.load(f'Sky/{sky_}.png').convert()
    screen.blit(sky, (0, 0))
    pygame.draw.rect(screen, COLOR_, (0, 420, 1200, 380))
    walls = vision_new(player.x, player.y, player.angle, textures, field_)
    world(screen, walls + [obj.object_locate(player, walls) for obj in sprite.list_of_objects])
    catch_a_lizun(player.x, player.y, sprite)
    lizun(screen, true)
    ball(screen, hall)
    true = False
    if transition(player.x, player.y, field_) and number() >= number_sprite and not hall_4:
        # возможность выхода в дверь
        player.new_hall(150, 150)
        hall += 1
        textures["1"] = pygame.image.load(textures_[str(hall)][0]).convert()
        textures["2"] = pygame.image.load(textures_[str(hall)][1]).convert()
        sky_ = choice([i for i in range(1, 9)])
        sky = pygame.image.load(f'Sky/{sky_}.png').convert()
        screen.blit(sky, (0, 0))
        if hall == 2 and sprite_true:
            number_sprite = 4
            sprite_true = False
            set_caught_()
            sprite.list_of_objects = [
                SpriteObject(sprite.sprite_types['s'], True, (8.5, 12.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (5.5, 20.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (13.5, 2.5), 0.8, 0.8)
            ]
            sprite.sprite_types_pos = {
                's2': (8, 12),
                's3': (5, 20),
                's4': (13, 2)
            }
        if hall == 3 and sprite_true_2:
            sprite_true_2 = False
            number_sprite = 4
            set_caught_()
            sprite.list_of_objects = [
                SpriteObject(sprite.sprite_types['s'], True, (8.5, 12.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (5.5, 20.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (13.5, 2.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (2.5, 20.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (4.5, 11.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (2.5, 8.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (12.5, 16.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (5.5, 3.5), 0.8, 0.8)
            ]
            sprite.sprite_types_pos = {
                's5': (8, 12),
                's6': (5, 20),
                's7': (13, 2),
                'rot': (2, 20),
                'rot2': (4, 11),
                'rot3': (3, 8),
                'rot4': (12, 16),
                'rot5': (5, 3)
            }
        if hall == 4:
            sprite_true_3 = False
            hall_4 = True
    if hall_4:
        if clearing_hall_4:
            clearing_hall_4 = False
            true_timer = True
            set_caught_()
            sprite.list_of_objects = [
                SpriteObject(sprite.sprite_types['s'], True, (30.5, 30.5), 0.0, 0.0)
            ]
            sprite.sprite_types_pos = {
                's': (30, 30)
            }
            field_, mass = hall_4_()
            player.mass = mass
            metronome.play(-1)

    if hall_4:
        if transition_4(player.x, player.y, field_) == "2":
            player.active = False
            if number() >= 1:
                end = True
        elif time_to_destroy_the_lizun:
            time_to_destroy_the_lizun = False
            time_to_destroy_the_lizun_()

    if not player.active and not end:
        pygame.draw.rect(screen, color_batten_further,
                         (535, 250, 220, 80), 0)

        font = pygame.font.Font(None, 60)
        text = font.render(f"Далее", True, (10, 10, 10))
        screen.blit(text, (565, 270))

        pygame.draw.rect(screen, color_batten_menu,
                         (535, 350, 220, 80), 0)
        font = pygame.font.Font(None, 60)
        text = font.render(f"Меню", True, (10, 10, 10))
        screen.blit(text, (575, 370))

        pygame.draw.rect(screen, color_batten_again,
                         (535, 450, 220, 80), 0)
        font = pygame.font.Font(None, 60)
        text = font.render(f"Заново", True, (10, 10, 10))
        screen.blit(text, (575, 470))
    if end:  # конец игры
        if result_payer:
            result_payer = False
            con = sqlite3.connect("game_base.db")
            cur = con.cursor()
            res = cur.execute(f''' 
                                SELECT count FROM password
                                WHERE login = '{login_ps}'
                                            ''').fetchall()[0][0]
            if int(res) < int(number()):
                cur.execute(f"""UPDATE password
                                SET count = '{number()}'
                                WHERE login = '{login_ps}'""")
                con.commit()
            con.close()
        player.music_schag.stop()
        sky = pygame.image.load(f'Texture/205.png').convert()
        screen.blit(sky, (0, 0))
        metronome.stop()
        timer = 0
        start = 0
        pygame.draw.rect(screen, color_batten_end, (940, 710, 220, 80), 0)

        font = pygame.font.Font(None, 60)
        text = font.render(f"Далее", True, (50, 10, 10))
        screen.blit(text, (955, 720))

        font = pygame.font.Font(None, 100)
        text = font.render(f"{number()}", True, (230, 30, 10))
        screen.blit(text, (535, 735))

    pygame.display.flip()
    clock.tick(60)
