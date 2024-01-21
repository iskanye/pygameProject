import objects.base_object
import objects.prefabs
from settings import *


class Map:
    def __init__(self, map_name):
        tmx_map = load_map(map_name)
        self.layers = dict()
        for layer in range(len(tmx_map.layers)):
            if callable(getattr(tmx_map.layers[layer], "tiles", None)):
                for x, y, tile in tmx_map.layers[layer].tiles():
                    sprite = pg.sprite.Sprite()
                    sprite.image = pg.transform.scale(tile, (TILE, TILE))
                    sprite.rect = pg.rect.Rect(x * TILE, y * TILE,
                                               TILE, TILE)
                    self.layers[layer] = self.layers.get(layer, []) + [sprite]
            else:
                for obj in tmx_map.layers[layer]:
                    if obj.type in objects.prefabs.PREFABS:
                        _object = objects.prefabs.PREFABS[obj.type](**obj.properties)
                        _object.rect.topleft = obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR
                    else:
                        _object = objects.base_object.BaseObject()
                        _object.image = pg.transform.scale(obj.image, (obj.width * SCALE_FACTOR
                                                                       , obj.height * SCALE_FACTOR))
                        _object.rect = pg.rect.Rect(obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR,
                                                    obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR)
                        if obj.type == 'player':
                            self.player_pos = (_object.rect.x + TILE / 2 - PLAYER_SIZE[0] * TILE / 2,
                                               _object.rect.y - PLAYER_SIZE[1] * TILE * 0.6)
                        if 'collision_rect' in obj.properties:
                            _object._collision_rect = pg.rect.Rect(*map(lambda a: float(a) * TILE,
                                                                        obj.properties['collision_rect'].split(';')))
                        if 'pivot' in obj.properties:
                            _object.pivot = pg.Vector2(*map(lambda a: float(a) * TILE,
                                                            obj.properties['pivot'].split(';')))
                    self.layers[layer] = self.layers.get(layer, []) + [_object]
