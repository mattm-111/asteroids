import pygame
from constants import *
pygame.init()
pygame.font.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


font_d = pygame.font.SysFont(None, 144)
font = pygame.font.Font('couri.ttf', 36)
death_text1 = font_d.render(f"ALL YOUR BASE IS", True, red)
death_text2 = font_d.render(f'BELONG TO US!!!!!', True, red)
score_text = font.render(f'Score:', True, white)
nuke_text = font.render(f'Nuke  ', True, white)
nuke_ready_text = font.render(f'Ready!', True, green)
player_life_text = font.render(f'Ships', True, white)
player_life_three = font.render(f'O O O', True, white)
player_life_two = font.render(f'O O', True, white)
player_life_one = font.render(f'O', True, white)
player_life_dead = font.render(f' ', True, white)


###############################


def ui_text(screen, myplayer):
    score_num = font.render(f'{myplayer.score}', True, (255, 255, 255))
    nuke_cooldown_text = font.render(f'{myplayer.nuke_cooldown:.2f}', True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(score_num, (10, 50))
    screen.blit(nuke_text, (1040, 670))
    if myplayer.nuke_cooldown <= 0:
        screen.blit(nuke_ready_text, (1140, 670))
    else:
        screen.blit(nuke_cooldown_text, (1140, 670))

def life_text(screen, myplayer):
    screen.blit(player_life_text, (1150,10))
    if myplayer.lives == 3:
        screen.blit(player_life_three, (1150, 50))
    elif myplayer.lives == 2:
        screen.blit(player_life_two, (1150,50))
    elif myplayer.lives == 1:
        screen.blit(player_life_one, (1150,50))
    else:
        screen.blit(player_life_dead, (1150,50))
    





def death_screen(screen, myplayer):
    screen.blit(death_text1, (150, 225))
    screen.blit(death_text2, (150, 425))


   
  
        
        
            
       











#        score_text = font.render(f'Score:', True, (255, 255, 255))
 #       score_num = font.render(f'{score}', True, (255, 255, 255))
  #      death_text = font_d.render(f"YOU DIED", True, (255, 0, 0))
   #     nuke_text = font.render(f'Nuke  ', True, (255, 255, 255))
    #    nuke_cooldown_text = font.render(f'{my_player.nuke_cooldown:.2f}', True, (255, 0, 0))
     #   nuke_ready_text = font.render(f'Ready!', True, (0, 255, 0))