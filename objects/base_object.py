from settings import *


class BaseObject(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = None
        self.rect = pg.rect.Rect(0, 0, 0, 0)
        self.pivot = NO_PIVOT
        self._collision_rect = NO_RECT
        self._interaction_rect = NO_RECT

    def position(self):
        return self.rect.topleft + self.pivot

    def collision_rect(self):
        return self._collision_rect.move(self.rect.topleft) if self._collision_rect != NO_RECT else None

    def interaction_rect(self):
        return self._interaction_rect.move(self.rect.topleft) if self._interaction_rect != NO_RECT else None

    def interact(self, player):
        pass

    def set_image(self, image, scale):
        self.image = pg.transform.scale(image, (TILE * scale[0], TILE * scale[1]))
