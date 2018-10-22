import pygame

from constants import Color


WIDTH = 1600
HEIGHT = 900
FPS = 30
GAMENAME = "Game Name"


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAMENAME)
clock = pygame.time.Clock()

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

    # render
    screen.fill(Color.red.value)
    pygame.display.flip()

pygame.quit()
