# -*- coding: utf-8 -*-
from typing import Tuple

import pygame
from project.constants import Color, Fonts, Images, WIDTH
from pygame import Surface
from pygame.sprite import Sprite


class GUI:
    def __init__(self, game):
        self.game = game
        self.resources = ResourceGUI(game)


class ResourceGUI(Sprite):
    def __init__(self, game):
        self.groups = game.gui_group
        super().__init__(self.groups)
        self.game = game
        width = 1000
        height = 70
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = WIDTH // 2
        self.image.fill(Color.GREY)

        # resources
        # self.wood = Wood(self, self.game)
        self.stone = Stone(self, self.game)
        self.iron = Iron(self, self.game)
        self.food = Food(self, self.game)
        # self.water = Water(self, self.game)
        # self.population = Population(self, self.game)

        self.timer = Timer(self, self.game)

    # def draw(self):
        # self.game.screen.blit(self.image, self.rect)


class Timer(Sprite):
    def __init__(self, gui, game):
        self.groups = game.resource_text
        super().__init__(self.groups)

        self.image = Surface((120, 30))
        self.image.fill(Color.GREY)
        self.gui = gui
        self.game = game
        self.time = game.seconds
        self.text = self.get_time()

    def update(self):
        self.time = self.game.seconds
        self.text = self.get_time()

    def draw(self, to):
        to.blit(self.image, (900, 15))
        to.blit(
            Fonts.arial.render(
                self.text, True, (0, 0, 0)
            ),
            (900, 15)
        )

    def get_time(self) -> str:
        m, s = divmod(self.time, 60)
        if m < 10:
            m = f"0{m}"
        if s < 10:
            s = f"0{s}"

        return f"{m}:{s}"


class Stone(Sprite):
    def __init__(self, gui, game):
        self.groups = game.resource_icon
        super().__init__(self.groups)

        # self.path = Images.stone_icon
        # self.image = pygame.image.load(self.path).convert_alpha()
        # self.image.set_colorkey(Color.BLACK)
        self.image = Surface((32, 32))
        self.image.fill(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.top = 20
        self.rect.left = 550

        self.text = Text(game, "stone", bg=Color.GREY, top=20, left=350)
        self.text.draw(self.image)


class Iron(Sprite):
    def __init__(self, gui, game):
        self.groups = game.resource_icon
        super().__init__(self.groups)

        # self.path = Images.iron_icon
        # self.image = pygame.image.load(self.path).convert_alpha()
        # self.image.set_colorkey(Color.BLACK)
        self.image = Surface((32, 32))
        self.image.fill((220, 220, 220))
        self.rect = self.image.get_rect()
        self.rect.top = 20
        self.rect.left = 750

        self.text = Text(game, "iron", bg=Color.GREY, top=20, left=550)
        self.text.draw(self.image)


class Food(Sprite):
    def __init__(self, gui, game):
        self.groups = game.resource_icon
        super().__init__(self.groups)

        self.path = Images.food_icon
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image.set_colorkey(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.top = 20
        self.rect.left = 950

        self.text = Text(game, "food", bg=Color.GREY, top=20, left=750)
        self.text.draw(self.image)


class Text(Sprite):
    def __init__(
        self,
        game,
        key: str,
        color: Tuple[int] = Color.WHITE,
        bg: Tuple[int] = None,
        top: int = 0,
        left: int = 0
    ):
        self.groups = game.resource_text
        super().__init__(self.groups)
        self.font = Fonts.arial
        self.color = color
        self.key = key
        self.bg = bg
        self.to_draw = True
        self.left = left
        self.top = top
        self.values = game.resources

        self.text = str(self.values.get(self.key))
        self.old_text = None
        bitmap_ = self.font.render(self.text, True, self.color)
        self.bitmap = pygame.Surface(bitmap_.get_size(), pygame.SRCALPHA)

        if self.bg is not None:
            self.bitmap.fill(self.bg)

        self.bitmap.blit(bitmap_, (0, 0))

        self.width = self.bitmap.get_width()
        self.height = self.bitmap.get_height()

    def update(self):
        self.text = str(self.values[self.key])
        if self.old_text != self.text:
            # rerender
            self.old_text = self.text

            bitmap_ = self.font.render(self.text, True, self.color)
            self.bitmap = pygame.Surface(bitmap_.get_size(), pygame.SRCALPHA)

            if self.bg is not None:
                self.bitmap.fill(self.bg)

            self.bitmap.blit(bitmap_, (0, 0))

            self.width = self.bitmap.get_width()
            self.height = self.bitmap.get_height()

            self.to_draw = True

    def draw(self, to, pos=(0, 0)):
        if self.to_draw:
            to.blit(self.bitmap, (self.left + pos[0], self.top + pos[1]))
            self.to_draw = False
