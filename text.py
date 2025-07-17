import pygame
from constants import *
pygame.init()
pygame.font.init()
font_d = pygame.font.SysFont(None, 144)
font = pygame.font.Font('couri.ttf', 36)
death_text = font_d.render(f"YOU DIED", True, (255, 0, 0))
score_text = font.render(f'Score:', True, (255, 255, 255))
nuke_text = font.render(f'Nuke  ', True, (255, 255, 255))
nuke_ready_text = font.render(f'Ready!', True, (0, 255, 0))




def ui_text(screen, myplayer, score):
    score_num = font.render(f'{score}', True, (255, 255, 255))
    nuke_cooldown_text = font.render(f'{myplayer.nuke_cooldown:.2f}', True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(score_num, (10, 50))
    screen.blit(nuke_text, (1050, 660))
    if myplayer.nuke_cooldown <= 0:
        screen.blit(nuke_ready_text, (1150, 660))
    else:
        screen.blit(nuke_cooldown_text, (1150, 660))
    





def death_screen(screen, myplayer):
    screen.blit(death_text, ((SCREEN_WIDTH / 4), (SCREEN_HEIGHT / 4)))
   
  
        
        
            
       











#        score_text = font.render(f'Score:', True, (255, 255, 255))
 #       score_num = font.render(f'{score}', True, (255, 255, 255))
  #      death_text = font_d.render(f"YOU DIED", True, (255, 0, 0))
   #     nuke_text = font.render(f'Nuke  ', True, (255, 255, 255))
    #    nuke_cooldown_text = font.render(f'{my_player.nuke_cooldown:.2f}', True, (255, 0, 0))
     #   nuke_ready_text = font.render(f'Ready!', True, (0, 255, 0))