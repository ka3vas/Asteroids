import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_color = "red"
        asteroid_width = 2
        pygame.draw.circle(screen, asteroid_color, self.position, self.radius, asteroid_width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        velocity_scaling = 3
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = int(random.uniform(20, 50))

        n_vector1 = self.velocity.rotate(angle)
        n_vector2 = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = n_vector1 * velocity_scaling

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = n_vector2 * velocity_scaling

