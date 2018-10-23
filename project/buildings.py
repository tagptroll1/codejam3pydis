# -*- coding: utf-8 -*-

from project.constants import NextColor
from pygame import Surface
from pygame.sprite import Sprite


class Building(Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Render sprites over color
        self.image = Surface((32, 32))
        self.image.fill(next(NextColor.nextColor()))
        self.rect = self.image.get_rect()

    def update(self):
        pass  # update logic for all buildings
