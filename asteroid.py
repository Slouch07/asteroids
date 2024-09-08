from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
       self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Generate a random angle between 20 and 50 degrees
            random_angle = random.uniform(20, 50)

            # Create two vectors using the asteroids original velocity and the new random angle
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)

            # Create new radius for smaller asteroids after split.
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create new asteroid object
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)

            # Set first new asteroid's velocity to 1.2 times the original
            asteroid1.velocity = vector1 * 1.2

            # Same as above for the second new asteroid
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2
