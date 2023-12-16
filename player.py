import pygame as pg
from settings import *
from utils import *


class Player(pg.sprite.GroupSingle):
    def __init__(self):
        super().__init__()
        self.idle_images = (
            load_sprite('player/idle/right.png'),
            load_sprite('player/idle/up.png'),
            load_sprite('player/idle/left.png'),
            load_sprite('player/idle/down.png')
        )
        self.moving_images = (
            tuple(load_sprite(f'player/movement/right{i + 1}.png') for i in range(6)),
            tuple(load_sprite(f'player/movement/up{i + 1}.png') for i in range(6)),
            tuple(load_sprite(f'player/movement/left{i + 1}.png') for i in range(6)),
            tuple(load_sprite(f'player/movement/down{i + 1}.png') for i in range(6))
        )
        self.animation_frame = 0
        self.sprite = pg.sprite.Sprite()
        self.sprite.image = None
        self.sprite.rect = pygame.Rect((WIDTH - TILE * PLAYER_SIZE) / 2,
                                       (HEIGHT - TILE * PLAYER_SIZE) / 2,
                                       TILE * PLAYER_SIZE, TILE * PLAYER_SIZE)
        self.set_image(self.idle_images[0], PLAYER_SIZE)
        self.direction = pg.math.Vector2(1, 0)
        self.moving = False

    def set_image(self, image, scale):
        self.sprite.image = pg.transform.scale(image, (TILE * scale, TILE * scale))

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
            self.sprite.rect.x += self.direction.x * PLAYER_SPEED / FPS
            self.sprite.rect.y += self.direction.y * PLAYER_SPEED / FPS

    def animation(self):
        if not self.moving:
            if self.direction.y > 0:
                self.set_image(self.idle_images[3], PLAYER_SIZE)
            elif self.direction.y < 0:
                self.set_image(self.idle_images[1], PLAYER_SIZE)
            if self.direction.x > 0:
                self.set_image(self.idle_images[0], PLAYER_SIZE)
            elif self.direction.x < 0:
                self.set_image(self.idle_images[2], PLAYER_SIZE)
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
            self.set_image(image_set[self.animation_frame // ANIM_FRAME_DURATION], PLAYER_SIZE)

    def update(self):
        self.user_input()
        self.movement()
        self.animation()
