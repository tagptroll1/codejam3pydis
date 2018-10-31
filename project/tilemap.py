# -*- coding: utf-8 -*-

from pathlib import Path

import pygame as pg
from project.constants import HEIGHT, TILESIZE, WIDTH


class Map:
    def __init__(self, *, data=None, save: Path = None):
        self.data = data or [[]]
        # TODO: generate a map here
        if not data and save:
            with save.open() as f:
                self.data = [line.split(",") for line in f]

            print(self.data)
        elif not data:
            with open(Path("project", "map.txt"), "rt") as f:
                self.data = [line.split(",") for line in f]

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tilewidth * TILESIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pg.Rect(x, y, self.width, self.height)
