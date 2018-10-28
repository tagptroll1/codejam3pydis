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
    PLANT_PLUSS = (10, 240, 10)  # resourceful
    ANIMAL = (255, 224, 189)
    STONE = (151, 151, 151)
    WOOD = (49, 99, 0)
    WATER = (100, 100, 220)
    GREY = (51, 51, 51)


WIDTH = 1600
HEIGHT = 900
FPS = 60
GAMENAME = "Game Name"
SPRITESHEETPATH = Path("project", "sprites", "sheet.png")
BGCOLOR = Color.BLACK

TILESIZE = 64
GRIDWIDTH = WIDTH // TILESIZE
GRIDHEIGHT = HEIGHT // TILESIZE

CAMERASPEED = 800

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, w, h):
        """
        Cuts out a sub image of the sheet
        """
        image = pygame.Surface((w, h))
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))

        return image

def fetch_subimage(x, y):
    x *= TILESIZE
    y *= TILESIZE
    return (x, y, TILESIZE, TILESIZE)

class Images:
    # Icons
    food_icon = str(Path("project", "sprites", "I_C_Meat.png"))

    # No resource tiles
    grass = fetch_subimage(0, 0)
    grass_rock = fetch_subimage(1, 1)
    grass_dino_l = fetch_subimage(0, 2)
    grass_dino_r = fetch_subimage(1, 2)
    grass_stub = fetch_subimage(0, 1)

    stone_tile = fetch_subimage(0, 7)
    dirt = fetch_subimage(0, 11)
    dirt_stone = fetch_subimage(1, 11)
    dirt_pebble1 = fetch_subimage(0, 12)
    dirt_pebble2 = fetch_subimage(1, 12)

    # Resources
    stone = fetch_subimage(0, 10)

    plant_minus = fetch_subimage(0, 4)
    plant = fetch_subimage(0, 3)
    plant_pluss = fetch_subimage(0, 5)

    animal = fetch_subimage(0, 9)

    water = fetch_subimage(0, 6)
    water_rock = fetch_subimage(1, 6)
    water_lily1 = fetch_subimage(2, 6)
    water_lily2 = fetch_subimage(3, 6)
    water_ball = fetch_subimage(4, 6)
    # __blend tiles__
    # water
    water_t = fetch_subimage(12, 1)
    water_r = fetch_subimage(11, 1)
    water_b = fetch_subimage(10, 1)
    water_l = fetch_subimage(9, 1)
    water_tl = fetch_subimage(9, 5)
    water_bl = fetch_subimage(10, 5)
    water_br = fetch_subimage(11, 5)
    water_tr = fetch_subimage(12, 5)
    water_cbl = fetch_subimage(9, 0)
    water_cbr = fetch_subimage(10, 0)
    water_ctr = fetch_subimage(11, 0)
    water_ctl = fetch_subimage(12, 0)
    # dirt
    dirt_rock_tl = fetch_subimage(4, 0)
    dirt_rock_bl = fetch_subimage(5, 0)
    dirt_rock_br = fetch_subimage(6, 0)
    dirt_rock_tr = fetch_subimage(7, 0)
    dirt_dino_l = fetch_subimage(4, 1)
    dirt_dino_b = fetch_subimage(5, 1)
    dirt_dino_r = fetch_subimage(6, 1)
    dirt_dino_t = fetch_subimage(7, 1)
    dirt_l = fetch_subimage(4, 2)
    dirt_b = fetch_subimage(5, 2)
    dirt_r = fetch_subimage(6, 2)
    dirt_t = fetch_subimage(7, 2)
    dirt_tl = fetch_subimage(4, 3)
    dirt_bl = fetch_subimage(5, 3)
    dirt_br = fetch_subimage(6, 3)
    dirt_tr = fetch_subimage(7, 3)
    dirt_ctl = fetch_subimage(4, 4)
    dirt_cbl = fetch_subimage(5, 4)
    dirt_cbr = fetch_subimage(6, 4)
    dirt_ctr = fetch_subimage(7, 4)



    # Buildings
    butcher = str(Path("project", "sprites", "buildings", "butcher.png"))
    farm = str(Path("project", "sprites", "buildings", "farm.png"))
    house = str(Path("project", "sprites", "buildings", "house.png"))
    mine = str(Path("project", "sprites", "buildings", "mine.png"))
    sawmill = str(Path("project", "sprites", "buildings", "sawmill.png"))
    stonemill = str(Path("project", "sprites", "buildings", "stonemill.png"))
    watermill = str(Path("project", "sprites", "buildings", "watermill.png"))




sprite_lookup = [
    Images.grass,
    Images.plant,
    Images.animal,
    Images.grass_rock,
    Images.grass_stub,
    Images.water,
    Images.water_t,
    Images.water_r,
    Images.water_b,
    Images.water_l,
    Images.water_tl,
    Images.water_bl,
    Images.water_br,
    Images.water_tr,
    Images.water_cbl,
    Images.water_cbr,
    Images.water_ctr,
    Images.water_ctl,
    Images.dirt_rock_tl,
    Images.dirt_rock_bl,
    Images.dirt_rock_br,
    Images.dirt_rock_tr,
    Images.dirt_dino_l,
    Images.dirt_dino_b,
    Images.dirt_dino_r,
    Images.dirt_dino_t,
    Images.dirt_l,
    Images.dirt_b,
    Images.dirt_r,
    Images.dirt_t,
    Images.dirt_tl,
    Images.dirt_bl,
    Images.dirt_br,
    Images.dirt_tr,
    Images.dirt_ctl,
    Images.dirt_cbl,
    Images.dirt_cbr,
    Images.dirt_ctr,
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
