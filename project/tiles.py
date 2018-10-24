# -*- coding: utf-8 -*-

from random import randint

from project.constants import Color, NextColor, TILESIZE
from pygame import Surface
from pygame.sprite import Sprite


# Type lookup:
# 0 - No resources
# 1 - Plant based resource (food)
# 2 - Animal based resource (food)
# 3 - Stone based resource
# 4 - wood based resource
# 5 - water based resource


class Tile(Sprite):
    def __init__(self, game, x: int, y: int):
        self.groups = game.all_sprites, game.tiles
        super().__init__(self.groups)
        # TODO: Render sprites over color
        self.game = game
        self.image = Surface((32, 32))
        self.image.fill(next(NextColor.nextColor()))
        self.rect = self.image.get_rect()
        self.type = None
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

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
        """
        <Tile x=5, y=10, type=3>
        """
        return f"<{self.__class__.__name__} x={self.rect.x}, y={self.rect.y}, type={self.type}>"


class NoResource(Tile):
    """
    A Tile which provides no resources
    """

    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image.fill(Color.SAND)
        self.type = 0


class PlantTile(Tile):
    """
    A Tile which provides food from plant matter
    """

    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image.fill(Color.PLANT)
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

    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image.fill(Color.ANIMAL)
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
    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image.fill(Color.STONE)
        self.type = 3

        self.start_value = randint(2, 8)
        self.value = self.start_value


class WoodTile(Tile):
    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image.fill(Color.WOOD)
        self.type = 4

        self.start_value = randint(1, 5)
        self.value = self.start_value


class WaterTile(Tile):
    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image.fill(Color.WATER)
        self.type = 5

        self.start_value = randint(1, 2)
        self.value = self.start_value


class GetTile:
    """
    Helper class with static methods to generate and return
    new tiles to be rendered.
    """
    @classmethod
    def loopup(cls, i):
        return {
            "0": cls.noresource,
            "1": cls.plant,
            "2": cls.animal,
            "3": cls.stone,
            "4": cls.wood,
            "5": cls.water
        }.get(i)

    @staticmethod
    def noresource(game, x: int, y: int) -> NoResource:
        return NoResource(game, x, y)

    @staticmethod
    def plant(game, x: int, y: int) -> PlantTile:
        return PlantTile(game, x, y)

    @staticmethod
    def animal(game, x: int, y: int) -> AnimalTile:
        return AnimalTile(game, x, y)

    @staticmethod
    def stone(game, x: int, y: int) -> StoneTile:
        return StoneTile(game, x, y)

    @staticmethod
    def wood(game, x: int, y: int) -> WoodTile:
        return WoodTile(game, x, y)

    @staticmethod
    def water(game, x: int, y: int) -> WaterTile:
        return WaterTile(game, x, y)
