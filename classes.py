"""Classes du jeu MC Gyver Rescue"""

import pygame
from pygame.locals import *
from config import *

class Level:
	"""Class for create level"""
	def __init__(self, file):
		self.FILE = fichier
		self.structure = 0


	def generate(self):
		"""Method for generate level by file.
		We create a general list, who contain a list by line to display"""
		#we open the file
		with open(self.file, "r") as file:
			level_structure = []
			#we run each line of file
			for line in file:
				level_line = []
				#we run the sprites (letters) contain by the file
				for sprite in line:
					#we escape \n
					if sprite != '\n':
						#we add the sprite at list of the line
						level_line.append(sprite)
				#we add the line to list of level
				level_structure.append(level_line)
			#we save this structure
			self.structure = level_structure


	def display(self, window):
		"""Méthod for display level by list of structure output by generate()"""
		#Loading images
		wall = pygame.image.load(WALL).convert()
		# start = pygame.image.load(image_depart).convert()
		# arrivee = pygame.image.load(image_arrivee).convert_alpha()

		#we run the list of level
		line_num = 0
		for line in self.structure:
			#we run the listes of lines
			case_num = 0
			for sprite in line:
				#we calcul real position in pixels
				x = case_num * SPRITE_SIZE
				y = line_num * SPRITE_SIZE
				if sprite == 'w':		   #w = Wall
					fenetre.blit(wall, (x,y))
				elif sprite == 's':		   #s = Start
					fenetre.blit(start, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				case_num += 1
			line_num += 1




class Perso:
	"""Class for create character"""
	def __init__(self, character, level):
		#Sprites of character
		self.character = pygame.image.load(CHARACTER).convert_alpha()

		#Position of character in cases and in pixels
		self.sprite_x = 0
		self.sprite_y = 0
		self.x = 0
		self.y = 0

		#level dans lequel le personnage se trouve
		self.level = level


	def moove(self, direction):
		"""Method for moove the character"""

		#Moove right
		if direction == 'right':
			#For dont out of screen
			if self.sprite_x < (number_sprites_side - 1):
				#We verify than case is not a wall
				if self.level.structure[self.sprite_y][self.sprite_x+1] != 'w':
					#Moove 1 case
					self.sprite_x += 1
					#Calcul of position "real" in pixel
					self.x = self.sprite_x * SPRITE_SIZE

		#Moove left
		if direction == 'left':
			if self.sprite_x > 0:
				if self.level.structure[self.sprite_y][self.sprite_x-1] != 'w':
					self.sprite_x -= 1
					self.x = self.sprite_x * SPRITE_SIZE
			# self.direction = self.left

		#Moove up
		if direction == 'up':
			if self.sprite_y > 0:
				if self.level.structure[self.sprite_y-1][self.sprite_x] != 'w':
					self.sprite_y -= 1
					self.y = self.sprite_y * SPRITE_SIZE
			# self.direction = self.up

		#Moove down
		if direction == 'down':
			if self.sprite_y < (nombre_sprite_cote - 1):
				if self.level.structure[self.sprite_y+1][self.sprite_x] != 'w':
					self.sprite_y += 1
					self.y = self.sprite_y * SPRITE_SIZE
			# self.direction = self.down
