import pygame
import sys
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from nuke import NuclearMissleBomb, Splosion
from checks import asteroid_collision_check, shockwave_growth, draw_sprites


def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('couri.ttf', 36)
    font_d = pygame.font.SysFont(None, 144)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    ## Create some pygame groups and containers for easier loops through class objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    nuke_group = pygame.sprite.Group()
    shockwave_group = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots_group, updatable, drawable)
    NuclearMissleBomb.containers = (nuke_group, updatable, drawable)
    Splosion.containers = (shockwave_group)

    
    ##Init some vars
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    my_asteroids = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    

    ## Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")       
        shockwave_growth(screen, shockwave_group, dt)                                                                  #grow shockwave first so player drawn on-top of it
        draw_sprites(screen, drawable)
        updatable.update(dt)
        asteroid_collision_check(screen, my_player, asteroids_group, shots_group, shockwave_group, nuke_group, dt)     #loop through each asteroid checking for player, shot, nuke, shockwave collisions
        my_player.update_timers(screen, dt)                                                                            #updates cooldown timers and refreshes the render for on-screen timers
        pygame.display.flip()                                                                                          #refreshes screen
        dt = (clock.tick(60) / 1000)                                                                                   #clock based on 60FPS
    



if __name__ == "__main__":
    main()

