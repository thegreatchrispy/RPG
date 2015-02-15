# *************************************************************
# Purpose: This is the main program for the first trial attempt
#          at making a simple RPG. Elements that are initially
#          to be included are as follows:
#          -- A four character party
#          -- A pause menu with options for:
#             *STATS*
#             *EQUIP*
#             *MAGIC*
#             *ITEMS*
#             *MAP*
#             *EXIT*
#          --
#
# Date:    02/14/15
# *************************************************************

import pygame, sys
from player import *
from colorPalette import *
from pygame.locals import *

# Define constants
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BGCOLOR = BLACK
PLAYERSIZE = 32 # size of player sprite in pixels

# Define variables


pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("RPG")
mainClock = pygame.time.Clock()

def set_background(screen, color):
    background = pygame.Surface(screen.get_size())
    background.fill(color)
    background = background.convert()
    screen.blit(background,(0,0))
    return background


while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            pass