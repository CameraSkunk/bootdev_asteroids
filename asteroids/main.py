#Run test using "uv run main.py" on command line.
#use Ctrl+c in terminal to kill game

import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()

        dt = Clock.tick(60) / 1000 #sets frame rate and updates dt (delta time) since last call

if __name__ == "__main__":
    main()
