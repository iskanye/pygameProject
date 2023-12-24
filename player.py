from utils import *
from settings import *


class Player(pg.sprite.GroupSingle):
    def __init__(self, camera):
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
        self.sprite.rect = pg.Rect((WIDTH - TILE * PLAYER_SIZE) / 2,
                                   (HEIGHT - TILE * PLAYER_SIZE) / 2,
                                   TILE * PLAYER_SIZE, TILE * PLAYER_SIZE)
        self.rect = pg.rect.Rect(self.sprite.rect.x + 37 * SCALE_FACTOR, self.sprite.rect.y + 74 * SCALE_FACTOR,
                                 23 * SCALE_FACTOR, 8 * SCALE_FACTOR)
        self.set_image(self.idle_images[0], PLAYER_SIZE)
        self.direction = pg.math.Vector2(1, 0)
        self.moving = False
        self.camera = camera

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

    def velocity(self):
        return self.direction * PLAYER_SPEED / FPS

    def movement(self):
        if self.moving:
            velocity = self.velocity()
            rect_x = pg.rect.Rect(self.rect.x + velocity.x, self.rect.y,
                                  self.rect.width, self.rect.height)
            rect_y = pg.rect.Rect(self.rect.x, self.rect.y + velocity.y,
                                  self.rect.width, self.rect.height)
            for i in self.camera.get_sprites_from_layer(COLLISION_LAYER):
                if rect_x.colliderect(i.rect):
                    velocity.x = 0
                if rect_y.colliderect(i.rect):
                    velocity.y = 0
            self.camera.update_player_pos(*velocity)

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

    def set_pos(self, x, y):
        self.camera.update_player_pos(x - self.sprite.rect.x, y - self.sprite.rect.y)
