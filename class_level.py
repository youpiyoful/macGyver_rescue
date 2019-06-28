# -*- coding: Utf-8 -*
"""Classes of game Mc-gyver"""
import pygame
import random

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
		objects = ['E', 'T', 'N']  # init list of objects
		for obj in objects:  # instruction for each object
			x = 0  # init value
			y = 0  # init value
			self.structure[x][y] = None  # init != 0 for allow to enter in loop
			while self.structure[x][y] != '0':
				line = random.randint(0, 14)
				case = random.randint(0, 14)
				x = line  # TODO faire en sorte que les objets n'apparaissent pas au même endroit
				y = case
			self.structure[x][y] = obj

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
				x = num_case * SPRITE_SIZE
				y = num_line * SPRITE_SIZE

				if sprite == 'w':  # m = wall
					window.blit(wall, (x, y))

				elif sprite == 's':  # s = start
					window.blit(start, (x, y))

				elif sprite == 'e':  # e = end
					window.blit(end, (x, y))

				elif sprite == 'E':
					window.blit(ether, (x, y))

				elif sprite == 'N':
					window.blit(needle, (x, y))

				elif sprite == 'T':
					window.blit(tube, (x, y))
				num_case += 1
			num_line += 1