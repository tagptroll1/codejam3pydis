# -*- coding: utf-8 -*-

from random import randint


class Color:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SAND = (237, 201, 175)
    PLANT = (0, 200, 0)
    ANIMAL = (255, 224, 189)
    STONE = (151, 151, 151)
    WOOD = (49, 99, 0)
    WATER = (100, 100, 220)
    GREY = (51, 51, 51)


WIDTH = 1600
HEIGHT = 900
FPS = 30
GAMENAME = "Game Name"

BGCOLOR = Color.BLACK

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

CAMERASPEED = 250


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
