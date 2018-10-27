# -*- coding: utf-8 -*-

from project.constants import TILESIZE, Images
import pygame
from pygame.sprite import Sprite
from pygame import Surface


class Building(Sprite):
    # class for buildings that stores x and y coordinates and manages displaying

    def __init__(self, game, x, y):
        self.groups = game.buildings
        super().__init__(self.groups)
        self.image = Surface((TILESIZE, TILESIZE))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def __repr__(self):
        return f"<{self.__class__.__name__} x={self.rect.x} y={self.rect.y}>"


class Resource_building(Building):
    """
    class for buildings that produce resources
    stores the amount of produced resources and the inventory they're added to
    """
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, x, y)
        self.inv = inv
        self.amount = amount


"""
Subclasses for different resource producing buildings manage the different sprites and resources
"""


class Sawmill(Resource_building):
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, inv, amount, x, y)
        self.path = Images.sawmill
        self.image = pygame.image.load(self.path)

    def add_resource(self):
        self.inv.wood += self.amount


class Stonemill(Resource_building):
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, inv, amount, x, y)
        self.path = Images.stonemill
        self.image = pygame.image.load(self.path)

    def add_resource(self):
        self.inv.stone += self.amount


class House(Resource_building):
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, inv, amount, x, y)
        self.path = Images.house
        self.image = pygame.image.load(self.path)

    def add_resource(self):
        self.inv.villagers += self.amount


class Mine(Resource_building):
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, inv, amount, x, y)
        self.path = Images.mine
        self.image = pygame.image.load(self.path)

    def add_resource(self):
        self.inv.iron += self.amount


class Watermill(Resource_building):
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, inv, amount, x, y)
        self.path = Images.watermill
        self.image = pygame.image.load(self.path)

    def add_resource(self):
        self.inv.water += self.amount


class Farm(Resource_building):
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, inv, amount, x, y)
        self.path = Images.farm
        self.image = pygame.image.load(self.path)

    def add_resource(self):
        self.inv.food += self.amount


class Butcher(Resource_building):
    def __init__(self, game, inv, amount, x, y):
        super().__init__(game, inv, amount, x, y)
        self.path = Images.butcher
        self.image = pygame.image.load(self.path)

    def add_resource(self):
        self.inv.food += self.amount
