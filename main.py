# -*- coding: Utf-8 -*
"""
game mc_gyver_rescue
escape game with 3 objects for win.

Script Python
Files : main.py, classes.py, constantes.py, l1, l2 + images
"""

import pygame

from pygame.locals import *
from random import *

from classes import *
from constantes import *

# def initialize():
pygame.init()
#Open window Pygame
window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
#Icone
icone = pygame.image.load(ICONE_IMAGE)
pygame.display.set_icon(icone)
#Title
pygame.display.set_caption(WINDOW_TITLE)



def loading_home_page(image):
    home = pygame.image.load(image).convert()
    window.blit(home, (0,0))

def display_new_position(background, level, character):
        #Displays at new positions
        window.blit(background, (0,0))
        level.display(window)
        window.blit(character.direction, (character.x, character.y))
        pygame.display.flip()

def end_game(character):
    win = 1
    lost = 0
    start_ticks = pygame.time.get_ticks() #starter tick

    if character == 3:
        print("you win !")
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000 #calculate how many seconds
        # print(seconds) #print how many seconds
        image_win = pygame.image.load(WIN).convert_alpha()
        window.blit(image_lost, (0,0))

        # if seconds == 10:
        result = win

    else:
        print("game over !")
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000 #calculate how many seconds
        # print(seconds) #print how many seconds
        image_lost = pygame.image.load(LOST).convert_alpha()
        window.blit(image_lost, (0,0))
        
        # if seconds > 10:
        result = lost
            
    pygame.display.flip()
    return result

def initialize_background():
    #Loading background
    background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()
    return background

def insert_object_randomly():
    """ Generate object randomly on the map """
    ether = Object(ETHER, level, "E")
    ether.display()
    needle = Object(NEEDLE, level, "N")
    needle.display()
    tube = Object(TUBE, level, "T")
    tube.display()

def init_level(choice):
    #Generate a choice from a FILE
    level = Level(choice)
    level.generate()
    level.display(window)
    return level

def main():
    carry_on = 1

    #MAIN LOOP
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
                        mc_gyver = 3
                    # launch to choice 2
                    elif event.key == K_F2:
                        carry_on_home = 0
                        choice = 'l2'
                        mc_gyver = 0
            
            
        #Verification than user have make a choice for don't load if he leaves
        if choice != 0:
            level = init_level(choice)
            background = initialize_background()
            # insert_object_randomly()
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
                        
                    #Keyboard of moove to mc_gyver
                    elif event.key == K_RIGHT:
                        mc.moove('right')

                    elif event.key == K_LEFT:
                        mc.moove('left')

                    elif event.key == K_UP:
                        mc.moove('up')

                    elif event.key == K_DOWN:
                        mc.moove('down')			
            
            display_new_position(background, level, mc)

            # mc_gyver = 2
            if level.structure[mc.case_y][mc.case_x] == 'e': #and mc_gyver == 3
                end_game(mc_gyver)

                # if event.key:
                #     carry_on_game = end_game(mc_gyver)
                # end_game(mc_gyver)
                # if end_game(mc_gyver) == 0:
                #     image_lost = pygame.image.load(LOST).convert_alpha()
                #     window.blit(image_lost, (0,0))
                #     pygame.display.flip()

main()


############### # IDEA:
# mc_giver = 0
# endsprite = 3
# if sprite == object:
#     mc_giver += 1
# if mc_giver == endsprite: donc 3
#     game = win !
# else:
#     game = lost !
