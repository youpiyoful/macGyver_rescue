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
		mur = pygame.image.load(WALL).convert()
		# depart = pygame.image.load(image_depart).convert()
		# arrivee = pygame.image.load(image_arrivee).convert_alpha()

		#we run the list of level
		line_num = 0
		for line in self.structure:
			#we run the listes of lines
			case_num = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1




class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve
		self.niveau = niveau


	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""

		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite

		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche

		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut

		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas
