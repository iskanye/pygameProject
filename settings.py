from utils import *

# Main settings
FPS = 60
SCALE_FACTOR = 2
TILE = 32 * SCALE_FACTOR
SIZE = WIDTH, HEIGHT = TILE * 12, TILE * 12
ANIM_FRAME_DURATION = 10
PLAYER_SIZE = (3, 3)
PLAYER_SPEED = TILE * 8
# Map Layers
COLLISION_LAYER = 0
PLAYER_LAYER = 4
OBJECT_LAYER = 3
UI_LAYER = 5
# Colors
BACKGROUND_COLOR = (6, 6, 8)
# Vectors and Rects
NO_PIVOT = pg.Vector2(TILE ** 2, TILE ** 2)
NO_RECT = pg.Rect(0, 0, TILE ** 2, TILE ** 2)
# Keyboard keys
INTERACT = pg.K_l
UP = pg.K_w
DOWN = pg.K_s
RIGHT = pg.K_d
LEFT = pg.K_a
