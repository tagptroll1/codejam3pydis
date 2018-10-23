# -*- coding: utf-8 -*-

from random import randint

from project.constants import Color, NextColor
from pygame import Surface
from pygame.sprite import Sprite


# Type lookup:
# 0 - No resources
# 1 - Plant based resource (food)
# 2 - Animal based resource (food)
# 3 - Stone based resource
# 4 - wood based resource


class Tile(Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Render sprites over color
        self.image = Surface((32, 32))
        self.image.fill(next(NextColor.nextColor()))
        self.rect = self.image.get_rect()
        self.type = None

        self.value = 0
        self.start_value = 0

    def update(self) -> None:
        pass  # update logic

    def reset(self) -> None:
        """
        Resets the value of the tile to it's starting value
        """
        self.value = self.start_value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} x={self.rect.x}, y={self.rect.y}, type={self.type}>"


class NoResource(Tile):
    """
    A Tile which provides no resources
    """

    def __init__(self):
        super().__init__()
        self.image.fill(Color.sand.value)
        self.type = 0


class PlantTile(Tile):
    """
    A Tile which provides food from plant matter
    """

    def __init__(self):
        super().__init__()
        self.image.fill(Color.plant.value)
        self.type = 1  # Plant based food tile

        # TODO: Sprite can reflect the amount the tile provides
        self.start_value = randint(2, 10)
        self.value = self.start_value

    def rain(self) -> None:
        """
        Rain improves the yield of plant based tiles
        """
        self.value = self.start_value * 1.2

    def flood(self) -> None:
        """
        A flood kills half the crops of a plant based tile
        """
        self.value = self.start_value * 0.5

    def drought(self) -> None:
        """
        A drought kills all plant based tiles
        """
        self.value = 0


class AnimalTile(Tile):
    """
    A Tile which provides food from animals
    """

    def __init__(self):
        super().__init__()
        self.image.fill(Color.animal.value)
        self.type = 2  # Animal based food tile

        # TODO: Sprite can reflect the amount the tile provides
        self.start_value = randint(4, 10)
        self.value = self.start_value

    def drought(self) -> None:
        """
        A drought kills half of the animals on the tile
        """
        self.value = self.start_value * 0.5


class StoneTile(Tile):
    def __init__(self):
        super().__init__()
        self.image.fill(Color.stone.value)
        self.type = 3

        self.start_value = randint(2, 8)
        self.value = self.start_value


class WoodTile(Tile):
    def __init__(self):
        super().__init__()
        self.image.fill(Color.wood.value)
        self.type = 4

        self.start_value = randint(1, 5)
        self.value = self.start_value


class WaterTile(Tile):
    def __init__(self):
        super().__init__()
        self.image.fill(Color.water.value)
        self.type = 5

        self.start_value = randint(1, 2)
        self.value = self.start_value
