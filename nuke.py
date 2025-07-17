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

    def detonate(self,dt):
        shockwave = Splosion(self.position.x, self.position.y, SHOCKWAVE_START_RADIUS)

    


class Splosion(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def grow_shockwave(self,dt):
        r = (self.radius + (dt * 200))
        x = self.position.x
        y = self.position.y
        self.kill()
        shockwave = Splosion(x, y, r)


    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius, 0)

        



    
    
        

        





    
        
