# -*- coding: utf-8 -*-
# Pass --editor while running to open the level editor
# instead of the game.

import argparse

from project.game import Game
from project.editor.editor import Editor

parser = argparse.ArgumentParser(description="Open game, or editor")
parser.add_argument(
    "-e",
    "--editor",
    help="Opens the map editor",
    action="store_true"
)
args = vars(parser.parse_args())

if args["editor"]:
    running = Editor()
else:
    running = Game()


while True:
    running.new()
    running.run()
