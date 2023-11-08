import pygame
from pygame.locals import *
import random

pygame.init() 

width_screen = 1024
height_screen = 768

screen = pygame.display.set_mode(width_screen, height_screen)
pygame.caption.set_caption("Main Menu")

def create_main_text(text,font,text_colour,x,y):
    img = font.render(text, True, text_colour)
    screen.blit(img, (x, y))

run = True

while run:
    screen.fill((52, 78, 91))



#Main/ Starting Screen code
    #Button to show rules, button to start game

#Moving game screen

#Game animations and visuals

#Controls of the bird

#Adding the obstacles

#Adding a score (counter) 

#Replay game after loss

#test2