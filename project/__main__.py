# -*- coding: utf-8 -*-

import pygame
# from buildings import Building
from project.constants import Color
from project.tiles import (
    AnimalTile, NoResource, PlantTile, StoneTile, WaterTile, WoodTile
)

WIDTH = 1600
HEIGHT = 900
FPS = 30
GAMENAME = "Game Name"


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAMENAME)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


def load_assets():
    # sprite
    nores = NoResource()
    all_sprites.add(nores)
    nores.rect.topleft = (50, 50)

    plant = PlantTile()
    all_sprites.add(plant)
    plant.rect.topleft = (250, 250)

    animal = AnimalTile()
    all_sprites.add(animal)
    animal.rect.topleft = (550, 550)

    stone = StoneTile()
    all_sprites.add(stone)
    stone.rect.topleft = (750, 750)

    wood = WoodTile()
    all_sprites.add(wood)
    wood.rect.topleft = (450, 750)

    for x in range(282, WIDTH, 32):
        water = WaterTile()
        all_sprites.add(water)
        water.rect.topleft = (x, 250)


def start_loop():
    # Game loop
    running = True
    while running:
        clock.tick(FPS)

        # input
        for event in pygame.event.get():
            # check for window exit
            if event.type == pygame.QUIT:
                running = False

        # update
        all_sprites.update()

        # render
        screen.fill(Color.red.value)
        all_sprites.draw(screen)
        pygame.display.flip()


load_assets()
start_loop()
pygame.quit()
