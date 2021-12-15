import pygame
from sys import exit

from settings import *  # imports everything
from level import Level

# initialize pygame
pygame.init()

# create the main screen
screen = pygame.display.set_mode(
    (screen_width, screen_height))

# creating the clock
clock = pygame.time.Clock()

# creating the level
level = Level(level_map, screen)

# creating game loop variables / flags
game_running = True

while game_running:
    # clear the frame
    screen.fill('black')

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # update the level
    level.run()

    pygame.display.update()  # update the screen
    clock.tick(60)  # set the fps to 60

# quit pygame as soon as the game loop ends
pygame.quit()
exit()
