import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idle_images = (
            pg.image.load('sprites/player/idle/right.png').convert_alpha(),
            pg.image.load('sprites/player/idle/up.png').convert_alpha(),
            pg.image.load('sprites/player/idle/left.png').convert_alpha(),
            pg.image.load('sprites/player/idle/down.png').convert_alpha()
        )
        self.moving_images = (
            tuple(pg.image.load(f'sprites/player/movement/right{i + 1}.png').convert_alpha() for i in range(6)),
            tuple(pg.image.load(f'sprites/player/movement/up{i + 1}.png').convert_alpha() for i in range(6)),
            tuple(pg.image.load(f'sprites/player/movement/left{i + 1}.png').convert_alpha() for i in range(6)),
            tuple(pg.image.load(f'sprites/player/movement/down{i + 1}.png').convert_alpha() for i in range(6))
        )
        self.animation_frame = 0
        self.image = None
        self.rect = (0, 0)
        self.set_image(self.idle_images[0], 4)
        self.direction = pg.math.Vector2(1, 0)
        self.pos = pg.math.Vector2(WIDTH - self.rect[0], HEIGHT - self.rect[1]) / 2
        self.moving = False

    def set_image(self, image, scale):
        self.image = pg.transform.scale(image, (TILE * scale, TILE * scale))
        self.rect = (TILE * scale, TILE * scale)

    def user_input(self):
        keys = pg.key.get_pressed()
        direction = pg.math.Vector2(0, 0)

        if keys[pg.K_w]:
            direction.y = -1
        if keys[pg.K_s]:
            direction.y = 1
        if keys[pg.K_d]:
            direction.x = 1
        if keys[pg.K_a]:
            direction.x = -1

        if direction.length_squared() != 0:
            self.moving = True
            self.direction = direction.normalize()
        else:
            self.moving = False

    def movement(self):
        if self.moving:
            self.pos += self.direction * SPEED / FPS

    def animation(self):
        if not self.moving:
            if self.direction.y > 0:
                self.set_image(self.idle_images[3], 4)
            elif self.direction.y < 0:
                self.set_image(self.idle_images[1], 4)
            if self.direction.x > 0:
                self.set_image(self.idle_images[0], 4)
            elif self.direction.x < 0:
                self.set_image(self.idle_images[2], 4)
        else:
            image_set = ()
            if self.direction.y > 0:
                image_set = self.moving_images[3]
            elif self.direction.y < 0:
                image_set = self.moving_images[1]
            if self.direction.x > 0:
                image_set = self.moving_images[0]
            elif self.direction.x < 0:
                image_set = self.moving_images[2]
            self.animation_frame = (self.animation_frame + 1) % (6 * ANIM_FRAME_DURATION)
            self.set_image(image_set[self.animation_frame // ANIM_FRAME_DURATION], 4)

    def update(self):
        self.user_input()
        self.movement()
        self.animation()
