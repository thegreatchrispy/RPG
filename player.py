# *************************************************************
# Purpose: This class allows for the representation of the
#          player as a sprite on the over world.
# Date:    02/14/15
# *************************************************************
import pygame
from colorPalette import *

# -------------------------------------------------------------
# Definitions:
# Dictionary used to define movement directions.
# Process maps each key to a tuple that represents the unit
# vector of the direction key pressed.
MOVEMENTS = {pygame.K_LEFT: (-1,0),
             pygame.K_RIGHT: (1,0),
             pygame.K_UP: (0,-1),
             pygame.K_DOWN: (0,1) }
PLAYERSIZE = 32 # size of player sprite in pixels
# -------------------------------------------------------------
# Function definitions:
def create_test_shape(size, color):
    # Function needed to create a surface to represent the character
    surface = pygame.Surface(size)
    surface.fill(color)
    surface = surface.convert()
    return surface
# -------------------------------------------------------------
# Class definition:
class Player(pygame.sprite.Sprite):
    # Class containing the sprite information about the player
    # Attributes:
    #   pos     -- position on the screen
    #   image   -- surface object representing the player
    #   rect    -- rectangle of the player sprite

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [x,y]
        self.image = create_test_shape((PLAYERSIZE,PLAYERSIZE), WHITE)
        self.rect = self.image.get_rect()
        self.size = self.rect.size

    def update(self):
        self.rect.topleft = self.pos

    def move_char(self, keys_pressed, rect):
        # For each key that is pressed, move
        # the player in the right direction
        pixels = 2

        for key in keys_pressed.list:
            self.pos[0] = self.pos[0] + MOVEMENTS[key][0] * pixels
            self.pos[1] = self.pos[1] + MOVEMENTS[key][1] * pixels
        self.rect.move(self.pos)
        self.update()