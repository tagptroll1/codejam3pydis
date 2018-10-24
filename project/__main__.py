# -*- coding: utf-8 -*-
from project.game import Game


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
g.show_go_screen()
