# -*- coding: utf-8 -*-

from pathlib import Path
from random import randint

import pygame


pygame.font.init()


class Color:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SAND = (237, 201, 175)
    PLANT_MINUS = (0, 160, 0)
    PLANT = (0, 200, 0)
    PLANT_PLUSS = (10, 240, 10)  # resourcefull
    ANIMAL = (255, 224, 189)
    STONE = (151, 151, 151)
    WOOD = (49, 99, 0)
    WATER = (100, 100, 220)
    GREY = (51, 51, 51)


WIDTH = 1600
HEIGHT = 900
FPS = 60
GAMENAME = "Game Name"

BGCOLOR = Color.BLACK

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

CAMERASPEED = 800


class Images:
    # Icons
    food_icon = str(Path("project", "sprites", "I_C_Meat.png"))

    # No resource tiles
    grass = str(Path("project", "sprites", "22", "2.png"))
    grass_rock = str(Path("project", "sprites", "22", "10.png"))
    wood = str(Path("project", "sprites", "22", "8.png"))
    stone = str(Path("project", "sprites", "22", "14.png"))

    # Resources
    plant_minus = str(Path("project", "sprites", "22", "a4.png"))
    plant = str(Path("project", "sprites", "22", "a5.png"))
    plant_pluss = str(Path("project", "sprites", "22", "9.png"))

    water = str(Path("project", "sprites", "22", "3.png"))
    water_side = str(Path("project", "sprites", "22", "4.png"))
    animal = str(Path("project", "sprites", "22", "16.png"))


sprite_lookup = [
    Images.grass,
    Images.plant,
    Images.animal,
    Images.stone,
    Images.wood,
    Images.water
]

sprite_side_lookup = [
    Images.water_side
]


class Fonts:
    arial = pygame.font.SysFont("Arial", 30)


def random():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class NextColor:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    @classmethod
    def nextColor(cls):
        cls.r = abs((cls.r + randint(-20, 20))) % 255
        cls.g = abs((cls.r + randint(-20, 20))) % 255
        cls.b = abs((cls.r + randint(-20, 20))) % 255
        yield cls.r, cls.g, cls.b
