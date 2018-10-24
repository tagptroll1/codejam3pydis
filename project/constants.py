# -*- coding: utf-8 -*-

from random import randint


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
