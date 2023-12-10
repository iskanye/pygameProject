import pygame
from settings import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
