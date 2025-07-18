from circleshape import CircleShape
from constants import *
import pygame



class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)


#draws itself and updates location based on dt clock time
    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
        

    def update(self, dt):
        self.position += (self.velocity * dt)

