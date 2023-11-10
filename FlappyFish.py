import pygame
from pygame.locals import *
import random
import sys
pygame.init()

timer=pygame.time.Clock()
fps=60
    # screen size
size = (1024, 768)
width = 1024
height = 768

background = pygame.image.load('gamebackground.png')
    #Main Screen
    # opens up a window
screen = pygame.display.set_mode(size)
screen.blit(background, (0,0))

def main_screen():
    #Main Screen
    # opens up a window
    screen.blit(background, (0,0))

# white color
    color = (0, 0, 0)

    # light shade of the button
    color_light = (255, 215, 0)

    # dark shade of the button
    color_dark = (255, 244, 0)

    # defining a font
    smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
    text = smallfont.render('PLAY', True, color)

    while True:

        for event in pygame.event.get():

            if type(event)== pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                mouse = pygame.mouse.get_pos()
                button_width = 200
                button_height = 70
                button_x = (width - button_width) // 2
                button_y = (height - button_height) // 2
                #play game
                if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
                    run = True
                    background2=pygame.image.load('gamebackground.png')
                    background_scroll=0
                    scroll_speed=4
                    while run:
                        timer.tick(fps)
                        screen.blit(background,(0,0))
                        screen.blit(background2,(background_scroll,768))
                        background_scroll -= scroll_speed
                        if abs(background_scroll)>35:
                            background_scroll=0
                    #for loop allows user to quit game
                        for event in pygame.event.get():
                            if type(event)== pygame.QUIT:
                                run=False
                    pygame.display.update
                else:
                    sys.exit()

        # fills the screen with a color
        # screen.fill((60, 25, 60))

        # Calculate the position of the button based on screen width and height
        button_width = 200
        button_height = 70
        button_x = (width - button_width) // 2
        button_y = (height - button_height) // 2

        # stores the (x, y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
            pygame.draw.rect(screen, color_light, [button_x, button_y, button_width, button_height])
        else:
            pygame.draw.rect(screen, color_dark, [button_x, button_y, button_width, button_height])

    # superimposing the text onto our button
        screen.blit(text, (button_x + 65, button_y + 20))

        # updates the frames of the game
        pygame.display.update()


main_screen()
#moving_game_screen()

#Main/ Starting Screen code
    #Button to show rules, button to start game
#Moving game screen

#Game animations and visuals

#Controls of the bird

#Adding the obstacles

#Adding a score (counter) 

#Replay game after loss

#test2