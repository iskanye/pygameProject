from utils import *
from settings import *


class Camera(pg.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()
        self.player_pos = (0, 0)

    def load_map(self, map):
        self.player_pos = map.player_pos
        for layer, obj in map.layers.items():
            self.add(obj, layer=layer)

    def update_player_pos(self, delta_x, delta_y):
        for layer in self.layers():
            if layer != PLAYER_LAYER:
                for sprite in self.get_sprites_from_layer(layer):
                    sprite.rect.x -= delta_x
                    sprite.rect.y -= delta_y
