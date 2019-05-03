#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Level:
	"""Class for create level"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generate(self):
		"""Method for generate level by file.
		We create a general list, who contain a list by line to display"""
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_level = []
			#On parcourt les lines du fichier
			for line in fichier:
				line_level = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in line:
					#On ignore les "\n" de fin de line
					if sprite != '\n':
						#On ajoute le sprite à la liste de la line
						line_level.append(sprite)
				#On ajoute la line à la liste du level
				structure_level.append(line_level)
			#On sauvegarde cette structure
			self.structure = structure_level
	
	
	def display(self, window):
		"""Méthod for display level by list of structure output by generate()"""
		#Loading images
		wall = pygame.image.load(WALL_IMAGE).convert()
		depart = pygame.image.load(START_IMAGE).convert()
		arrivee = pygame.image.load(ARRIVAL_IMAGE).convert_alpha()
		
		#On parcourt la liste du level
		num_line = 0
		for line in self.structure:
			#On parcourt les listes de lines
			num_case = 0
			for sprite in line:
				#On calcule la position réelle en pixels
				x = num_case * SPRITE_SIZE
				y = num_line * SPRITE_SIZE
				if sprite == 'm':		   #m = wall
					window.blit(wall, (x,y))
				elif sprite == 'd':		   #d = Départ
					window.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					window.blit(arrivee, (x,y))
				num_case += 1
			num_line += 1
			
			
			
			
class Character:
	"""Classe permettant de créer un character"""
	def __init__(self, character, level):
		#Sprites du character
		self.right = pygame.image.load(character).convert_alpha()
		self.left = pygame.image.load(character).convert_alpha()
		self.up = pygame.image.load(character).convert_alpha()
		self.down = pygame.image.load(character).convert_alpha()
		#Position du character en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.right
		#Level dans lequel le character se trouve 
		self.level = level
	
	
	def moove(self, direction):
		"""Methode permettant de déplacer le character"""
		
		#Déplacement vers la right
		if direction == 'right':
			#Pour ne pas dépasser l'écran
			if self.case_x < (NUMBER_SIDE_SPRITE - 1):
				#On vérifie que la case de destination n'est pas un wall
				if self.level.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * SPRITE_SIZE
			#Image dans la bonne direction
			self.direction = self.right
		
		#Déplacement vers la left
		if direction == 'left':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * SPRITE_SIZE
			self.direction = self.left
		
		#Déplacement vers le up
		if direction == 'up':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * SPRITE_SIZE
			self.direction = self.up
		
		#Déplacement vers le down
		if direction == 'down':
			if self.case_y < (NUMBER_SIDE_SPRITE - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * SPRITE_SIZE
			self.direction = self.down
