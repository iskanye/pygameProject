import map
from player import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)

        self.clock = pg.time.Clock()
        self.player = Player()
        self.map = map.Map('test.tmx')

    def update(self):
        for event in pg.event.get():
            if event.type == pygame.QUIT:
                pg.quit()
                exit()
        self.clock.tick(FPS)
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        self.player.draw(self.screen)
        self.player.update()
        pg.display.flip()
