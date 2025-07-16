from constants import *
from circleshape import *
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


## draws player object, once per frame
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

## rotates player istance, called from update method
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

##updates self orientation and movement vector on key press, checked once per frame.    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate((dt * -1))
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((dt * -1))


## gives a movement vector,  called in update()
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    

