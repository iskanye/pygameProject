import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pg.image.load('sprites/player/idle/down.png').convert_alpha()
        self.image = pg.transform.scale(img, (TILE * 4, TILE * 4))
        self.direction = pg.math.Vector2(0, 0)
