from constants import *
from circleshape import CircleShape

import pygame



class NuclearMissleBomb(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, NUKE_RADIUS)


    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
        

    def update(self, dt):
        self.position += (self.velocity * dt)


##creates a shockwave with splosion class,  sets to start radius which will then be pickup by the shockwave grow check to be passed to the grow shockwave method
    def detonate(self,dt):
        shockwave = Splosion(self.position.x, self.position.y, SHOCKWAVE_START_RADIUS)

    
###################################################
    

class Splosion(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


#grows shockwave based on the dt clock,  up to the max radius listed in constants.   the shockwave check handles the max values
    def grow_shockwave(self,dt):
        r = (self.radius + (dt * 200))
        x = self.position.x
        y = self.position.y
        self.kill()
        shockwave = Splosion(x, y, r)


    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius, 0)

        



    
    
        

        





    
        
