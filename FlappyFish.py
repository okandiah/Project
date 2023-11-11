import pygame
from pygame.locals import *
import random
import sys

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


class Fishy(pygame.sprite.Sprite):
    def __init__(self, x, y):  # Fix: Corrected the typo here
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            fishy = pygame.image.load(f'fishy{num}.png')
            self.images.append(fishy)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel=0
        self.clicked=False

    def update(self):
        self.vel +=0.5
        self.vel += 0.5
        if self.vel > 8:
            self.bel=8
        if self.rect.bottom < 545:
            self.rect.y += int(self.vel)
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
            self.clicked = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

			#handle the animation
        self.counter += 1
        swim_cooldown = 5
            
        if self.counter > swim_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.image = self.images[self.index]
            #rotate bird
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)


fishy_group = pygame.sprite.Group()
swimmy = Fishy(100, height/2)
fishy_group.add(swimmy)


def play_screen():
    background2 = pygame.image.load('sandbackground.png')
    background_scroll = 0
    scroll_speed = 2

    while run:
        timer.tick(fps)
        screen.blit(background, (0, 0))
        fishy_group.draw(screen)
        fishy_group.update()  # Fix: Corrected the method name here
        screen.blit(background2, (background_scroll, 250))
        background_scroll -= scroll_speed

        if abs(background_scroll) > 35:
            background_scroll = 0

        # for loop allows the user to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main_screen():
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

            if type(event) == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button, switch to the play screen
                mouse = pygame.mouse.get_pos()
                button_width = 200
                button_height = 70
                button_x = (width - button_width) // 2
                button_y = (height - button_height) // 2
                run=False
                if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
                    run=True
                    play_screen()
                else:
                    run =False
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
        # changes to a lighter shade
        if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
            pygame.draw.rect(screen, color_light, [button_x, button_y, button_width, button_height])
        else:
            pygame.draw.rect(screen, color_dark, [button_x, button_y, button_width, button_height])

        # superimposing the text onto our button
        screen.blit(text, (button_x + 65, button_y + 20))

        # updates the frames of the game
        pygame.display.update()


main_screen()

# Call main_screen() to start the game
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