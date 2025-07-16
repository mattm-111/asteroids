from circleshape import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
        

    def update(self, dt):
        self.position += (self.velocity * dt)



