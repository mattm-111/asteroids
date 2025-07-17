import pygame
import sys
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from nuke import NuclearMissleBomb, Splosion
from text import ui_text, death_screen, life_text




def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('couri.ttf', 36)
    font_d = pygame.font.SysFont(None, 144)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    ## Create some pygame groups and containers
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
        
        for shockwave in shockwave_group:
            if shockwave.radius >= 15 and shockwave.radius <300:
                shockwave.grow_shockwave(dt)
                shockwave.draw(screen)
            else:
                shockwave.kill()        
        for player in drawable:
            player.draw(screen)
        updatable.update(dt)
        for roids in asteroids_group:
            if my_player.collide(roids) == True:
                print("game over")
                death_screen(screen, my_player)
                pygame.display.flip()
                time.sleep(3)
                sys.exit()
            for shot in shots_group:
                if shot.collide(roids):
                    shot.kill()
                    roids.split()
                    my_player.score_up()
            for shockwave in shockwave_group:
                if shockwave.collide(roids):
                    roids.split()
                    my_player.score_up()
            for nuke in nuke_group:
                if nuke.collide(roids):
                    roids.split()
                    nuke.detonate(dt)
                    nuke.kill()
                    my_player.score_up()
        my_player.nuke_cooldown -= dt
      
        ui_text(screen, my_player)
        life_text(screen, my_player)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
    




















if __name__ == "__main__":
    main()

