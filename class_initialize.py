import pygame

from class_level import Level
from constantes import WINDOW_SIDE, ICONE_IMAGE, WINDOW_TITLE, BACKGROUND_IMAGE


class Initializer:
    """ Initializer for game using pygame ! """
    # def __init__(self):
    #     """ init my object """
    #     pass

    @staticmethod
    def initialize_window():
        """ initialize window with pygame function """
        # Open window Pygame
        window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
        # Icone
        icone = pygame.image.load(ICONE_IMAGE)
        pygame.display.set_icon(icone)
        # Title
        pygame.display.set_caption(WINDOW_TITLE)
        return window

    @staticmethod
    def init_level(choice, window):
        """ initialize the map with the player choice """
        # Generate a choice from a FILE
        level = Level(choice)
        level.generate()
        level.random_obj()
        level.display(window)
        return level

    @staticmethod
    def loading_home_page(image, window):
        """ load the homepage """
        home = pygame.image.load(image).convert()
        window.blit(home, (0, 0))

    @staticmethod
    def initialize_background():
        """ initialise the background of map game """
        background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()  # Loading background
        return background

    @staticmethod
    def display_new_position(background, level, character, window):
        """ display new position of character """
        # Displays at new positions
        window.blit(background, (0, 0))  # Reload background with good position
        level.display(window)  # Reload the element of the map at the good position
        # Reload character at the good position in the map
        window.blit(character.direction, (character.x_pixels, character.y_pixels))
        pygame.display.flip()  # Update the "surface"
