# -*- coding: utf-8 -*-
from abc import ABC
from random import gauss, randrange

import numpy as np

from project.tiles import Grass, WoodTile, WaterTile


class Map:
    def __init__(self, width, height, game):
        self.game = game
        self.width = width
        self.height = height
        self.terrain = [[None] * width for _ in range(height)]

        self.generate_terrain()

    def __repr__(self):
        return repr(self.terrain)

    def __str__(self):
        return '\n'.join(''.join(str(parcel) for parcel in line) for line in self.terrain)

    def get_parcel(self, x, y):
        return self.terrain[y][x]

    def set_parcel(self, x, y, _type, **parcel_kwargs):
        self.terrain[y][x] = _type(self.game, x, y, **parcel_kwargs)

    def initialize_base_terrain(self, parcel_type, **parcel_kwargs):
        """This initialize whole terrain with given parcel types"""
        for x in range(self.width):
            for y in range(self.height):
                self.set_parcel(x, y, parcel_type, **parcel_kwargs)

    def generate_terrain(self):
        self.initialize_base_terrain(Grass)
        self.generate_trees(randrange((self.width * self.height) / 2))
        self.generate_rivers(randrange(4), 1)

    def generate_grass(self):
        """ Adds grass everywhere"""
        self.initialize_base_terrain(Grass)

    def generate_rivers(self, number, max_width):
        """initate rivers"""
        for _ in range(number):
            start_point = (randrange(1, self.width - 1), randrange(1, self.height - 1))
            self.generate_river(start_point, 1)

    def generate_trees(self, number):
        for _ in range(number):
            x = randrange(0, self.width)
            y = randrange(0, self.height)
            self.set_parcel(x, y, WoodTile)

    def generate_river(self, start_point, width):
        """ Generates a single river from a starting point"""
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
        # initialize starting point
        self.set_parcel(*start_point, WaterTile)

        # choose a direction
        dir_index = randrange(0, 8)
        new_point = np.array(start_point) + directions[dir_index]
        self.set_parcel(*new_point.tolist(), WaterTile)
        previous_dir_index = dir_index

        # TODO an inifinite loop can occure because if no path il allowed.
        # For instance a river trapped inside another one

        # draw the river until it hits a border
        while new_point[0] not in (0, self.width - 1) and new_point[1] not in (0, self.height - 1):
            dir_index = int(np.clip(round(gauss(previous_dir_index, 1)), 0, 7))

            # no going backwards
            if abs(dir_index - previous_dir_index) == 4:
                continue

            new_point += directions[dir_index]

            # no colision with a existing river or itself
            if isinstance(self.get_parcel(*new_point), WaterTile):
                continue

            self.set_parcel(*new_point.tolist(), WaterTile)
            previous_dir_index = dir_index
