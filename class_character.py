# -*- coding: Utf-8 -*
"""Classes of game Mc-gyver"""
import pygame

from constantes import NUMBER_SIDE_SPRITE
from constantes import SPRITE_SIZE


class Character:
    """Class for create character"""
    def __init__(self, image_character, level):
        # Sprites of character
        self.right = pygame.image.load(image_character).convert_alpha()
        self.left = pygame.image.load(image_character).convert_alpha()
        self.up = pygame.image.load(image_character).convert_alpha()
        self.down = pygame.image.load(image_character).convert_alpha()
        # Position of character in cases and in pixels
        self.case_x = 0
        self.case_y = 0
        self.x_pixels = 0
        self.y_pixels = 0
        # Direction by default
        self.direction = self.right
        # Level where your character is
        self.level = level

    @staticmethod
    def stock_quest_item(position, quest_item_list):
        """ record list of taken object """

        if position == 'N' and 'N' not in quest_item_list:
            quest_item_list.append('N')

        elif position == 'T' and 'T' not in quest_item_list:
            quest_item_list.append('T')

        elif position == 'E' and 'E' not in quest_item_list:
            quest_item_list.append('E')

        return quest_item_list

    @staticmethod
    def score_meter(position, score, quest_item_list):
        """
            add + 1 to variable score when the position
            of character is on an object
        """
        if position == 'N' and 'N' not in quest_item_list:
            score += 1

        elif position == 'T' and 'T' not in quest_item_list:
            score += 1

        elif position == 'E' and 'E' not in quest_item_list:
            score += 1

        return score

    def moove(self, direction):

        """Method for moove character"""
        # Moove right

        if direction == 'right':

            # For don t out of screen
            if self.case_x < (NUMBER_SIDE_SPRITE - 1):

                # We verify than the case of destination is not a wall
                if self.level.structure[self.case_y][self.case_x + 1] != 'w':

                    # Moove 1 case
                    self.case_x += 1

                    # Calcul of position "real" in pixel
                    self.x_pixels = self.case_x * SPRITE_SIZE

            # Image in the good direction
            self.direction = self.right
        # Moove left

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'w':
                    self.case_x -= 1
                    self.x_pixels = self.case_x * SPRITE_SIZE
            self.direction = self.left
        # Moove up

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'w':
                    self.case_y -= 1
                    self.y_pixels = self.case_y * SPRITE_SIZE
            self.direction = self.up
        # Moove down

        if direction == 'down':
            if self.case_y < (NUMBER_SIDE_SPRITE - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'w':
                    self.case_y += 1
                    self.y_pixels = self.case_y * SPRITE_SIZE
            self.direction = self.down
