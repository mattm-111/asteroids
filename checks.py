import pygame
import sys
import time
from constants import *


## for each asteroid,  checks to see if there is a collision with a player, shot, nuke, or shockwave and takes actions.

def asteroid_collision_check(screen, my_player, asteroids_group, shots_group, shockwave_group, nuke_group, dt):
    for roids in asteroids_group:
        #login on if a life needs to be taken away or if game ends
        if my_player.collide(roids) == True and my_player.can_be_damaged == True and my_player.lives > 1:
            my_player.on_hit()
        elif my_player.collide(roids) == True and my_player.can_be_damaged == True and my_player.lives == 1:
            my_player.on_death(screen)
            pygame.display.flip()
            time.sleep(3)
            sys.exit()
        #checks each shot and shockwave -  if collides deletes the object and calls the split method
        for shot in shots_group:
            if shot.collide(roids):
                shot.kill()
                roids.split()
                my_player.score_up()
        for shockwave in shockwave_group:
            if shockwave.collide(roids):
                roids.split()
                my_player.score_up()
        #checks to see if a nuke collides,  if it does calls detonate to start the shockwave
        for nuke in nuke_group:
            if nuke.collide(roids):
                roids.split()
                nuke.detonate(dt)
                nuke.kill()
                my_player.score_up()



def shockwave_growth(screen, shockwave_group, dt):
    for shockwave in shockwave_group:
        ##detects nuke detonation by checking if there is a shockwave with defualt radius.  Grows until reaches max radius before deleting the sprite.
        if shockwave.radius >= SHOCKWAVE_START_RADIUS and shockwave.radius < SHOCKWAVE_MAX_RADIUS:
            shockwave.grow_shockwave(dt)
            shockwave.draw(screen)
        else:
            shockwave.kill()  

def draw_sprites(screen, drawable):
    for player in drawable:
        player.draw(screen)

                


