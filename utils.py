import pygame


def load_sprite(name):
    return pygame.image.load(f'sprites/{name}').convert_alpha()
