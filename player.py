from math import sin, cos, pi, tan
from field import *
import pygame


DIST = 300 / (2 * tan((pi / 3) / 2))


class Player:
    def __init__(self, screen, mass=mass, x=150, y=150, mouse=False, sens=0.005, mouse_vision=True, keyboard=True):
        pygame.mouse.set_visible(mouse_vision)

        self.keyboard = keyboard
        self.mouse_vision = mouse_vision
        self.x, self.y = x, y
        self.mass = mass
        self.angle = 0
        self.screen = screen
        self.mouse = mouse
        self.sens = sens
        self.active = True
        self.true = False
        self.true2 = False
        self.music_schag = pygame.mixer.Sound('Music/шаги.ogg')
        self.music_schag.stop()

        self.music_fon = pygame.mixer.Sound('Music/ф1.ogg')
        self.music_fon.set_volume(0.5)
        self.fon_ps = True

        self.bg = False
        self.bg_2 = False
        self.music_bg = pygame.mixer.Sound("Music/бег.ogg")
        self.music_bg.stop()

    def display(self, screen):  # отображение игрока
        pygame.draw.circle(screen, ((145, 230, 145)), (self.x, self.y), 8)
        pygame.draw.line(screen, ((120, 150, 200)), (self.x, self.y), (self.x + 1250 * cos(self.angle),
                                                                        self.y + 900 * sin(self.angle)))

    # новый зал
    def new_hall(self, x, y):
        self.x, self.y = x, y

    def motion(self):  # движение игрока
        self.true = False
        self.bg = False
        if self.active:
            if self.fon_ps:
                self.fon_ps = False
                self.music_fon.play(-1)
            pygame.mouse.set_visible(self.mouse_vision)
            if self.mouse:
                pygame.mouse.get_pos()
                difference = pygame.mouse.get_pos()[0] - 600
                pygame.mouse.set_pos((600, 400))
                self.angle += difference * self.sens
            if self.keyboard:
                if pygame.key.get_pressed()[pygame.K_LEFT]:  # влево от луча
                    x = self.x + 4 * cos(self.angle - pi / 2)
                    y = self.y + 4 * sin(self.angle - pi / 2)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle - pi / 2)) // 100 * 100,
                             (y + 40 * sin(self.angle - pi / 2)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y
                        self.true = True

                if pygame.key.get_pressed()[pygame.K_RIGHT]:  # вправо от луча
                    x = self.x + 4 * cos(self.angle + pi / 2)
                    y = self.y + 4 * sin(self.angle + pi / 2)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle + pi / 2)) // 100 * 100,
                             (y + 40 * sin(self.angle + pi / 2)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y
                        self.true = True

                if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
                    x = self.x + 4 * cos(self.angle)
                    y = self.y + 4 * sin(self.angle)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle)) // 100 * 100, (y + 40 * sin(self.angle)) // 100 * 100) \
                            not in self.mass:
                        self.x = x
                        self.y = y
                        self.true = True

                if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
                    x = self.x + 5 * cos(self.angle)
                    y = self.y + 5 * sin(self.angle)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 50 * cos(self.angle)) // 100 * 100, (y + 50 * sin(self.angle)) // 100 * 100) \
                            not in self.mass:
                        self.x = x
                        self.y = y
                        self.bg = True
                        self.true = False

                if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:  # назад от луча
                    x = self.x + 4 * cos(self.angle + pi)
                    y = self.y + 4 * sin(self.angle + pi)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle + pi)) // 100 * 100,
                             (y + 40 * sin(self.angle + pi)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y
                        self.true = True

                if pygame.key.get_pressed()[pygame.K_a]:
                    self.angle -= 0.05
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.angle += 0.05
            else:
                if pygame.key.get_pressed()[pygame.K_a]:  # влево от луча
                    x = self.x + 4 * cos(self.angle - pi / 2)
                    y = self.y + 4 * sin(self.angle - pi / 2)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle - pi / 2)) // 100 * 100,
                             (y + 40 * sin(self.angle - pi / 2)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y
                        self.true = True

                if pygame.key.get_pressed()[pygame.K_d]:  # вправо от луча
                    x = self.x + 4 * cos(self.angle + pi / 2)
                    y = self.y + 4 * sin(self.angle + pi / 2)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle + pi / 2)) // 100 * 100,
                             (y + 40 * sin(self.angle + pi / 2)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y
                        self.true = True

                if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
                    x = self.x + 4 * cos(self.angle)
                    y = self.y + 4 * sin(self.angle)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle)) // 100 * 100,
                             (y + 40 * sin(self.angle)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y

                if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
                    x = self.x + 5 * cos(self.angle)
                    y = self.y + 5 * sin(self.angle)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 50 * cos(self.angle)) // 100 * 100,
                             (y + 50 * sin(self.angle)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y
                        self.bg = True
                        self.true = False

                if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:  # назад от луча
                    x = self.x + 4 * cos(self.angle + pi)
                    y = self.y + 4 * sin(self.angle + pi)
                    if (x // 100 * 100, y // 100 * 100) not in self.mass and \
                            ((x + 40 * cos(self.angle + pi)) // 100 * 100,
                             (y + 40 * sin(self.angle + pi)) // 100 * 100) not in self.mass:
                        self.x = x
                        self.y = y
                        self.true = True

                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.angle -= 0.05
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.angle += 0.05

            self.angle %= pi * 2
            # звук при движении
            if self.bg:
                self.true = False
            if self.true:
                if not self.true2:
                    self.music_schag.play(-1)
                self.true2 = self.true
            else:
                self.music_schag.stop()
                self.true2 = self.true
            if self.bg:
                if not self.bg_2:
                    self.music_bg.play(-1)
                self.bg_2 = True
            else:
                self.music_bg.stop()
                self.bg_2 = False
        else:
            pygame.mouse.set_visible(True)
            self.fon_ps = True
            self.bg = False
            self.bg_2 = False
            self.music_bg.stop()
            self.music_fon.stop()

    def verification_of_correctness(self, walls, x, y):
        for i in walls:
            if i[1] * 100 - 8 <= x <= i[1] * 100 + 108 and i[0] * 100 - 8 <= y <= i[0] * 100 + 108:
                return False
        return True


def mapping(a, b):
    return (a // 100) * 100, (b // 100) * 100


wall_column = 0


# для отрисовки
def vision_new(x_pl, y_pl, player_angle, textures, field_):
    global wall_column
    walls = []
    fov = pi / 3
    ox, oy = x_pl, y_pl
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - fov / 2
    texture_v, texture_h = 1, 1
    for ray in range(350):
        sin_a = sin(cur_angle)
        cos_a = cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        x, dx = (xm + 100, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, 2500, 100):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in field_:
                texture_v = field_[tile_v]
                break
            x += dx * 100

        y, dy = (ym + 100, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, 1500, 100):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in field_:
                texture_h = field_[tile_h]
                break
            y += dy * 100

        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % 100
        depth *= cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int((3 * DIST * 100) / depth), 5 * 800)

        try:
            wall_column = textures[texture].subsurface(offset * (1200 // 100), 0, 1200 // 100, 1200)
            wall_column = pygame.transform.scale(wall_column, (1200 // 300, proj_height))
            wall_pos = (ray * (1200 // 300), 400 - proj_height // 2)
            walls.append((depth, wall_column, wall_pos))
        except Exception:
            pass

        cur_angle += fov / 300
    return walls


def world(screen, world_objects):
    for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
        if obj[0]:
            i, object, object_pos = obj
            screen.blit(object, object_pos)
