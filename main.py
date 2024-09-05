# imports the open-source pygame library
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        pygame.display.flip()


        # limit the framerate to 60 FPS
        dt = fps_clock.tick(60) / 1000

# ensures the main() function is only called when this file is run directly.
if __name__ == "__main__":
  main()
