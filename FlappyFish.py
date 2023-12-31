# Swimmy Fish
# NE 111 Final Project
# By Ovia Kandiah and Anoushka Saha
# Dec. 5th, 2023

# Importing needed modules
import pygame
from pygame.locals import *
import random

# Initializing modules
pygame.init()

# Window name
pygame.display.set_caption('Swimmy Fish')

# Defining variables
timer = pygame.time.Clock()
fps = 50
game_over= False
swimming = False
score = 0
pass_obstacle = False

obstacle_gap = 300
obstacle_frequency = 1300
last_obstacle = pygame.time.get_ticks() - obstacle_frequency
scroll_speed = 2

# Screen size
width = 800
height = 600
size = (width, height)

background = pygame.image.load('seabackground.png')
run = True

# Opens up a window
screen = pygame.display.set_mode(size)
screen.blit(background, (0, 0))

###############################################################################################
# Class Name        : Fishy
# Class Parameter   : pygame.sprite.Sprite
# Class Description : Controls animation and graphics of fish character

class Fishy(pygame.sprite.Sprite):
    # __init___ initializes the attributes of an object when it is formed
    def __init__(self, x, y):  
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):

            # 3 images of fish being imported then added to list
            fishy = pygame.image.load(f'fishy{num}.png')
            self.images.append(fishy)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Positioning of the fish using get_rect()
        self.rect.center = [x, y]
        self.vel=0
        self.clicked=False

    def update(self):

        # Defining the gravity and motion of the fish
        if swimming == True:

            # Jump fishy, adding 0.5 to velocity to make sure the fish accelerates
            self.vel +=0.5

            # Limits velocity to 8, so speed is reasonable
            if self.vel > 8:
                self.vel=8
        else:
            self.vel += 0.5
            if self.vel<8:
                self.vel=8

        self.counter += 1
        swim_cooldown = 5
            
        if self.counter > swim_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.image = self.images[self.index]

            # Rotate fish
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)

###############################################################################################
# Class Name        : obstacles
# Class Parameter   : pygame.sprite.Sprite 
# Class Description : Controls animation and graphics of pipe obstacles

class obstacles(pygame.sprite.Sprite):

    # Initializing the pipe image as a sprite
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()

        # Positioning of pipes as obstacles with gaps in between
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y - int(obstacle_gap/2)]
        if position == -1:
            self.rect.topleft = [x,y + int(obstacle_gap/2)]
    
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


fishy_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

swimmy = Fishy(100, height/2)
fishy_group.add(swimmy)

###############################################################################################
# Function Name        : reset_game()
# Function Parameter   : None
# Function Returns     : None
# Function Description : Clears all variables and sprite groups required to restart game

def reset_game():
    global swimming, game_over, last_obstacle, pass_obstacle, score, fishy_group, obstacle_group

    swimming = False
    game_over = False
    last_obstacle = pygame.time.get_ticks() - obstacle_frequency
    pass_obstacle = False
    score = 0

    # Clear existing sprite groups and recreate the fishy sprite
    fishy_group.empty()
    obstacle_group.empty()
    swimmy = Fishy(100, height/2)
    fishy_group.add(swimmy)

###############################################################################################
# Function Name        : play_screen()
# Function Parameter   : None
# Function Returns     : None
# Function Description : Controls gameplay

def play_screen():

    #Ensure variables are available in each function by declaring as global
    global run, swimming, game_over, last_obstacle, pass_obstacle, score
    background2 = pygame.image.load('sandbackground.png')
    background_scroll = 0
    scroll_speed = 2

    #game loop
    while run and not game_over:

        # Create the necessary graphics for when the game is running
        timer.tick(fps)
        screen.blit(background, (0, 0))
        fishy_group.draw(screen)
        obstacle_group.draw(screen)
        fishy_group.update()
        obstacle_group.update()

        # Draw the ground
        screen.blit(background2, (background_scroll, 475))
        background_scroll -= scroll_speed

        # Check the score
        if len(obstacle_group)>0:
            if fishy_group.sprites()[0].rect.right >= obstacle_group.sprites()[0].rect.left and fishy_group.sprites()[0].rect.left <= obstacle_group.sprites()[0].rect.right and not pass_obstacle:
                pass_obstacle = True
                score +=1
            if pass_obstacle == True and fishy_group.sprites()[0].rect.left> obstacle_group.sprites()[0].rect.right:
                pass_obstacle = False
        
        # Display score
        color = (255, 100 ,2)
        smallfont = pygame.font.SysFont('Corbel', 50)
        score_text = smallfont.render(str(score), True, color)
        screen.blit(score_text,(int(width/2),20))

        # If fish collides with pipe the game is over and can be replayed
        if pygame.sprite.groupcollide(fishy_group, obstacle_group, False, True) or swimmy.rect.top<0:
            game_over = True
            reset_game()
            main_screen()

        # If fish hits top border the game is over and can be replayed
        if fishy_group.sprites()[0].rect.top <=-30:
            fishy_group.sprites()[0].rect.bottom = height
            game_over = True
            reset_game()
            main_screen()

        # # If fish hits ground the game is over and can be replayed 
        if fishy_group.sprites()[0].rect.bottom < (height - 75):
            fishy_group.sprites()[0].rect.y += int(fishy_group.sprites()[0].vel)
        else:
            fishy_group.sprites()[0].rect.bottom = height
            game_over = True
            reset_game()
            main_screen()
        
        # Makes the fish jump when the mouse is clicked
        if pygame.mouse.get_pressed()[0] == 1 and swimmy.clicked==False:
            fishy_group.sprites()[0].clicked = True
            fishy_group.sprites()[0].vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            fishy_group.sprites()[0].clicked = False

        # Adding obstacles specific intervals and random heights if the game is in play and the fish is swimming
        if game_over== False and swimming == True:
            time_now = pygame.time.get_ticks()
            if (time_now - last_obstacle) > obstacle_frequency:
                obstacle_height = random.randint(-100,100)
                bottom_obstacle = obstacles(width, int(height/2)+ obstacle_height, -1)
                top_obstacle = obstacles(width, int(height/2)+ obstacle_height, 1)
                obstacle_group.add(bottom_obstacle)
                obstacle_group.add(top_obstacle)
                last_obstacle = time_now
                background_scroll -= scroll_speed
                if abs(background_scroll) > 35:
                    background_scroll = 0
                    obstacle_group.update()

        # Checks if mouse is being clicked to play game or to exit game, overall allows user to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and swimming == False and game_over == False:
                swimming = True

        pygame.display.update()

###############################################################################################
# Function Name        : main_screen()
# Function Parameter   : None
# Function Returns     : None
# Function Description : Displays the home screen and button that starts the game

def main_screen():
    global run  

    # Graphics of main screen
    color = (0, 0, 0)
    title_colour = (124, 252, 0)
    color_light = (255, 215, 0)
    color_dark = (255, 244, 0)
    #importing fonts
    playfont = pygame.font.SysFont('Corbel', 35)
    ptext = playfont.render('PLAY', True, color)
    titlefont = pygame.font.Font('waterpark.ttf', 120)
    title = titlefont.render("Swimmy Fish", True, title_colour)
    screen.blit(title, (40, 40))

    # Sizing of button
    ibutton_width = 220
    ibutton_height = 80
    ibutton_x = (width - ibutton_width) // 2
    ibutton_y = (height - ibutton_height) // 2

    #While program runs it is checking mouse movement on main screen
    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            # Checks if window is being closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If play button is clicked, play_screen() is called and the game starts
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ibutton_x <= mouse[0] <= ibutton_x + ibutton_width and ibutton_y <= mouse[1] <= ibutton_y + ibutton_height:
                    run = True
                    play_screen()

        # Drawing button and changing button color based on mouse hovering
        if ibutton_x <= mouse[0] <= ibutton_x + ibutton_width and ibutton_y <= mouse[1] <= ibutton_y + ibutton_height:
            pygame.draw.rect(screen, color_light, [ibutton_x, ibutton_y, ibutton_width, ibutton_height])
        else:
            pygame.draw.rect(screen, color_dark, [ibutton_x, ibutton_y, ibutton_width, ibutton_height])

        # Displaying text on button
        screen.blit(ptext, (ibutton_x + 75, ibutton_y + 25))

        pygame.display.update()

# Call main_screen() to start the game
main_screen()
