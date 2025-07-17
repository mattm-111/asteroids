from constants import *
from circleshape import CircleShape

import pygame



class Nuke(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, NUKE_RADIUS)


    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
        

    def update(self, dt):
        self.position += (self.velocity * dt)