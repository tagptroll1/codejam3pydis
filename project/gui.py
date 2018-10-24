# -*- coding: utf-8 -*-

import pygame
from project.constants import Color, HEIGHT, Images, WIDTH
from pygame import Surface
from pygame.sprite import Sprite


class GUI:
    def __init__(self, game):
        self.game = game
        self.resources = ResourceGUI(game)


class ResourceGUI(Sprite):
    def __init__(self, game):
        self.groups = game.gui_group, game.resource_gui
        super().__init__(self.groups)
        self.game = game
        width = int(WIDTH * 0.7)
        height = int(HEIGHT * 0.08)
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = WIDTH // 2
        self.image.fill(Color.GREY)

        # resources
        self.food = Food(self, self.game)


class Resource:
    def __init__(self):
        self.value = 0
        self.old = None
        self.draw_it = True

    def update(self):
        if self.value != self.old:
            self.old = self.value
            self.draw_it = True
        else:
            self.draw_it = False


class Food(Sprite, Resource):
    def __init__(self, gui, game):
        self.groups = game.resource_gui
        Sprite.__init__(self, self.groups)
        Resource.__init__(self)

        self.gui = gui
        self.game = game
        self.path = Images.food_icon
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image.set_colorkey(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.top = 30
        self.rect.centerx = (WIDTH//2) + WIDTH * 0.2

        self.value = 5  # get this from game, or some state manager

        self.text_fig = {
            "game": self.game,
            "text": str(self.value),
            "size": 30,
            "color": Color.WHITE,
            "width": 50,
            "height": 30,
            "x": self.rect.right,
            "y": 25
        }
        self.text = Text(**self.text_fig)

    def update(self):
        Resource.__init__(self)
        if self.draw_it:

            self.text = Text(**self.text_fig)


class Text(Sprite):
    def __init__(
        self, game, text, size, color, width, height, x, y
    ):
        self.groups = game.resource_gui
        super().__init__(self.groups)
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.font = pygame.font.SysFont("Arial", size)
        self.color = color
        self.textSurf = self.font.render(text, 1, color)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
