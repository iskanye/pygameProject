from settings import *


class Camera(pg.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()
        self.player_pos = (0, 0)

        self.shake_magnitude = 0
        self.shake_time = 0
        self.shaking = False
        self.shake_frame = 0

    def load_map(self, map):
        self.player_pos = map.player_pos
        for layer, obj in map.layers.items():
            self.add(obj, layer=layer)

    def unload_map(self):
        for layer in self.layers():
            if layer != PLAYER_LAYER and layer != UI_LAYER:
                for i in self.get_sprites_from_layer(layer):
                    i.kill()

    def update_player_pos(self, delta_x, delta_y):
        for layer in self.layers():
            if layer != PLAYER_LAYER and layer != UI_LAYER:
                for sprite in self.get_sprites_from_layer(layer):
                    sprite.rect.x -= delta_x
                    sprite.rect.y -= delta_y

    def draw(self, surface, bgsurf=None, special_flags=0):
        for layer in self.layers():
            if layer != OBJECT_LAYER and layer != PLAYER_LAYER and layer != UI_LAYER:
                for tile in self.get_sprites_from_layer(layer):
                    surface.blit(tile.image, tile.rect.topleft)
            elif layer == OBJECT_LAYER:
                objects = self.get_sprites_from_layer(layer) + self.get_sprites_from_layer(PLAYER_LAYER)
                for obj in filter(lambda a: a.pivot == NO_PIVOT and a.image is not None, objects):
                    surface.blit(obj.image, obj.rect.topleft)
                for obj in sorted(filter(lambda a: a.pivot != NO_PIVOT, objects),
                                  key=lambda a: a.position().y):
                    surface.blit(obj.image, obj.rect.topleft)
        for tile in self.get_sprites_from_layer(UI_LAYER):
            surface.blit(tile.image, tile.rect.topleft)

    def shake(self, magnitude, time):
        self.shake_magnitude = magnitude
        self.shake_time = time
        self.shaking = True
        self.shake_frame = 0

    def update(self):
        super().update()
        if self.shaking and self.shake_frame <= self.shake_time * FPS:
            self.shake_frame += 1
            self.update_player_pos(*(rand_norm_vector() * (1 - self.shake_frame /
                                                           (self.shake_time * FPS)) * self.shake_magnitude))
        if self.shake_frame > self.shake_time * FPS:
            self.shaking = False
