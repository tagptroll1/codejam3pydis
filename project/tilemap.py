# -*- coding: utf-8 -*-

from pathlib import Path

import pygame as pg
from project.constants import HEIGHT, TILESIZE, WIDTH


class Map:
    def __init__(self, *, data=[], save: Path=None):
        self.data = data
        # TODO: generate a map here
        if not data and save:
            with save.open() as f:
                for line in f:
                    self.data.append(line)
        elif not data:
            with open(Path("project", "map.txt"), "rt") as f:
                for line in f:
                    self.data.append(line)

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

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pg.Rect(x, y, self.width, self.height)
