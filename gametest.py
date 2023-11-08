import pygame
import sys

# initializing the constructor
pygame.init()

# screen resolution
res = (1024, 768)
width = 1024
height = 768

background = pygame.image.load('gamebackground.png')

# opens up a window
screen = pygame.display.set_mode(res)
screen.blit(background, (0,0))

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (255, 215, 0)

# dark shade of the button
color_dark = (255, 244, 0)

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('quit', True, color)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            mouse = pygame.mouse.get_pos()
            button_width = 200
            button_height = 70
            button_x = (width - button_width) // 2
            button_y = (height - button_height) // 2
            if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
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
    screen.blit(text, (button_x + 70, button_y + 15))

    # updates the frames of the game
    pygame.display.update()


