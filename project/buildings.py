# -*- coding: utf-8 -*-

from pygame import Surface
from pygame.sprite import Sprite
from inventory import Inventory
from constants import TILESIZE


class Building(Sprite):
    #class for buildings that stores x and y coordinates and manages displaying 

    def __init__(self, x, y, image=None):
        super().__init__()
        #TODO Render sprites over color
        self.image = image
        self.x = x 
        self.y = y 

    def add_rect(self):
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
    def __init__(self, inv, amount, x, y):
        super().__init__(x, y)
        self.inv = inv
        self.amount = amount

"""
Subclasses for different resource producing buildings manage the different sprites and resources
"""

class Sawmill(Resource_building):
    def __init__(self, inv, amount, x, y):
        super().__init__(inv, amount, x, y)

    def add_resource(self):
        self.inv.wood += self.amount


class Stonemill(Resource_building):
    def __init__(self, inv, amount):
        super().__init__(inv, amount)

    def add_resource(self):
        self.inv.stone += self.amount


class House(Resource_building):
    def __init__(self, inv, amount):
        super().__init__(inv, amount)

    def add_resource(self):
        self.inv.villagers += self.amount


class Mine(Resource_building):
    def __init__(self, inv, amount):
        
        super().__init__(inv, amount)

    def add_resource(self):
        self.inv.iron += self.amount


class Watermill(Resource_building):
    def __init__(self, inv, amount):
        super().__init__(inv, amount)

    def add_resource(self):
        self.inv.water += self.amount


class Farm(Resource_building):
    def __init__(self, inv, amount):
        super().__init__(inv, amount)

    def add_resource(self):
        self.inv.food += self.amount


class Butcher(Resource_building):
    def __init__(self, inv, amount):
        super().__init__(inv, amount)

    def add_resource(self):
        self.inv.food += self.amount