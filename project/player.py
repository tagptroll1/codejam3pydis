# -*- coding: utf-8 -*-

import pygame
from project.constants import CAMERASPEED, TILESIZE
from pygame.sprite import Sprite


class CameraMan(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        super().__init__(self.groups)
        self.game = game
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()

        self.vx = 0
        self.vy = 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        self.vx = 0
        self.vy = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -CAMERASPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = CAMERASPEED

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -CAMERASPEED

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = CAMERASPEED

        # if self.vx != 0 and self.vy != 0:

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.rect.y = self.y
