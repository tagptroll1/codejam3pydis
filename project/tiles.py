from pygame import Surface
from pygame.sprite import Sprite
from constants import NextColor


class Tile(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # TODO: Render sprites over color
        self.image = Surface((32, 32))
        self.image.fill(next(NextColor.nextColor()))
        self.rect = self.image.get_rect()

    def update(self):
        pass  # update logic
