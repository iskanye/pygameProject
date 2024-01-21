import objects.base_object
from settings import *


class LevelChangeTrigger(objects.base_object.BaseObject):
    def __init__(self, **kwargs):
        super().__init__()

        self._trigger_rect = pg.Rect(0, 0, TILE, TILE)
        self.level = kwargs['level']

    def trigger(self, player):
        player.game.load_map(self.level)
