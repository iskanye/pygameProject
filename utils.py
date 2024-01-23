import pygame as pg
import random

from pytmx.util_pygame import load_pygame


def load_sprite(name):
    return pg.image.load(f'sprites/{name}').convert_alpha()


def load_map(name):
    return load_pygame(f'maps/{name}')


def rand_norm_vector():
    x = random.random() * 2 - 1
    y = (random.randint(0, 1) * 2 - 1) * (1 - x**2)**0.5
    return pg.Vector2(x, y)
