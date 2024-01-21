from settings import *
from map import Map
from player import Player
from camera import Camera
from lives import Lives


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        self.clock = pg.time.Clock()
        self.current_level = ''

        self.camera = Camera()

        self.player = Player(self.camera, self)
        self.camera.add(self.player, layer=PLAYER_LAYER)

        self.lives = Lives()
        self.camera.add(self.lives, layer=UI_LAYER)

        try:
            with open('save.txt', 'rt') as f:
                self.load_map(f.readline().strip())
        except FileNotFoundError:
            self.load_map('level1.tmx')

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                with open('save.txt', 'wt') as f:
                    print(self.current_level, file=f)
                pg.quit()
                exit()
        self.clock.tick(FPS)
        self.screen.fill(BACKGROUND_COLOR)
        self.camera.draw(self.screen)
        pg.draw.rect(self.screen, pg.Color('blue'), self.player.collision_rect, 1)
        pg.draw.circle(self.screen, pg.Color('blue'), self.player.position(), 2)
        self.camera.update()
        pg.display.flip()

    def load_map(self, map):
        self.current_level = map
        self.camera.unload_map()
        self.camera.load_map(Map(map))
        self.player.set_pos(*self.camera.player_pos)
