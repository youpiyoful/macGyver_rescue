"""
@desc only contain Constants Classe
"""


class Config():
    """
    Contain all the constants variables
    """
    SPRITES_NUMBER = 20*19
    SPRITE_SIZE = 30
    FILE = "map.txt"
    ITEMS = [{"item": "NEEDLE", "image": "images/needle.png", "map": "N"},
             {"item": "ETHER", "image": "images/ether.png", "map": "E"},
             {"item": "TUBE", "image": "images/tube.png", "map": "T"}]
    CHARACTER = "images/mcgyver.png"
    GUARD = "images/guard.png"
    WALL = "images/wall.png"
    FLOOR = "images/floor2.png"
    SYRINGE = "images/syringe.png"
    HOME = "images/mcgyver_home.png"
    WIN = "images/WIN.jpg"
    LOSE = "images/LOSE.jpg"
