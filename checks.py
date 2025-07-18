import pygame
import sys
import time
from player import Player
from circleshape import CircleShape
from shot import Shot
from nuke import NuclearMissleBomb, Splosion

def asteroid_collision_check(screen, my_player, asteroids_group, shots_group, shockwave_group, nuke_group, dt):
    for roids in asteroids_group:
        if my_player.collide(roids) == True and my_player.can_be_damaged == True and my_player.lives > 1:
            my_player.on_hit()
        elif my_player.collide(roids) == True and my_player.can_be_damaged == True and my_player.lives == 1:
            my_player.on_death(screen)
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


def shockwave_growth(screen, shockwave_group, dt):
    for shockwave in shockwave_group:
        if shockwave.radius >= 15 and shockwave.radius <300:
            shockwave.grow_shockwave(dt)
            shockwave.draw(screen)
        else:
            shockwave.kill()  

def draw_sprites(screen, drawable):
    for player in drawable:
        player.draw(screen)

                


