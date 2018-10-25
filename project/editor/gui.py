# -*- coding: utf-8 -*-

import pygame as pg
from project.constants import Color, HEIGHT, WIDTH, sprite_lookup, sprite_side_lookup
from pygame.sprite import Sprite


class GUI(Sprite):
    def __init__(self, game):
        self.groups = game.gui_group
        super().__init__(self.groups)

        self.image = pg.Surface((100, 600))
        self.rect = self.image.get_rect()

        self.rect.right = WIDTH
        self.rect.centery = HEIGHT / 2
        self.image.fill(Color.GREY)

        self.rotation = 0
        self.selected_tile = 0

        self.picker = Picker(self, game)

    def update(self):
        self.picker.update()

    def draw(self):
        self.picker.render_tiles()
        self.image.blit(self.save.image, (10, 560))


class Picker:
    def __init__(self, gui, game):
        self.tiles = pg.sprite.Group()
        self.gui = gui
        self.game = game
        self.render_tiles()

    def render_tiles(self):
        for x in range(6):
            path = sprite_lookup[x]
            MenuItem(path, x, self.gui, self)

        for y in range(1):
            path = sprite_side_lookup[y]
            for rot in range(4):
                MenuItem(path, x + y + rot + 1, self.gui, self, rot=rot)

        self.gui.save = SaveButton(self, self.game)

        self.tiles.draw(self.gui.image)


class MenuItem(Sprite):
    def __init__(self, path, x, gui, picker, rot=0):
        self.groups = picker.tiles
        super().__init__(self.groups)
        self.rot = rot
        self.type = x - rot
        # tile icon
        self.x, self.y = divmod(x, 13)
        self.x = (self.x * 45) + 12
        self.y = (self.y * 45) + 12

        self.image = pg.Surface((32, 32))
        self.image_ = pg.image.load(path).convert()
        self.image_ = pg.transform.scale(
            self.image_, (32, 32))
        self.image_ = pg.transform.rotate(self.image_, rot * 90)
        self.rect = self.image_.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

        self.image.blit(self.image_, (0, 0))


class SaveButton(Sprite):
    def __init__(self, picker, game):
        self.groups = game.gui_group
        super().__init__(self.groups)

        self.image = pg.Surface((50, 20))
        self.rect = self.image.get_rect()
        self.rect.left = picker.gui.rect.left + 20
        self.rect.top = picker.gui.rect.top + 550
        self.image.fill(Color.BLACK)
