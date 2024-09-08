# imports the open-source pygame library
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    pygame.init()
    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()


        # limit the framerate to 60 FPS
        dt = fps_clock.tick(60) / 1000

# ensures the main() function is only called when this file is run directly.
if __name__ == "__main__":
  main()
