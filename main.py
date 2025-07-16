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
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('couri.ttf', 36)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    ## Create some pygame groups and containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots_group, updatable, drawable)
    
    ##Init some vars
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    my_asteroids = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    
    ##score keeping function
    

    ## Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for player in drawable:
            player.draw(screen)
        updatable.update(dt)
        score_text = font.render(f'Score:', True, (255, 255, 255))
        score_num = font.render(f'{score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit (score_num, (10, 50))
        for roids in asteroids_group:
            if my_player.collide(roids) == True:
                print("game over")
                time.sleep(1)
                sys.exit()
            for shot in shots_group:
                if shot.collide(roids):
                    shot.kill()
                    roids.split()
                    score += 100
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
    




















if __name__ == "__main__":
    main()

