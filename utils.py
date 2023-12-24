import pygame as pg
from pytmx.util_pygame import load_pygame


def load_sprite(name):
    return pg.image.load(f'sprites/{name}').convert_alpha()


def load_map(name):
    return load_pygame(f'maps/{name}')
