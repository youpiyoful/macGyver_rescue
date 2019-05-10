# -*- coding: Utf-8 -*
"""Classes of game Mc-gyver"""

import pygame
from pygame.locals import *
from random import *

from constantes import *

class Level:
	"""Class for create level"""
	def __init__(self, file):
		self.file = file
		self.structure = 0
	
	
	def generate(self):
		"""Method for generate level by file.
		We create a general list, who contain a list by line to display"""
		#we open file
		with open(self.file, "r") as file:
			structure_level = []
			#we rune line of file
			for line in file:
				line_level = []
				#we run sprites (letters) contain in file
				for sprite in line:
					#we ignore the "\n" of end line
					if sprite != '\n':
						#we add the sprite at line of level
						line_level.append(sprite)
				#we add the line at structure level
				structure_level.append(line_level)
			#we save structure 
			self.structure = structure_level
	
	
	def display(self, window):
		"""Méthod for display level by list of structure output by generate()"""
		#Loading images
		wall = pygame.image.load(WALL_IMAGE).convert()
		start = pygame.image.load(START_IMAGE).convert()
		end = pygame.image.load(ARRIVAL_IMAGE).convert_alpha()

		
		#we run the level's list
		num_line = 0
		for line in self.structure:
			#we run list of lines
			num_case = 0
			for sprite in line:
				#we calcul the real position in pixels
				x = num_case * SPRITE_SIZE
				y = num_line * SPRITE_SIZE
				if sprite == 'w':		   #m = wall
					window.blit(wall, (x,y))
				elif sprite == 's':		   #s = start
					window.blit(start, (x,y))
				elif sprite == 'e':		   #e = end
					window.blit(end, (x,y))
				num_case += 1
			num_line += 1
			
	def init_object_place():
		""" Method for display object randomly in the map """ 
		#Loading image
		ether = pygame.image.load(ETHER).convert()
		tube = pygame.image.load(TUBE).convert()
		xxxx = pygame.image.load().convert()
		
		#we run the level's list
		num_line = 0
		for line in self.structure:
			#we run list of lines
			num_case = 0
			for sprite in line:
				#we calcul the real position in pixels
				x = num_case * SPRITE_SIZE
				y = num_line * SPRITE_SIZE
				if sprite == '0':		   #0 = empty case
					 = uniform(12, 18)
				elif sprite == 's':		   #s = start
					window.blit(start, (x,y))
				elif sprite == 'e':		   #e = end
					window.blit(end, (x,y))
				num_case += 1
			num_line += 1
			
			
class Character:
	"""Class for create character"""
	def __init__(self, character, level):
		#Sprites of character
		self.right = pygame.image.load(character).convert_alpha()
		self.left = pygame.image.load(character).convert_alpha()
		self.up = pygame.image.load(character).convert_alpha()
		self.down = pygame.image.load(character).convert_alpha()
		#Position of character in cases and in pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction by default
		self.direction = self.right
		#Level where your character is 
		self.level = level
	
	
	def moove(self, direction):
		"""Method for moove character"""
		
		#Moove right
		if direction == 'right':
			#For don t out of screen
			if self.case_x < (NUMBER_SIDE_SPRITE - 1):
				#We verify than the case of destination is not a wall
				if self.level.structure[self.case_y][self.case_x+1] != 'w':
					#Moove 1 case
					self.case_x += 1
					#Calcul of position "real" in pixel
					self.x = self.case_x * SPRITE_SIZE
			#Image in the good direction
			self.direction = self.right
		
		#Moove left
		if direction == 'left':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'w':
					self.case_x -= 1
					self.x = self.case_x * SPRITE_SIZE
			self.direction = self.left
		
		#Moove up
		if direction == 'up':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'w':
					self.case_y -= 1
					self.y = self.case_y * SPRITE_SIZE
			self.direction = self.up
		
		#Moove down
		if direction == 'down':
			if self.case_y < (NUMBER_SIDE_SPRITE - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'w':
					self.case_y += 1
					self.y = self.case_y * SPRITE_SIZE
			self.direction = self.down
