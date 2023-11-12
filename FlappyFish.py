import pygame
from pygame.locals import *
import random
import sys

pygame.init()

timer = pygame.time.Clock()
fps = 50
game_over= False
swimming = False

obstacle_gap = 150
obstacle_frequency = 1500
last_obstacle = pygame.time.get_ticks() - obstacle_frequency
scroll_speed = 2

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
        if swimming == True:
            #jump fishy
            self.vel +=0.5
            if self.vel > 8:
                self.vel=8
        else:
            self.vel += 0.5
            if self.vel<8:
                self.vel=8

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

class obstacles(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()

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

        #look for collisions 
        if pygame.sprite.groupcollide(fishy_group, obstacle_group, False, True) or flappy.rect.top<0:
            game_over = True
        #has fish hit top
        if fishy_group.sprites()[0].rect.top <=-30:
            fishy_group.sprites()[0].rect.bottom = height
            game_over = True
        #has fish hit ground 
        if fishy_group.sprites()[0].rect.bottom < height:
            fishy_group.sprites()[0].rect.y += int(fishy_group.sprites()[0].vel)
        else:
            fishy_group.sprites()[0].rect.bottom = height
            game_over = True
        
        #new obstacles
        if pygame.mouse.get_pressed()[0] == 1 and swimmy.clicked==False:
            fishy_group.sprites()[0].clicked = True
            fishy_group.sprites()[0].vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            fishy_group.sprites()[0].clicked = False

        if game_over== False and swimming == True:
            time_now = pygame.time.get_ticks()
            if time_now - last_obstacle>obstacle_frequency:
                obstacle_height = random.randint(-100,100)
                bottom_obstacle = obstacles(width, int(height/2)+ obstacle_height, -1)
                top_obstacle = obstacles(width, int(height/2)+ obstacle_height, 1)
                obstacle_group.add(bottom_obstacle)
                obstacle_group.add(top_obstacle)
                last_obstacle = time_now

                ground_scroll -= scroll_speed
                if abs(ground_scroll) > 35:
                    ground_scroll = 0
                    obstacle_group.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and swimming == False and game_over == False:
                swimming = True

        pygame.display.update()

def main_screen():
    global run  # Declare run as global
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
