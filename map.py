import objects.base_object
from settings import *


class Map:
    def __init__(self, map_name):
        map = load_map(map_name)
        self.layers = dict()
        for layer in range(len(map.layers)):
            if callable(getattr(map.layers[layer], "tiles", None)):
                for x, y, tile in map.layers[layer].tiles():
                    sprite = pg.sprite.Sprite()
                    sprite.image = pg.transform.scale(tile, (TILE, TILE))
                    sprite.rect = pg.rect.Rect(x * TILE, y * TILE,
                                               TILE, TILE)
                    self.layers[layer] = self.layers.get(layer, []) + [sprite]
            else:
                for obj in map.layers[layer]:
                    _object = objects.base_object.BaseObject()
                    _object.image = pg.transform.scale(obj.image, (obj.width * SCALE_FACTOR
                                                                   , obj.height * SCALE_FACTOR))
                    _object.rect = pg.rect.Rect(obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR,
                                                obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR)
                    if obj.type == 'player':
                        self.player_pos = (_object.rect.x + TILE / 2 - PLAYER_SIZE * TILE / 2,
                                           _object.rect.y - PLAYER_SIZE * TILE * 0.6)
                    self.layers[layer] = self.layers.get(layer, []) + [_object]
