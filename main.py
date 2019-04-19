from classes.game import Game


def main():
    """
    Main Method, just launches the Game class who drive the whole programm
    """
    game = Game()
    game.play()


if __name__ == "__main__":
	main()

# import pygame
# from pygame.locals import *
#
# pygame.init()
#
#
#
# # class Map:
# # 	def openWindow(self, large, long):
# # 		self.window = pygame.display.set_mode((large, long))
# # 	def loadBackground(self, backgroundImage):
# # 		self.background = pygame.image.load(backgroundImage).convert()
# # 	def stickBackground(self, background):
#
# #Open window Pygame
# window = pygame.display.set_mode((640, 480))
#
# #Load background
# background = pygame.image.load("background.jpg").convert()
# window.blit(background, (0,0))
#
# #Load perso
# perso = pygame.image.load("perso.png").convert_alpha()
# position_perso = perso.get_rect()
# window.blit(perso, position_perso)
#
# #Screen refresh
# def screenRefresh():
# 	pygame.display.flip()
#
# #Infinite loop
# continuer = 1
# while continuer:
# 	for event in pygame.event.get():	#Attente des événements
# 		if event.type == QUIT:
# 			continuer = 0
# 		if event.type == KEYDOWN:
# 			# pygame.key.set_repeat(400, 30)
# 			if event.key == K_DOWN:	#Si "flèche bas"
# 				#On descend le perso
# 				position_perso = position_perso.move(0,3)
# 				# pygame.key.set_repeat(400, 30) pour répéter l'action quand la touche reste enfoncé.
# 			if event.key == K_UP:
# 				position_perso = position_perso.move(0,-3)
# 			if event.key == K_LEFT:
# 				position_perso = position_perso.move(-3,0)
# 			if event.key == K_RIGHT:
# 				position_perso = position_perso.move(3,0)
#
# 	#Re-sticking
# 	window.blit(background, (0,0))
# 	window.blit(perso, position_perso)
# 	#Refresh
# 	pygame.display.flip()
