import pygame
from pygame.locals import *
import sys
import random

swimming = False
game_over = False

class Fishy(pygame.sprite.Sprite):
    global swimming, game_over
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