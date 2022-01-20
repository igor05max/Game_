import pygame
import math
from player import DIST


# создание лизунов
class Sprites:
    def __init__(self):
        self.sprite_types = {
            's': pygame.image.load('lisun.png').convert_alpha(),
            'rot': pygame.image.load('lisun_red.png').convert_alpha()
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['s'], True, (1.5, 2.5), 0.8, 0.8)
        ]
        self.sprite_types_pos = {
            's': (1, 1)
        }


class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * 100, pos[1] * 100
        self.shift = shift
        self.scale = scale

    # для отрисовки
    def object_locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += math.pi * 2

        delta_rays = int(gamma / (math.pi / 3 / 300))
        current_ray = (300 // 2 - 1) + delta_rays
        distance_to_sprite *= math.cos(math.pi / 3 / 2 - current_ray * (math.pi / 3 / 300))
        try:
            if 0 <= current_ray <= 300 - 1 and distance_to_sprite < walls[current_ray][0]:
                proj_height = min(int(3 * DIST * 100 / distance_to_sprite * self.scale), 2 * 800)
                half_proj_height = proj_height // 2
                shift = half_proj_height * self.shift

                sprite_pos = (current_ray * 4 - half_proj_height, 400 - half_proj_height + shift)
                sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
                return (distance_to_sprite, sprite, sprite_pos)
            else:
                return (False, )
        except Exception:
            return (False, )
