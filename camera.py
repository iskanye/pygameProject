from settings import *


class Camera(pg.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()
        self.player_pos = (0, 0)

    def load_map(self, map):
        self.player_pos = map.player_pos
        for layer, obj in map.layers.items():
            self.add(obj, layer=layer)

    def update_player_pos(self, delta_x, delta_y):
        for layer in self.layers():
            if layer != PLAYER_LAYER:
                for sprite in self.get_sprites_from_layer(layer):
                    sprite.rect.x -= delta_x
                    sprite.rect.y -= delta_y

    def draw(self, surface, bgsurf=None, special_flags=0):
        for layer in self.layers():
            if layer != OBJECT_LAYER and layer != PLAYER_LAYER:
                for tile in self.get_sprites_from_layer(layer):
                    surface.blit(tile.image, tile.rect.topleft)
            elif layer == OBJECT_LAYER:
                objects = self.get_sprites_from_layer(layer) + self.get_sprites_from_layer(PLAYER_LAYER)
                for obj in filter(lambda a: a.pivot == NO_PIVOT, objects):
                    surface.blit(obj.image, obj.rect.topleft)
                for obj in sorted(filter(lambda a: a.pivot != NO_PIVOT, objects),
                                  key=lambda a: a.position().y):
                    surface.blit(obj.image, obj.rect.topleft)