import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        asteroid_color = "white"
        asteroid_width = 2
        pygame.draw.circle(screen, asteroid_color, self.position, self.radius, asteroid_width)

    def update(self, dt):
        self.position += self.velocity * dt