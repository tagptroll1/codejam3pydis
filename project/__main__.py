import pygame
# from buildings import Building
from constants import Color
from tiles import Tile

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
    for x in range(0, WIDTH, 32):
        for y in range(0, HEIGHT, 32):
            tile = Tile()
            tile.rect.topleft = (x, y)
            all_sprites.add(tile)


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
