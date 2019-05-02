"""
@desc    Only contain Class Display, see the description below
"""
import pygame
from pygame.locals import *
from config import Config

class Display:
    """
    Pygame Display management
    """
    pygame.init()

    def __init__(self):
        self.level_structure = []
        self.height = Config.SPRITES_NUMBER * Config.SPRITE_SIZE
        self.width = (Config.SPRITES_NUMBER + 1) * Config.SPRITE_SIZE

    @property
    def window_generation(self):
        """
        Window Generation
        """
        pygame.display.set_caption("McGyver Rescue !")
        return pygame.display.set_mode((self.height, self.width))

    @staticmethod
    def display_game(location, window):
        """
        Start/End display Management according to the state of the game
        """
        if location == "home":
            image = pygame.image.load(Config.HOME).convert()
            pygame.display.update(window.fill(0))  # displaying home screen
            window.blit(image, (0, 0))  # displaying home screen
            pygame.display.flip()  # window refreshing
        elif location == "win":
            image = pygame.image.load(Config.WIN).convert()
            window.blit(image, (0, 0))  # displaying home screen
            pygame.display.flip()  # window refreshing
        elif location == "lose":
            image = pygame.image.load(Config.LOSE).convert()
            window.blit(image, (0, 0))  # displaying home screen
            pygame.display.flip()  # window refreshing

    @staticmethod
    def display_level(level, character, window):
        """
        Display all the Game images from the structure level
            and character position
        @param  object  level       Contain level object
        @param  object  characters  Contain character object
        @param  object  window      Contain the pygame window
        """
        line_number = 0
        for line in level.get_map_structure:
            case_number = 0
            for sprite in line:
                x = case_number * Config.SPRITE_SIZE
                y = line_number * Config.SPRITE_SIZE
                if sprite == "0":
                    window.blit(pygame.image.load(Config.WALL).convert(),
                                (x, y))
                elif sprite == "N":
                    window.blit(pygame.image.load(Config.FLOOR).convert(),
                                (x, y))
                    if "NEEDLE" not in character.character_items:
                        window.blit(
                            pygame.image.load(
                                Config.ITEMS[0]['image'])
                            .convert(), (x, y))
                    else:
                        window.blit(
                            pygame.image.load(
                                Config.ITEMS[0]['image'])
                            .convert(), (0, 450))
                elif sprite == "E":
                    window.blit(pygame.image.load(Config.FLOOR).convert(),
                                (x, y))
                    if "ETHER" not in character.character_items:
                        window.blit(
                            pygame.image.load(
                                Config.ITEMS[1]['image'])
                            .convert(), (x, y))
                    else:
                        window.blit(
                            pygame.image.load(
                                Config.ITEMS[1]['image'])
                            .convert(), (30, 450))
                elif sprite == "T":
                    window.blit(pygame.image.load(Config.FLOOR).convert(),
                                (x, y))
                    if "TUBE" not in character.character_items:
                        window.blit(
                            pygame.image.load(
                                Config.ITEMS[2]['image'])
                            .convert(), (x, y))
                    else:
                        window.blit(
                            pygame.image.load(
                                Config.ITEMS[2]['image'])
                            .convert(), (60, 450))
                elif sprite in ("C", "1"):
                    window.blit(pygame.image.load(Config.FLOOR).convert(),
                                (x, y))
                elif sprite == "G":
                    window.blit(pygame.image.load(Config.FLOOR).convert(),
                                (x, y))
                    window.blit(pygame.image.load(Config.GUARD).convert(),
                                (x, y))
                case_number += 1
            line_number += 1

            window.blit(pygame.image.load(Config.CHARACTER).convert(),
                        (character.character_position[0]
                         * Config.SPRITE_SIZE,
                         character.character_position[1]
                         * Config.SPRITE_SIZE))

            pygame.display.flip()
