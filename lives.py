import objects.base_object
from settings import *


class Lives(objects.base_object.BaseObject):
    def __init__(self, game):
        super().__init__()
        self.images = tuple(load_sprite(f'hearts/{i + 1}.png') for i in range(6))

        self.set_image(self.images[0], (2, 2))
        self.rect = pg.Rect(0, 0, TILE * 2, TILE * 2)
        self.lives = 2
        self.animation_frame = 0
        self.game = game

        self.damaged = False
        self.timer = 0

    def animation(self):
        if self.lives == 2:
            self.animation_frame = (self.animation_frame + 1) % (6 * ANIM_FRAME_DURATION)
            self.set_image(self.images[self.animation_frame // (ANIM_FRAME_DURATION * 2)], (2, 2))
        elif self.lives == 1:
            self.animation_frame = (self.animation_frame + 1) % (3 * ANIM_FRAME_DURATION)
            self.set_image(self.images[self.animation_frame // ANIM_FRAME_DURATION + 3], (2, 2))

    def damage_countdown(self):
        if self.damaged:
            self.timer += 1
        if self.timer >= FPS:
            self.timer = 0
            self.damaged = False

    def update(self):
        self.animation()
        self.damage_countdown()

    def take_damage(self):
        if self.damaged:
            return
        self.lives -= 1
        self.damaged = True
        if self.lives == 0:
            self.game.load_map(self.game.current_level)

    def restore_health(self):
        self.lives = 2
