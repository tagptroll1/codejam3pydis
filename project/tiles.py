# -*- coding: utf-8 -*-

from random import randint
from typing import Tuple

from project.constants import (
    Color, Images,
    NextColor, TILESIZE
)
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
        self.groups = game.tiles
        super().__init__(self.groups)
        # TODO: Render sprites over color
        self.game = game
        self.image = Surface((TILESIZE, TILESIZE))
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

    def get_img(self, index: Tuple[int]):
        return self.game.sheet.get_image(*index)

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


class Grass(NoResource):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        imgnr = randint(0, 100)
        if imgnr > 3:
            self.image = self.get_img(Images.grass)
        elif imgnr == 3:
            self.image = self.get_img(Images.grass_rock)
        elif imgnr == 2:
            self.image = self.get_img(Images.grass_dino_l)
        else:
            self.image = self.get_img(Images.grass_stub)


class PlantTile(Tile):
    """
    A Tile which provides food from plant matter
    """

    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        # self.image.fill(Color.PLANT)
        self.type = 1  # Plant based food tile

        # TODO: Sprite can reflect the amount the tile provides
        self.start_value = randint(2, 10)
        self.value = self.start_value
        self.update()

    def update(self):
        super().update()
        if self.value > 7:
            self.image = self.get_img(Images.plant_minus)
        elif self.value > 2:
            self.image = self.get_img(Images.plant)
        else:
            self.image = self.get_img(Images.plant_pluss)

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
        self.image = self.get_img(Images.animal)
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
        self.image = self.get_img(Images.stone)
        self.type = 3

        self.start_value = randint(2, 8)
        self.value = self.start_value


class WoodTile(Tile):
    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image = Surface((TILESIZE, TILESIZE))
        self.image.fill(Color.WOOD)
        # self.image = self.get_img(Images.wood)
        self.type = 4

        self.start_value = randint(1, 5)
        self.value = self.start_value


class WaterTile(Tile):
    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image = self.get_img(Images.water)
        self.type = 5

        self.start_value = randint(1, 2)
        self.value = self.start_value


class WaterRockTile(Tile):
    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image = self.get_img(Images.water_rock)
        self.type = 6

        self.start_value = 1
        self.value = self.start_value


class WaterLily(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.water_lily1,
            Images.water_lily2,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 7 + rotation

        self.start_value = 1
        self.value = self.start_value


class WaterBall(Tile):
    def __init__(self, game, x: int, y: int):
        super().__init__(game, x, y)
        self.image = self.get_img(Images.water_ball)
        self.type = 9

        self.start_value = randint(1, 2)
        self.value = self.start_value


class WaterRock(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.water_rock_l,
            Images.water_rock_b,
            Images.water_rock_r,
            Images.water_rock_t,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 13 + rotation

        self.start_value = 1
        self.value = self.start_value


class WaterDirtRock(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.water_dirtrock_l,
            Images.water_dirtrock_b,
            Images.water_dirtrock_r,
            Images.water_dirtrock_t,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 17 + rotation

        self.start_value = 1
        self.value = self.start_value


class WaterFlower(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.water_flower_l,
            Images.water_flower_b,
            Images.water_flower_r,
            Images.water_flower_t,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 21 + rotation

        self.start_value = 1
        self.value = self.start_value


class WaterSide(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.water_t,
            Images.water_r,
            Images.water_b,
            Images.water_l,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 25 + rotation

        self.start_value = 1
        self.value = self.start_value


class WaterLShape(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.water_tl,
            Images.water_bl,
            Images.water_br,
            Images.water_tr,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 29 + rotation

        self.start_value = 1
        self.value = self.start_value


class WaterCorner(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.water_cbl,
            Images.water_cbr,
            Images.water_ctr,
            Images.water_ctl,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 33 + rotation

        self.start_value = 1
        self.value = self.start_value


class DirtRock(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.dirt_rock_tl,
            Images.dirt_rock_bl,
            Images.dirt_rock_br,
            Images.dirt_rock_tr,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 37 + rotation


class DirtDino(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.dirt_dino_l,
            Images.dirt_dino_b,
            Images.dirt_dino_r,
            Images.dirt_dino_t,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 41 + rotation


class DirtSide(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.dirt_l,
            Images.dirt_b,
            Images.dirt_r,
            Images.dirt_t,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 45 + rotation


class DirtLShape(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.dirt_tl,
            Images.dirt_bl,
            Images.dirt_br,
            Images.dirt_tr,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 49 + rotation


class DirtCorner(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.dirt_ctl,
            Images.dirt_cbl,
            Images.dirt_cbr,
            Images.dirt_ctr,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 53 + rotation


class RockCorner(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.rock_cbl,
            Images.rock_cbr,
            Images.rock_ctr,
            Images.rock_ctl,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 57 + rotation


class RockSide(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.rock_l,
            Images.rock_b,
            Images.rock_r,
            Images.rock_t,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 61 + rotation


class RockLSide(Tile):
    def __init__(self, game, x, y, rotation=0):
        """
        0 - water faces top
        1 - water faces left
        2 - water faces bottom
        3 - water faces right
        """
        super().__init__(game, x, y)
        sides = [
            Images.rock_tl,
            Images.rock_bl,
            Images.rock_br,
            Images.rock_tr,
        ]
        self.image = self.get_img(sides[rotation])
        self.type = 65 + rotation


# TODO: Fix docstring on classes

class GetTile:
    """
    Helper class with static methods to generate and return
    new tiles to be rendered.
    """
    theclass = [
        Grass,
        PlantTile,
        AnimalTile,
        StoneTile,
        WoodTile,
        WaterTile,
        WaterRockTile,
        (WaterLily, 0),
        (WaterLily, 1),
        WaterBall,
        (WaterRock, 0),
        (WaterRock, 1),
        (WaterRock, 2),
        (WaterRock, 3),
        (WaterDirtRock, 0),
        (WaterDirtRock, 1),
        (WaterDirtRock, 2),
        (WaterDirtRock, 3),
        (WaterFlower, 0),
        (WaterFlower, 1),
        (WaterFlower, 2),
        (WaterFlower, 3),
        (WaterSide, 0),
        (WaterSide, 1),
        (WaterSide, 2),
        (WaterSide, 3),
        (WaterLShape, 0),
        (WaterLShape, 1),
        (WaterLShape, 2),
        (WaterLShape, 3),
        (WaterCorner, 0),
        (WaterCorner, 1),
        (WaterCorner, 2),
        (WaterCorner, 3),
        (DirtRock, 0),
        (DirtRock, 1),
        (DirtRock, 2),
        (DirtRock, 3),
        (DirtDino, 0),
        (DirtDino, 1),
        (DirtDino, 2),
        (DirtDino, 3),
        (DirtSide, 0),
        (DirtSide, 1),
        (DirtSide, 2),
        (DirtSide, 3),
        (DirtLShape, 0),
        (DirtLShape, 1),
        (DirtLShape, 2),
        (DirtLShape, 3),
        (DirtCorner, 0),
        (DirtCorner, 1),
        (DirtCorner, 2),
        (DirtCorner, 3),
        (RockCorner, 0),
        (RockCorner, 1),
        (RockCorner, 2),
        (RockCorner, 3),
        (RockSide, 0),
        (RockSide, 1),
        (RockSide, 2),
        (RockSide, 3),
        (RockLSide, 0),
        (RockLSide, 1),
        (RockLSide, 2),
        (RockLSide, 3),
    ]

    @staticmethod
    def lookup(i, game, x, y):
        tile_class = GetTile.theclass[int(i)]

        if isinstance(tile_class, tuple):
            tile_class, rot = tile_class
            return tile_class(game, x, y, rot)
        return tile_class(game, x, y)
