# -*- coding: Utf-8 -*
"""
game mc_gyver_rescue
escape game with 3 objects for win.

Script Python
Files : main.py, classes.py, constantes.py, l1, l2 + images
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

#Open window Pygame
window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
#Icone
icone = pygame.image.load(ICONE_IMAGE)
pygame.display.set_icon(icone)
#Title
pygame.display.set_caption(WINDOW_TITLE)


#PRINCIPAL LOOP
carry_on = 1

def loading_home_page(image):
    home = pygame.image.load(image).convert()
    window.blit(home, (0,0))

def display_new_position():
        #Displays at new positions
        window.blit(fond, (0,0))
        level.display(window)
        window.blit(mc.direction, (mc.x, mc.y))
        pygame.display.flip()


while carry_on:

    loading_home_page(HOME_IMAGE)

    #refresh
    pygame.display.flip()

    # we remake variables to 1 for each looping
    carry_on_game = 1
    carry_on_home = 1

    #MENU LOOP
    while carry_on_home:
    
        #Limit of loop speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
        
            #If user leave, we make variables to loop
            #at 0 for don't launch anything and exit
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                carry_on_home = 0
                carry_on_game = 0
                carry_on = 0
                #Variable for choice level
                choice = 0
                
            elif event.type == KEYDOWN:				
                #Launch choice 1
                if event.key == K_F1:
                    carry_on_home = 0	#Leave home
                    choice = 'l1'		#We init the choice to Launch
                # launch to choice 2
                elif event.key == K_F2:
                    carry_on_home = 0
                    choice = 'l2'
            
        
    #Verification than user have make a choice for don't load if he leaves
    if choice != 0:
        #Loading background
        fond = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()

        #Generate a choice from a FILE
        level = Level(choice)
        level.generate()
        level.display(window)

        #Creation of mc Gyver
        mc = Character(IMAGE_CHARACTER, level)

                
    #GAME LOOP
    while carry_on_game:
    
        #Limit speed looping
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():
        
            #if user leave, we make the variable who continue the game quand
            #the variable general at 0 for close the window
            if event.type == QUIT:
                carry_on_game = 0
                carry_on = 0
        
            elif event.type == KEYDOWN:
                #if user push escape here, we comeback only at home
                if event.key == K_ESCAPE:
                    carry_on_game = 0
                    
                #Keyboard of moove to mc_giver
                elif event.key == K_RIGHT:
                    mc.moove('right')
                elif event.key == K_LEFT:
                    mc.moove('left')
                elif event.key == K_UP:
                    mc.moove('up')
                elif event.key == K_DOWN:
                    mc.moove('down')			
            
        display_new_position()
        if level.structure[mc.case_y][mc.case_x] == 'e': #and mc_gyver == 3
            carry_on_game = 0

############### # IDEA:
# mc_giver = 0
# endsprite = 3
# if sprite == object:
#     mc_giver += 1
# if mc_giver == endsprite: donc 3
#     game = win !
# else:
#     game = lost !
