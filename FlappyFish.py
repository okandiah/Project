import pygame
from pygame.locals import *
import random
import sys
from Classes import Fishy

pygame.init()

timer = pygame.time.Clock()
fps = 50
game_over= False
swimming = False

# screen size
size = (800, 600)
width = 800
height = 600

background = pygame.image.load('seabackground.png')
run = True
# opens up a window
screen = pygame.display.set_mode(size)
screen.blit(background, (0, 0))

fishy_group = pygame.sprite.Group()
swimmy = Fishy(100, height/2)
fishy_group.add(swimmy)

# ... (your existing code)

def play_screen():
    global run, swimming, game_over  # Declare run as global
    background2 = pygame.image.load('sandbackground.png')
    background_scroll = 0
    scroll_speed = 2

    while run and not game_over:
        timer.tick(fps)
        screen.blit(background, (0, 0))
        fishy_group.draw(screen)
        fishy_group.update()
        screen.blit(background2, (background_scroll, 250))
        background_scroll -= scroll_speed
        #has fish hit top
        if fishy_group.sprites()[0].rect.top <=-30:
            fishy_group.sprites()[0].rect.top = height
            game_over = True
        #has fish hit ground 
        if fishy_group.sprites()[0].rect.bottom < height:
            fishy_group.sprites()[0].rect.y += int(fishy_group.sprites()[0].vel)
        else:
            fishy_group.sprites()[0].rect.bottom = height
            game_over = True
        if pygame.mouse.get_pressed()[0] == 1 and swimmy.clicked==False:
            fishy_group.sprites()[0].clicked = True
            fishy_group.sprites()[0].vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            fishy_group.sprites()[0].clicked = False
        if abs(background_scroll) > 35:
            background_scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and swimming == False and game_over == False:
                swimming = True

        pygame.display.update()

def main_screen():
    global run, swimming  # Declare run as global
    color = (0, 0, 0)
    title_colour = (124, 252, 0)
    color_light = (255, 215, 0)
    color_dark = (255, 244, 0)
    smallfont = pygame.font.SysFont('Corbel', 30)
    instructionfont = pygame.font.SysFont('Corbel', 35)

    text = smallfont.render('INSTRUCTIONS', True, color)
    itext = instructionfont.render('PLAY', True, color)
    titlefont = pygame.font.Font('waterpark.ttf', 120)
    title = titlefont.render("Swimmy Fish", True, title_colour)
    screen.blit(title, (40, 40))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                button_width = 200
                button_height = 70
                button_x = (width - button_width) // 2
                button_y = (height - button_height) // 2

                if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
                    run = True
                    play_screen()

        ibutton_width = 220
        ibutton_height = 80
        ibutton_x = (width - ibutton_width) // 2
        ibutton_y = (height - ibutton_height) // 2

        button_width = 220
        button_height = 80
        button_x = (width - button_width) // 2
        button_y = (height - button_height) // 1.5

        mouse = pygame.mouse.get_pos()

        if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
            pygame.draw.rect(screen, color_light, [button_x, button_y, button_width, button_height])
        else:
            pygame.draw.rect(screen, color_dark, [button_x, button_y, button_width, button_height])

        if ibutton_x <= mouse[0] <= ibutton_x + ibutton_width and ibutton_y <= mouse[1] <= ibutton_y + ibutton_height:
            pygame.draw.rect(screen, color_light, [ibutton_x, ibutton_y, ibutton_width, ibutton_height])
        else:
            pygame.draw.rect(screen, color_dark, [ibutton_x, ibutton_y, ibutton_width, ibutton_height])

        screen.blit(text, (button_x + 15, button_y + 25))
        screen.blit(itext, (ibutton_x + 75, ibutton_y + 25))

        pygame.display.update()

# Call main_screen() to start the game
main_screen()
