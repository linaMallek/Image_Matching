import pygame
import button
import numpy as np
import cv2
from fct import * 


pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")
bg = pygame.image.load("images/Multi_UI.png")
#game variables
paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
bloc_img = pygame.image.load("images/bloc.png").convert_alpha()
dico_img = pygame.image.load("images/dico.png").convert_alpha()
clear_img = pygame.image.load("images/clear.png").convert_alpha()
quit_img = pygame.image.load('images/quit.png').convert_alpha()


#create button instances
resume_button = button.Button(150, 230, bloc_img, 1)
dico_button = button.Button(397, 230, dico_img, 1)
clear_button = button.Button(287, 325, clear_img, 1)
quit_button = button.Button(20,540, quit_img, 1)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


run = True
while run:

      screen.blit(bg, (0, 0))

  

      menu_state == "main"

      if resume_button.draw(screen):
        recherchre_block()
        
      if dico_button.draw(screen):
        recherche_decho()
        

      if  clear_button.draw(screen):
        cv2.destroyAllWindows()
        
      
      if quit_button.draw(screen):
        
        run = False
 
  #event handler
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
             paused = True
         if event.type == pygame.QUIT:
             run = False

      pygame.display.update()

pygame.quit()