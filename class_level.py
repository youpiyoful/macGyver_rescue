# -*- coding: Utf-8 -*
"""Classes of game Mc-gyver"""
import random
import pygame

from constantes import LOST
from constantes import WIN
from constantes import ARRIVAL_IMAGE
from constantes import ETHER
from constantes import NEEDLE
from constantes import SPRITE_SIZE
from constantes import START_IMAGE
from constantes import TUBE
from constantes import WALL_IMAGE


class Level:
    """Class for create level"""

    def __init__(self, file):
        self.file = file
        self.structure = 0

    @staticmethod
    def end_game(character, window):
        """ verify the score for return win or lose """
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

    def generate(self):
        """Method for generate level by file.
        We create a general list, who contain a list by line to display"""
        # we open file
        with open(self.file, "r") as file:
            structure_level = []
            # we rune line of file
            for line in file:
                line_level = []
                # we run sprites (letters) contain in file
                for sprite in line:
                    # we ignore the "\n" of end line
                    if sprite != '\n':
                        # we add the sprite at line of level
                        line_level.append(sprite)
                # we add the line at structure level
                structure_level.append(line_level)
            # we save structure
            self.structure = structure_level

    def random_obj(self):
        """ generate random object at unique place on the map"""
        objects = ['E', 'T', 'N']  # init list of objects
        for obj in objects:  # instruction for each object
            x_line = 0  # init value
            y_case = 0  # init value
            self.structure[x_line][y_case] = None  # init != 0 for allow to enter in loop
            while self.structure[x_line][y_case] != '0':
                line = random.randint(0, 14)
                case = random.randint(0, 14)
                x_line = line
                y_case = case
            self.structure[x_line][y_case] = obj

    def display(self, window):
        """Method for display level by list of structure output by generate()"""
        # Loading images
        wall = pygame.image.load(WALL_IMAGE).convert()
        start = pygame.image.load(START_IMAGE).convert()
        end = pygame.image.load(ARRIVAL_IMAGE).convert_alpha()
        tube = pygame.image.load(TUBE).convert_alpha()
        needle = pygame.image.load(NEEDLE).convert_alpha()
        ether = pygame.image.load(ETHER).convert_alpha()

        # we run the level's list
        num_line = 0

        for line in self.structure:
            # we run list of lines
            num_case = 0

            for sprite in line:
                # we calcul the real position in pixels
                x_case = num_case * SPRITE_SIZE
                y_case = num_line * SPRITE_SIZE

                if sprite == 'w':  # m = wall
                    window.blit(wall, (x_case, y_case))

                elif sprite == 's':  # s = start
                    window.blit(start, (x_case, y_case))

                elif sprite == 'e':  # e = end
                    window.blit(end, (x_case, y_case))

                elif sprite == 'E':
                    window.blit(ether, (x_case, y_case))

                elif sprite == 'N':
                    window.blit(needle, (x_case, y_case))

                elif sprite == 'T':
                    window.blit(tube, (x_case, y_case))
                num_case += 1
            num_line += 1
