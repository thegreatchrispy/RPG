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

# -------------------------------------------------------------
# Main Game Loop:
def main():
    # Starting point of the game
    pygame.init() # initialize pygame modules
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    background = set_background(DISPLAYSURF,BGCOLOR)
    pygame.display.set_caption(TITLE) # Game title in the window.
    #mainClock = pygame.time.Clock()
    KEYSPRESSED = []
    player = Player(0,0) # coordinates of spawn point
    allsprites = pygame.sprite.RenderPlain((player))

    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = True
                    moveRight = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = True
                    moveDown = False
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

            else:
                pass


        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False

        if moveLeft and player.rect.left > 0:
            KEYSPRESSED.append(K_LEFT)
            player.move_char(KEYSPRESSED, background.get_rect())
        if moveRight and player.rect.right < WINDOWWIDTH:
            KEYSPRESSED.append(K_RIGHT)
            player.move_char(KEYSPRESSED, background.get_rect())
        if moveUp and player.rect.top > 0:
            KEYSPRESSED.append(K_UP)
            player.move_char(KEYSPRESSED, background.get_rect())
        if moveDown and player.rect.bottom < WINDOWHEIGHT:
            KEYSPRESSED.append(K_DOWN)
            player.move_char(KEYSPRESSED, background.get_rect())

        allsprites.update()
        DISPLAYSURF.blit(background, (0,0))
        allsprites.draw(DISPLAYSURF)
        pygame.display.flip()

if __name__ == "__main__":
    main()