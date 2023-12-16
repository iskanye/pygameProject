from player import *
from utils import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    clock = pygame.time.Clock()
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update()
        pygame.display.flip()
