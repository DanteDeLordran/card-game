import sys

from pathlib import Path
import pygame
import pygwidgets
from config import FPS, WINDOW_WIDTH, WINDOW_HEIGHT

def run():
    pygame.init()
    pygame.display.set_caption('Card Game')
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    background = pygwidgets.Image(window, (0,0), Path(__file__).parent.parent / 'assets' / "images" / 'background.png')

    new_game_button = pygwidgets.TextButton(window, (20, 530), 'New Game', width=100, height=45)
    higher_button = pygwidgets.TextButton(window, (540, 520), 'Higher', width=100, height=45)
    lower_button = pygwidgets.TextButton(window, (340, 520), 'Lower', width=100, height=45)
    quit_button = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




        pygame.display.update()

        clock.tick(FPS)