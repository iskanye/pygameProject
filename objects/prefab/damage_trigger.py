import objects.base_object
from settings import *


class DamageTrigger(objects.base_object.BaseObject):
    def __init__(self, **kwargs):
        super().__init__()
        self.set_image(kwargs['image'], (1, 1))

        self._trigger_rect = pg.rect.Rect(*map(lambda a: float(a) * TILE,
                                               kwargs['trigger_rect'].split(';')))

    def trigger(self, player):
        player.lives.take_damage()
