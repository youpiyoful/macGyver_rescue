""" Main class of mac_gyver game."""
import pygame

from pygame.constants import QUIT, KEYDOWN, K_ESCAPE, K_F1, K_F2, K_RIGHT, K_LEFT, K_UP, K_DOWN

from class_character import Character
from class_initialize import Initializer
from constantes import HOME_IMAGE, IMAGE_CHARACTER


class MacGyverGame:
    """ mac_gyver_game  contain algorithm for launch game"""
    def __init__(self):
        pass

    @staticmethod
    def launch_game():
        """ main function who run 3 loops and call all the function"""
        window = Initializer.initialize_window()
        carry_on = 1  # Start the loop
        choice = 0  # Init value choice at 0

        # MAIN LOOP
        while carry_on:
            mc_gyver_score = 0  # Init the variable score
            quest_item_list = []  # Create list for stock quest item
            Initializer.loading_home_page(HOME_IMAGE, window)

            # refresh
            pygame.display.flip()

            # we remake variables to 1 for each looping
            carry_on_game = 0
            carry_on_home = 1

            while carry_on_home:
                # Limit of loop speed
                pygame.time.Clock().tick(30)

                for event in pygame.event.get():

                    carry_on = 1

                    # make variables to loop at 0 for don't launch anything and exit
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        carry_on_home = 0
                        carry_on_game = 0
                        carry_on = 0
                        choice = 0  # Variable for choice level

                    elif event.type == KEYDOWN:

                        # Launch choice 1
                        if event.key == K_F1:
                            carry_on_game = 1
                            carry_on_home = 0  # Leave home
                            choice = 'l1'  # Map choice

                        # launch to choice 2
                        elif event.key == K_F2:
                            carry_on_game = 1
                            carry_on_home = 0
                            choice = 'l2'

            # Verification than user have make a choice for don't load if he leaves
            if choice in ('l1', 'l2'):
                level = Initializer.init_level(choice, window)
                background = Initializer.initialize_background()
                mac = Character(IMAGE_CHARACTER, level)  # Creation of mac Gyver

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
                            mac.moove('right')

                        elif event.key == K_LEFT:
                            mac.moove('left')

                        elif event.key == K_UP:
                            mac.moove('up')

                        elif event.key == K_DOWN:
                            mac.moove('down')

                Initializer.display_new_position(background, level, mac, window)
                # Store position in a variable named position
                position = level.structure[mac.case_y][mac.case_x]
                # calcul and return score
                mc_gyver_score = Character.score_meter(position, mc_gyver_score, quest_item_list)
                # Insert the object into a list
                quest_item_list = Character.stock_quest_item(position, quest_item_list)

                # delete the object pick up by mc_gyer of the map
                to_pick_up = level.transform_case_object_in_empty_case(position)
                level.structure[mac.case_y][mac.case_x] = to_pick_up

                # verify if mc_gyver is on the end case
                if level.structure[mac.case_y][mac.case_x] == 'e':  # leave the game

                    # displays possessed objects
                    for item in quest_item_list:
                        print(item)

                    # displays result message
                    while mc_gyver_score in [0, 1, 2, 3]:  # Allow to verify than mc_gyver exist
                        print(mc_gyver_score)
                        level.end_game(mc_gyver_score, window)

                        for event in pygame.event.get():  # allows leave image result

                            if event.type == KEYDOWN:
                                carry_on_game = 0  # comeback in home loop
                                mc_gyver_score = None
