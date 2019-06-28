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
		self.x = 0
		self.y = 0
		# Direction by default
		self.direction = self.right
		# Level where your character is
		self.level = level

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
					self.x = self.case_x * SPRITE_SIZE

			# Image in the good direction
			self.direction = self.right
		
		# Moove left
		if direction == 'left':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x - 1] != 'w':
					self.case_x -= 1
					self.x = self.case_x * SPRITE_SIZE
			self.direction = self.left
		
		# Moove up
		if direction == 'up':
			if self.case_y > 0:
				if self.level.structure[self.case_y - 1][self.case_x] != 'w':
					self.case_y -= 1
					self.y = self.case_y * SPRITE_SIZE
			self.direction = self.up
		
		# Moove down
		if direction == 'down':
			if self.case_y < (NUMBER_SIDE_SPRITE - 1):
				if self.level.structure[self.case_y + 1][self.case_x] != 'w':
					self.case_y += 1
					self.y = self.case_y * SPRITE_SIZE
			self.direction = self.down


