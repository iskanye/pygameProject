from utils import *
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
                    sprite.rect = tile.get_rect()
                    sprite.rect.x = x * TILE
                    sprite.rect.y = y * TILE
                    self.layers[layer] = self.layers.get(layer, []) + [sprite]
            else:
                for obj in map.layers[layer]:
                    sprite = pg.sprite.Sprite()
                    sprite.image = pg.transform.scale(obj.image, (obj.width * SCALE_FACTOR
                                                                  , obj.height * SCALE_FACTOR))
                    sprite.rect = obj.image.get_rect()
                    sprite.rect.x = obj.x * SCALE_FACTOR
                    sprite.rect.y = obj.y * SCALE_FACTOR
                    if obj.type == 'player':
                        self.player_pos = (sprite.rect.x + sprite.rect.width - TILE * PLAYER_SIZE / 2,
                                           sprite.rect.y + sprite.rect.height * 2 - TILE * PLAYER_SIZE)
                    self.layers[layer] = self.layers.get(layer, []) + [sprite]
