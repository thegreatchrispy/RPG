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
#          -- An over world where the main character interacts
#          -- A simple battle system incorporating the stats:
#             *STRENGTH*
#             *DEFENSE*
#             *VITALITY*
#             *INTELLIGENCE*
#             *AGILITY*
#          -- A leveling system that incorporates health & mana
#          -- A map system to display onscreen
#          -- An item system: stats, abilities, price
#
# Date:    02/14/15
# *************************************************************
#
# -------------------------------------------------------------
# Import statements:
import pygame, sys
from player import *
from colorPalette import *
from pygame.locals import *
# -------------------------------------------------------------
# Define constants:
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
MOVESPEED = 6
SPAWNPOINT = (0,0)

BGCOLOR = BLACK
PLAYERSIZE = 32 # size of player sprite in pixels
TITLE = "RPG" # Game title

# -------------------------------------------------------------
# Define variables:


# -------------------------------------------------------------
# Function definitions:
def set_background(screen, color):
    background = pygame.Surface(screen.get_size())
    background.fill(color)
    background = background.convert()
    screen.blit(background,(0,0))
    return background

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get():
        if event == QUIT:
            terminate()
        if event == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
        break

def noWallCollision(rect):
    return True

# -------------------------------------------------------------
# Main Game Loop:
def main():
    # Starting point of the game
    pygame.init() # initialize pygame modules
    mainClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    #background = set_background(DISPLAYSURF,BGCOLOR)
    pygame.display.set_caption(TITLE) # Game title in the window.

    player = pygame.Rect(WINDOWWIDTH / 2, WINDOWHEIGHT / 2, PLAYERSIZE, PLAYERSIZE)
    playerImage = pygame.image.load('TESTIMAGE.png')


    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False


    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                # change the keyboard variables
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False
                if event.key == ('r'):
                    player.topleft = (SPAWNPOINT)

        # draw the background onto the surface
        DISPLAYSURF.fill(BGCOLOR)

        if moveDown and player.bottom < WINDOWHEIGHT:
            player.top += MOVESPEED
        if moveUp and player.top > 0:
            player.top -= MOVESPEED
        if moveLeft and player.right < WINDOWWIDTH:
            player.left -= MOVESPEED
        if moveRight and player.bottom < WINDOWHEIGHT:
            player.right += MOVESPEED

        # draw the block onto the surface
        DISPLAYSURF.blit(playerImage, player)

        pygame.display.update()
        mainClock.tick(40)

if __name__ == "__main__":
    main()