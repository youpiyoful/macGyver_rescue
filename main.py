# -*- coding: Utf-8 -*
"""
game mc_gyver_score_rescue
escape game with 3 objects for win.

Script Python
Files : main.py, classes.py, constantes.py, l1, l2 + images
"""
import pygame

from pygame.constants import KEYDOWN
from pygame.constants import K_ESCAPE
from pygame.constants import K_DOWN
from pygame.constants import K_F1
from pygame.constants import K_F2
from pygame.constants import K_LEFT
from pygame.constants import K_RIGHT
from pygame.constants import K_UP
from pygame.constants import QUIT

from classes import Character
from classes import Level
from constantes import BACKGROUND_IMAGE
from constantes import HOME_IMAGE
from constantes import ICONE_IMAGE
from constantes import IMAGE_CHARACTER
from constantes import LOST
from constantes import WIN
from constantes import WINDOW_TITLE
from constantes import WINDOW_SIDE


def initialize_window():
    pygame.init()
    # Open window Pygame
    window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
    # Icone
    icone = pygame.image.load(ICONE_IMAGE)
    pygame.display.set_icon(icone)
    # Title
    pygame.display.set_caption(WINDOW_TITLE)
    return window


def loading_home_page(image, window):
    home = pygame.image.load(image).convert()
    window.blit(home, (0, 0))


def display_new_position(background, level, character, window):
    # Displays at new positions
    window.blit(background, (0, 0))  # Reload background with good position
    level.display(window)  # Reload the element of the map at the good position
    window.blit(character.direction, (character.x, character.y)) # Reload character at the good position in the map
    pygame.display.flip()  # Update the "surface"


def end_game(character, window):
    win = 1
    lost = 0

    if character == 3:
        print("you win !")
        image_win = pygame.image.load(WIN).convert_alpha()
        window.blit(image_win, (0, 0))
        result = win

    else:
        print("game over !")
        image_lost = pygame.image.load(LOST).convert_alpha()
        window.blit(image_lost, (0, 0))
        result = lost
            
    pygame.display.flip()
    return result


def initialize_background():
    background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()  # Loading background
    return background


def init_level(choice, window):
    # Generate a choice from a FILE
    level = Level(choice)
    level.generate()
    level.random_obj()
    level.display(window)
    return level


def score_meter(position, score, quest_item_list):
    if position == 'N' and 'N' not in quest_item_list:
        score += 1
    
    elif position == 'T' and 'T' not in quest_item_list:
        score += 1

    elif position == 'E' and 'E' not in quest_item_list:
        score += 1

    return score


def transform_object_in_empty_case(position):
    if position == 'E' or position == 'N' or position == 'T':
        position = '0'
    return position


def stock_quest_item(position, quest_item_list):

    if position == 'N' and 'N' not in quest_item_list:
        quest_item_list.append('N')

    elif position == 'T' and 'T' not in quest_item_list:
        quest_item_list.append('T')

    elif position == 'E' and 'E' not in quest_item_list:
        quest_item_list.append('E')
    
    return quest_item_list


def main():
    window = initialize_window()
    carry_on = 1  # Start the loop

    # MAIN LOOP
    while carry_on:
        mc_gyver_score = 0  # Init the variable score
        quest_item_list = []  # Create list for stock quest item
        loading_home_page(HOME_IMAGE, window)

        # refresh
        pygame.display.flip()

        # we remake variables to 1 for each looping
        carry_on_game = 1
        carry_on_home = 1
        
        # MENU LOOP
        while carry_on_home:
            # Limit of loop speed
            pygame.time.Clock().tick(30)
        
            for event in pygame.event.get():
            
                # If user leave, we make variables to loop at 0 for don't launch anything and exit
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    carry_on_home = 0
                    carry_on_game = 0
                    carry_on = 0
                    choice = 0  # Variable for choice level
                    
                elif event.type == KEYDOWN:
                    # Launch choice 1
                    if event.key == K_F1:
                        carry_on_home = 0  # Leave home
                        choice = 'l1'  # Map choice
                        
                    # launch to choice 2
                    elif event.key == K_F2:
                        carry_on_home = 0
                        choice = 'l2'

        # Verification than user have make a choice for don't load if he leaves
        if choice != 0:
            level = init_level(choice, window)
            background = initialize_background()
            mc = Character(IMAGE_CHARACTER, level)  # Creation of mc Gyver
                    
        # GAME LOOP
        while carry_on_game:
            # Limit speed looping
            pygame.time.Clock().tick(30)
        
            for event in pygame.event.get():
            
                # If user leave, variable who continue the game = 0 for close the window
                if event.type == QUIT:
                    carry_on_game = 0
                    carry_on = 0
            
                elif event.type == KEYDOWN:

                    # If user push escape here, we comeback only at home
                    if event.key == K_ESCAPE:
                        carry_on_game = 0
                        
                    # Keyboard of moove to mc_gyver
                    elif event.key == K_RIGHT:
                        mc.moove('right')

                    elif event.key == K_LEFT:
                        mc.moove('left')

                    elif event.key == K_UP:
                        mc.moove('up')

                    elif event.key == K_DOWN:
                        mc.moove('down')			
            
            display_new_position(background, level, mc, window)
            position = level.structure[mc.case_y][mc.case_x]  # Store position in a variable named position
            mc_gyver_score = score_meter(position, mc_gyver_score, quest_item_list)  # calcul and return score
            quest_item_list = stock_quest_item(position, quest_item_list)  # Insert the object into a list

            # delete the object pick up by mc_gyer of the map
            level.structure[mc.case_y][mc.case_x] = transform_object_in_empty_case(position)

            # verify if mc_gyver is on the end case
            if level.structure[mc.case_y][mc.case_x] == 'e':  # leave the game

                # displays possessed objects
                for item in quest_item_list:
                    print(item)

                # displays result message 
                while mc_gyver_score in [0, 1, 2, 3]:  # Allow to verify than mc_gyver is not None
                    print(mc_gyver_score)
                    end_game(mc_gyver_score, window)
                    
                    # allows you to leave the result image of the game
                    for event in pygame.event.get():
                        
                        if event.type == KEYDOWN:
                            carry_on_game = 0  # comeback in home loop
                            mc_gyver_score = None


main()
