import objects.base_object
from settings import *


class Door(objects.base_object.BaseObject):
    def __init__(self):
        super().__init__()
        self.images = tuple(load_sprite(f'door/{i}.png') for i in range(1, 4))
        self.rect = pg.Rect(0, 0, TILE * 2, TILE * 2)
        self.pivot = pg.Vector2(TILE, TILE * 3)
        self.set_image(self.images[0], (2, 3))
