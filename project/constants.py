# -*- coding: utf-8 -*-

from enum import Enum
from random import randint


class Color(Enum):
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    sand = (237, 201, 175)
    plant = (0, 200, 0)
    animal = (255, 224, 189)
    stone = (151, 151, 151)
    wood = (49, 99, 0)
    water = (100, 100, 220)

    @staticmethod
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
