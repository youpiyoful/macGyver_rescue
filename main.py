"""
Game Mac Gyver Rescue
Jeu dans lequel Mac Gyver doit réussir à rammasser trois objets pour endormir le gardien et s'échapper.

Script Python
Fichiers : main.py, classes.py, config.py, n1, n2 + images
"""


import pygame
from pygame.locals import *
from classes import *
from config import *

pygame.init()



# class Map:
# 	def openWindow(self, large, long):
# 		self.window = pygame.display.set_mode((large, long))
# 	def loadBackground(self, backgroundImage):
# 		self.background = pygame.image.load(backgroundImage).convert()
# 	def stickBackground(self, background):

#Open window Pygame
window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))

#Load background
# background = pygame.image.load("background.jpg").convert()
# window.blit(background, (0,0))

#Load perso
# perso = pygame.image.load("perso.png").convert_alpha()
# position_perso = perso.get_rect()
# window.blit(perso, position_perso)

#Icon
icon = pygame.image.load(ICON_IMAGE)
pygame.display.set_icon(icon)

#Title
pygame.display.set_caption(WINDOW_TITLE)


#Screen refresh
# def screenRefresh():
# 	pygame.display.flip()

start = 1

# PRINCIPAL LOOP
while start:
    #Loading and display of home screen
    home = pygame.image.load(HOME).convert()
    window.blit(home, (0,0))

    #refresh
    pygame.display.flip()

    # we remake variables to 1 for each looping
    game_continue = 1
    home_continue = 1

    #MENU LOOP
    while home_continue:

        #Limit of loop speed
        pygame.time.Clock().tick(30)
        
        #GAME LOOP
        for event in pygame.event.get():

            #If user leave, we make variables to loop
            #at 0 for don't launch anything and exit
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                home_continue = 0
                game_continue = 0
                start = 0
                #Variable for choice choice
                choice = 0

            elif event.type == KEYDOWN:
                #Launch choice 1
                if event.key == K_F1:
                    home_continue = 0 #Leave home
                    choice = 'l1' #We init the choice to Launch
                # launch to choice 2
                elif event.key == K_F2:
                    home_continue = 0
                    choice = 'l2'

#Verification than user have make a choice for don't load if he leaves
if choice != 0:
    #Loading background
    background = pygame.image.load(background_image).convert()

    #Generate a choice from a FILE
    level = Level(choice)
    level.generate()
    level.display(window)

    #Creation of mc Gyver
    mc_giver = Perso(CHARACTER, level)

#Looping of game_continue
while game_continue:

    #Limit speed looping
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():

        #if user leave, we make the variable who continue the game quand
        #the variable general at 0 for close the window
        if event.type == QUIT:
            game_continue = 0
            start = 0

        elif event.type == KEYDOWN:
            #if user push escape here, we comeback only at home
            if event.key == K_ESCAPE:
                game_continue = 0

            #Keyboard of moove to mc_giver
        elif event.key == K_RIGHT:
            mc_giver.moove('right')
        elif event.key == K_LEFT:
            mc_giver.moove('left')
        elif event.key == K_UP:
            mc_giver.moove('up')
        elif event.key == K_DOWN:
            mc_giver.moove('down')

    #Displays at new positions
    window.blit(background, (0,0))
    level.display(window)
    window.blit(mc_giver, (mc_giver.x, mc_giver.y))

    pygame.display.flip()

    #victory -> Comeback to home
    if level.structure[mc_giver.sprite_y][mc_giver.sprite_x] == 'a':
        game_continue = 0



    while condition:
        pygame.time.Clock().tick(30)
        pass

############### # IDEA:
# mc_giver = 0
# endsprite = 3
# if sprite == object:
#     mc_giver += 1
# if mc_giver == endsprite: donc 3
#     game = win !
# else:
#     game = lost !


#Infinite loop
# continuer = 1
# while continuer:
# 	for event in pygame.event.get():	#Attente des événements
# 		if event.type == QUIT:
# 			continuer = 0
# 		if event.type == KEYDOWN:
# 			# pygame.key.set_repeat(400, 30)
# 			if event.key == K_DOWN:	#Si "flèche bas"
# 				#On descend le perso
# 				position_perso = position_perso.move(0,3)
# 				# pygame.key.set_repeat(400, 30) pour répéter l'action quand la touche reste enfoncé.
# 			if event.key == K_UP:
# 				position_perso = position_perso.move(0,-3)
# 			if event.key == K_LEFT:
# 				position_perso = position_perso.move(-3,0)
# 			if event.key == K_RIGHT:
# 				position_perso = position_perso.move(3,0)
#
# 	#Re-sticking
# 	window.blit(background, (0,0))
# 	window.blit(perso, position_perso)
# 	#Refresh
# 	pygame.display.flip()
