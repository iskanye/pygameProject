import objects.base_object
from settings import *


class TriggerSpike(objects.base_object.BaseObject):
    def __init__(self, **kwargs):
        super().__init__()
        self.images = ([load_sprite(f'trigger_spike/{i}.png') for i in range(1, 5)] +
                       [load_sprite(f'trigger_spike/2.png')])
        self.set_image(self.images[0], (1, 1))

        self._trigger_rect = pg.Rect(0.1 * TILE, 0.1 * TILE, 0.8 * TILE, 0.8 * TILE)

        self.triggered = False
        self.damaging = False

        self.timer = 0
        self.animation_frame = 0

    def trigger(self, player):
        if not self.triggered:
            self.triggered = True
            self.set_image(self.images[1], (1, 1))
        elif self.damaging:
            player.lives.take_damage()

    def animation(self):
        if self.damaging and self.animation_frame < 3 * ANIM_FRAME_DURATION - 1:
            self.animation_frame = (self.animation_frame + 1) % (3 * ANIM_FRAME_DURATION)
            self.set_image(self.images[self.animation_frame // ANIM_FRAME_DURATION + 2], (1, 1))

    def cycle(self):
        if self.triggered and self.timer < 0.75 * FPS and not self.damaging:
            self.timer += 1

        elif self.triggered and self.timer >= 0.75 * FPS:
            self.timer = 0
            self.damaging = True

        elif self.damaging and self.animation_frame >= 3 * ANIM_FRAME_DURATION - 1:
            self.animation_frame = 0
            self.damaging = False
            self.triggered = False
            self.set_image(self.images[0], (1, 1))

    def update(self):
        self.cycle()
        self.animation()



