import objects.base_object
from settings import *


class Door(objects.base_object.BaseObject):
    def __init__(self, **kwargs):
        super().__init__()
        self.images = tuple(load_sprite(f'door/{i}.png') for i in range(1, 4))
        self.pivot = pg.Vector2(TILE, TILE * 3)
        self.set_image(self.images[0], (2, 3))

        self.rect = pg.Rect(0, 0, TILE * 2, TILE * 3)
        self._collision_rect = pg.Rect(0, TILE * 2, TILE * 2, TILE)
        self._interaction_rect = pg.Rect(0, TILE * 1.75, TILE * 2, TILE * 1.5)

        self.open = False
        self.animation_frame = 0

    def interact(self, player):
        self.open = True
        self._interaction_rect = NO_RECT

    def animation(self):
        if self.open and self.animation_frame < 3 * ANIM_FRAME_DURATION - 1:
            self.animation_frame = (self.animation_frame + 1) % (3 * ANIM_FRAME_DURATION)
            self.set_image(self.images[self.animation_frame // ANIM_FRAME_DURATION], (2, 3))
        elif self.animation_frame == 3 * ANIM_FRAME_DURATION - 1:
            self.open = False
            self._collision_rect = NO_RECT

    def update(self):
        self.animation()


