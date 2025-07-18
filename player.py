import pygame
import sys
from constants import *
from circleshape import CircleShape
from shot import Shot
from nuke import NuclearMissleBomb
from text import death_screen, ui_text, life_text


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.nuke_cooldown = 0
        self.score = 0
        self.lives = 3
        self.can_be_damaged = True
        self.grace_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


## draws player object, once per frame
    def draw(self, screen):
        if self.can_be_damaged == True:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)
        else:
            pygame.draw.polygon(screen, "green", self.triangle(), 2)

## rotates player istance, called from update method
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

##updates self orientation and movement vector on key press, checked once per frame.    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotate((dt * -1))
        if keys[pygame.K_RIGHT]:
            self.rotate((dt))
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move((dt * -1))
        if keys[pygame.K_SPACE]:
            if self.shot_timer() and self.can_be_damaged:
                self.shoot()
        if keys[pygame.K_b]:
            if self.nuke_timer() and self.can_be_damaged:
                self.nuke()
        if keys[pygame.K_ESCAPE]:
            print("Manual Exit Key Pressed")
            sys.exit()


## gives a movement vector,  called in update()
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        color = "red"
        shot = Shot(self.position.x, self.position.y)
        shot.velocity =  pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


    def nuke(self):
        color = 'red'
        nuke = NuclearMissleBomb(self.position.x, self.position.y)
        nuke.velocity =  pygame.Vector2(0, 1).rotate(self.rotation) * NUKE_SPEED

    
    #shot timer,  will return true to the shoot()method if cooldown is at or below 0,  then set the timer to the cooldown constant
    def shot_timer(self, ):
        if self.cooldown <= 0:
            self.cooldown = PLAYER_SHOOT_COOLDOWN
            return True
        

    def nuke_timer(self,):
        if self.nuke_cooldown <= 0:
            self.nuke_cooldown = NUKE_COOLDOWN
            return True
        
        
    def score_up(self):
        self.score += 100


#checks grace timer to know if player should not be damagable,  happens after loss of life
    def check_grace(self):
        if self.grace_timer <= 0:
            self.can_be_damaged = True

#logic after player getting hit,   removes a life and player enters a grace period
    def on_hit(self):
        self.lives -= 1
        self.can_be_damaged = False
        self.position.x = (SCREEN_WIDTH / 2)
        self.position.y = (SCREEN_HEIGHT / 2)
        self.grace_timer = PLAYER_GRACE


    def on_death(self, screen):
        print("game over")
        death_screen(screen, self)
        ui_text(screen, self)


#updates all tracked timers,   happens once per game loop
    def update_timers(self, screen, dt):
        self.nuke_cooldown -= dt
        self.cooldown -= dt
        self.grace_timer -= dt
        if self.grace_timer <= 0:
            self.can_be_damaged = True
        ui_text(screen, self)
        life_text(screen, self)
    


            
        
        

