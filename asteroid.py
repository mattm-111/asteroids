import pygame
import random
from circleshape import CircleShape
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius


    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
        

    def update(self, dt):
        self.position += (self.velocity * dt)

## on impact with shots, nukes or shockwaves will delete itself.  if it isn't an already "small" asteroid will spawn two more smaller asteroids moving slightly faster in mirrored vectors.  
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            pos_angle = random.uniform(20, 50)
            pos_velocity = self.velocity.rotate(pos_angle)
            neg_velocity = (self.velocity.rotate(pos_angle) * -1)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            self.spawn_new(split_radius, self.position, pos_velocity)
            self.spawn_new(split_radius, self.position, neg_velocity)


    def spawn_new(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = (velocity * 1.2)
        
            



