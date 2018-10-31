# -*- coding: utf-8 -*-
from random import randrange

import numpy as np

from project.tiles import GrassTile, WaterTile, WoodTile


class Map:
    def __init__(self, width, height, game):
        self.game = game
        self.width = width
        self.height = height
        self.terrain = [[None] * width for _ in range(height)]
        self.constructions = [[None] * width for _ in range(height)]

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
        self.initialize_base_terrain(GrassTile)
        # self.generate_trees(randrange((self.width * self.height) // 2))
        self.generate_rivers(randrange(1, 4), 1)

    def generate_grass(self):
        """ Adds grass everywhere"""
        self.initialize_base_terrain(GrassTile)

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

    def generate_river(self, start_point, width=1):
        """ Generates a single river from a starting point"""
        orientations = [
            np.array((-1, 0)),  # north
            np.array((0, 1)),  # est
            np.array((1, 0)),  # south
            np.array((0, -1)),  # west
        ]

        counter = 0
        orientation_idx = randrange(0, 4)
        new_point = np.array(start_point) + orientations[orientation_idx]
        while new_point[0] not in (0, self.width) and new_point[1] not in (0, self.height):
            self.set_parcel(*new_point, WaterTile)

            counter += 1
            try:
                while isinstance(self.get_parcel(*new_point), WaterTile):
                    idx = randrange(0, 100)
                    if 75 < idx <= 88:
                        orientation_idx = (orientation_idx + 1) % 4
                    elif 88 < idx:
                        orientation_idx = (orientation_idx - 1) % 4

                    new_point += orientations[orientation_idx]
            except IndexError:
                pass

            if counter > 100:
                return

    def is_constructable(self, top, left, bottom, right):
        try:
            for y in range(top, bottom + 1):
                if any(tile is not None for tile in self.constructions[y][left:right + 1]) \
                        or any(not parcel.constructable for parcel in self.terrain[y][left:right + 1]):
                    return False
            return True
        except IndexError:
            print(f'is contructable indexerror: top: {top}, left: {left}, bottom: {bottom}, right: {right}')
