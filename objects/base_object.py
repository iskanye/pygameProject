from settings import *


class BaseObject(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = None
        self.rect = pg.rect.Rect(0, 0, 0, 0)
        self.pivot = NO_PIVOT

    def position(self):
        return self.rect.topleft + self.pivot

    def set_image(self, image, scale):
        self.image = pg.transform.scale(image, (TILE * scale[0], TILE * scale[1]))
