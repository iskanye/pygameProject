import pygame as pg
from utils import *
from settings import *


class Map(pg.sprite.LayeredUpdates):
    def __init__(self, map_name):
        super().__init__()
        map = load_map(map_name)
        for layer in range(len(map.layers)):
            for x, y, tile in map.layers[layer].tiles():
                sprite = pg.sprite.Sprite()
                sprite.image = pg.transform.scale(tile, (TILE, TILE))
                sprite.rect = tile.get_rect()
                sprite.rect.x = x * TILE
                sprite.rect.y = y * TILE
                self.add(sprite, layer=layer)
