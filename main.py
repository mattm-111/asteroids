import pygame
# import the connect_database function
# and the database_version variable
# from database.py into the current file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *
import sys
import time



def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots_group, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    my_asteroids = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for player in drawable:
            player.draw(screen)
        updatable.update(dt)
        for roids in asteroids_group:
            if my_player.collide(roids) == True:
                print("game over")
                time.sleep(1)
                sys.exit()
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
    




















if __name__ == "__main__":
    main()

