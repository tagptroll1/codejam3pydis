# -*- coding: utf-8 -*-
from abc import ABC
from math import ceil
from random import gauss, randrange

import numpy as np


class Cell(ABC):
    value = None

    def __str__(self):
        return str(self.value)


class Dust(Cell):
    value = '░'


class Grass(Cell):
    value = '\x1b[0;32;46m▒\x1b[0m'


class Tree(Cell):
    value = '\x1b[0;30;42m▓\x1b[0m'


class Bush(Cell):
    value = '⬡'


class Water(Cell):
    value = '\x1b[0;34m▓\x1b[0m'


class Map:
    def __init__(self, m, n):
        """Initalize a m×n matrice"""
        self.m = m
        self.n = n
        self.terrain = [[None] * n for _ in range(m)]
        self.initialize_base_terrain(Grass)
        self.initialize_trees(randrange((n * m) / 2))
        self.initialize_rivers(randrange(4), 1)

    def __repr__(self):
        return repr(self.terrain)

    def __str__(self):
        return '\n'.join(''.join(str(parcel) for parcel in line) for line in self.terrain)

    def get_parcel(self, x, y):
        return self.terrain[y][x]

    def initialize_parcel(self, x, y, _type, **parcel_kwargs):
        self.terrain[y][x] = _type(**parcel_kwargs)

    def initialize_base_terrain(self, parcel_type=Dust, **parcel_kwargs):
        """This initialize whole terrain with given parcel types"""
        for x in range(self.n):
            for y in range(self.m):
                self.terrain[y][x] = parcel_type(**parcel_kwargs)

    def initialize_grass(self):
        self.initialize_base_terrain(Grass)

    def initialize_rivers(self, number, max_width):
        """initate rivers"""
        for _ in range(number):
            start_point = (randrange(1, self.n - 1), randrange(1, self.m - 1))
            self.generate_river(start_point, 1)

    def initialize_trees(self, number):
        for _ in range(number):
            x = randrange(0, self.n)
            y = randrange(0, self.m)
            self.initialize_parcel(x, y, Tree)

    def generate_river(self, start_point, width):
        # start point
        self.initialize_parcel(*start_point, Water)

        directions = {
            0: np.array((-1, 0)),  # North
            1: np.array((-1, 1)),  # North-Est
            2: np.array((0, 1)),  # Est
            3: np.array((1, 1)),  # South-Est
            4: np.array((1, 0)),  # South
            5: np.array((1, -1)),  # South-West
            6: np.array((0, -1)),  # West
            7: np.array((-1, -1)),  # North-West
        }
        # choose a direction
        dir_index = randrange(0, 8)
        new_point = np.array(start_point) + directions[dir_index]
        self.initialize_parcel(*new_point.tolist(), Water)
        previous_dir_index = dir_index

        #TODO an inifinite loop can occure because if no path il allowed. For instance a river trapped inside another one
        # draw the river until it hits a border
        while new_point[0] not in (0, self.n - 1) and new_point[1] not in (0, self.m - 1):
            dir_index = int(np.clip(round(gauss(previous_dir_index, 1)), 0, 7))

            # no going backwards
            if abs(dir_index - previous_dir_index) == 4:
                continue

            new_point += directions[dir_index]

            # no colision with a existing river or itself
            if isinstance(self.get_parcel(*new_point), Water):
                continue

            self.initialize_parcel(*new_point.tolist(), Water)
            previous_dir_index = dir_index
