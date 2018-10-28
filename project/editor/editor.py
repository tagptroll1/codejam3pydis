# -*- coding: utf-8 -*-
import sys
import time
from pathlib import Path

import pygame as pg
from project.constants import (
    FPS, GRIDHEIGHT, GRIDWIDTH,
    HEIGHT, SPRITESHEETPATH, Spritesheet,
    TILESIZE, WIDTH
)
from project.editor.gui import GUI
from project.player import CameraMan
from project.tilemap import Camera, Map
from project.tiles import GetTile as get_tile


class Editor:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Game editor")
        self.clock = pg.time.Clock()
        # self.map = Map([[0] * int(50) for _ in range(int(50))])
        save = Path("project", "saves", "1540754869.txt")
        self.map = Map(save=save)

        self.startx = WIDTH / 2
        self.starty = HEIGHT / 2
        print("Editor opened")

    def new(self):
        self.sheet = Spritesheet(str(SPRITESHEETPATH))
        self.all_sprites = pg.sprite.Group()
        self.tiles = pg.sprite.Group()
        self.gui_group = pg.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if str(tile).isnumeric():
                    get_tile.lookup(tile, self, col, row)

        self.gui = GUI(self)
        self.camera_man = CameraMan(self, GRIDWIDTH//2, GRIDHEIGHT//2)
        self.camera = Camera(self.map.width, self.map.height)

    def save_map(self):
        Path("project", "saves").mkdir(exist_ok=True)
        tosave = "".join([",".join(map(str, row)) for row in self.map.data])
        with Path("project", "saves", f"{int(time.time())}.txt").open("w") as file:
            file.write(tosave)

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        """
        Quit the game
        """
        pg.quit()
        sys.exit()

    def events(self):
        """
        Handle all events
        """

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.KEYDOWN:
                # Button press
                if event.key == pg.K_ESCAPE:
                    pass  # open menu

            # Draw stone on clicked tile
            if event.type == pg.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if self.gui.rect.collidepoint(x, y):
                    for item in self.gui.picker.tiles:
                        if item.rect.collidepoint(x - self.gui.rect.left, y - self.gui.rect.top):
                            self.gui.selected_tile = item.type

                    if self.gui.save.rect.collidepoint(x + 10, y - 10):
                        self.save_map()

                    # player clicked a gui piece, dont interact with the world
                    return
                # Calculates diff from start pos and camera pos
                diffx = self.camera_man.x - self.startx
                diffy = self.camera_man.y - self.starty
                # offsets the placement based on differance
                x = (diffx + x) // TILESIZE
                y = (diffy + y) // TILESIZE

                self.map.data[int(y)][int(x)] = self.gui.selected_tile

    def update(self):
        self.all_sprites.update()
        self.tiles.update()
        self.camera.update(self.camera_man)
        print(len(self.tiles))

    def draw(self):
        self.screen.fill((0, 0, 0))

        for sprite in self.tiles:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        self.screen.blit(self.gui.image, self.gui.rect)
        self.gui.draw()

        pg.display.flip()
