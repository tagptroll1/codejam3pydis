# -*- coding: utf-8 -*-

import sys

import pygame as pg
# from buildings import Building
from project.constants import (
    BGCOLOR, Color, FPS,
    GAMENAME, GRIDHEIGHT, GRIDWIDTH,
    HEIGHT, TILESIZE, WIDTH
)
from project.gui import GUI
from project.player import CameraMan
from project.tilemap import Camera, Map
from project.tiles import GetTile as get_tile


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(GAMENAME)
        self.clock = pg.time.Clock()
        self.load_data()

        self.startx = WIDTH // 2
        self.starty = HEIGHT // 2

    def load_data(self):
        """
        Load data, generate map?
        """
        self.map = Map()

    def new(self):
        """
        Initialize a new game
        """
        self.all_sprites = pg.sprite.Group()
        self.tiles = pg.sprite.Group()
        self.gui_group = pg.sprite.Group()
        self.resource_gui = pg.sprite.Group()
        self.gui = GUI(self)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                # Probably newline, but tile is sometimes None
                if tile in ("012345"):
                    # Fetches helper method for tile lookup and calls it
                    get_tile.loopup(tile)(self, col, row)

        # Camera
        self.camera_man = CameraMan(self, GRIDWIDTH//2, GRIDHEIGHT//2)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        """
        Start the game
        """
        self.playing = True
        while self.playing:
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

    def update(self):
        """
        Update the game and sprites
        """
        self.all_sprites.update()
        self.resource_gui.update()
        self.camera.update(self.camera_man)

    def draw_grid(self):
        """
        Draws a grid to show where tiles meet
        """
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, Color.GREY,
                         (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, Color.GREY,
                         (0, y), (WIDTH, y))

    def draw(self):
        """
        Draw all sprites and flip display
        """
        self.screen.fill(BGCOLOR)
        self.draw_grid()

        for sprite in self.tiles:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        self.gui_group.draw(self.screen)
        self.resource_gui.draw(self.screen)
        pg.display.flip()

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
                for gui in self.gui_group:
                    if gui.rect.collidepoint(x, y):
                        # player clicked a gui piece, dont interact with the world
                        print("guiclick")
                        gui.food.value += 1
                        return
                # Calculates diff from start pos and camera pos
                diffx = self.camera_man.x - self.startx
                diffy = self.camera_man.y - self.starty
                # offsets the placement based on differance
                x = (diffx + x) // TILESIZE
                y = (diffy + y) // TILESIZE
                get_tile.stone(self, x, y)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
