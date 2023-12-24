from utils import *
from settings import *
from map import Map
from player import Player
from camera import Camera


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        self.clock = pg.time.Clock()

        self.camera = Camera()

        self.player = Player(self.camera)
        self.camera.add(self.player, layer=PLAYER_LAYER)

        self.load_map('test.tmx')

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        self.clock.tick(FPS)
        self.screen.fill(BACKGROUND_COLOR)
        self.camera.draw(self.screen)
        pg.draw.rect(self.screen, pg.Color('blue'), self.player.rect, 1)
        self.player.update()
        pg.display.flip()

    def load_map(self, map):
        self.camera.load_map(Map(map))
        self.player.set_pos(*self.camera.player_pos)
