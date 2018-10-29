# -*- coding: utf-8 -*-

import pygame as pg
from project.constants import Color, HEIGHT, WIDTH, sprite_lookup
from pygame.sprite import Sprite


class GUI(Sprite):
    def __init__(self, game):
        self.groups = game.gui_group
        super().__init__(self.groups)

        self.image = pg.Surface((250, 700))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.right = WIDTH
        self.rect.centery = HEIGHT / 2
        self.image.fill(Color.GREY)

        self.rotation = 0
        self.selected_tile = 0

        self.picker = Picker(self, game)

    def update(self):
        self.picker.update()


class Picker:
    def __init__(self, gui, game):
        self.tiles = pg.sprite.Group()
        self.gui = gui
        self.game = game
        self.render_tiles()

    def render_tiles(self):
        for x, path in enumerate(sprite_lookup):
            MenuItem(path, x, self.gui, self)

        self.tiles.draw(self.gui.image)
        self.gui.save = SaveButton(self, self.game)
        self.gui.image.blit(
            self.gui.save.image,
            (10, 640)
        )


class MenuItem(Sprite):
    def __init__(self, path, x, gui, picker):
        self.groups = picker.tiles
        super().__init__(self.groups)
        # tile icon
        self.type = x
        self.x, self.y = divmod(x, 14)
        self.x = (self.x * 45) + 12
        self.y = (self.y * 45) + 12

        self.image = pg.Surface((32, 32))
        self.image_ = gui.game.sheet.get_image(*path)
        self.image_ = pg.transform.scale(
            self.image_, (32, 32))
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
        self.rect.left = picker.gui.rect.left + 10
        self.rect.top = picker.gui.rect.top + 640
        self.image.fill(Color.BLACK)
