from sprite import SpriteObject


# размещение и уничтожение лизуна
def sprite_movements(x, y, sprite, sprite_type=('s', 0), cleaning=False, view='s'):
    if not cleaning:
        sprite.list_of_objects[sprite_type[1]] = SpriteObject(sprite.sprite_types[view]
                                                              , True, (x + 0.5, y + 0.5), 0.8, 0.8)
    else:
        sprite.list_of_objects[sprite_type[1]] = SpriteObject(sprite.sprite_types[view]
                                                              , True, (x + 0.5, y + 0.5), 0.0, 0.0)
    sprite.sprite_types_pos[sprite_type[0]] = x, y


cor_x, cor_y = 1, 5
cor_x2, cor_y2 = 1, 1
x, y = cor_x, cor_y
