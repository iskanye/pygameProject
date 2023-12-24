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
        self.camera.load_map(Map('test.tmx'))

        self.player = Player(self.camera)
        self.player.set_pos(*self.camera.player_pos)
        self.camera.add(self.player, layer=PLAYER_LAYER)

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        self.clock.tick(FPS)
        self.camera.draw(self.screen)
        self.player.update()
        pg.display.flip()
