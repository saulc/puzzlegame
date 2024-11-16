
import pygame, sys

from part import part, board


class game:


	width = 800
	height = 800
	fullscreen = True	
	surface = None 

	bg = None 


	def __init__(self):
		pygame.init()

		bg = pygame.image.load("./android.png").convert()  
		if Game.fullscreen:
			Game.width = pygame.display.Info().current_w
			Game.height = pygame.display.Info().current_h

		Game.surface = pygame.display.set_mode([Game.width, Game.height])
		pygame.display.set_caption('Puzzle solver')

		self.start()

	def printText(self, text, size=45):
		white = pygame.Color(255, 255, 255)
		f = pygame.font.get_default_font()
		myfont = pygame.font.SysFont(f, size, True , False)
		label = myfont.render(text, True, white)
		Game.surface.blit(label, (Game.width//3, Game.height//3))


	def start(self):
		white = pygame.Color(255, 255, 255)
		black = pygame.Color(0, 0, 0)

		#set the FPS for this game
		FPS = 30 #30 frames per second
		fpsClock = pygame.time.Clock()

		pygame.font.init()
		f = pygame.font.get_default_font()
		myfont = pygame.font.SysFont(f, 35, True , False)

		while True:
			# Game.surface.fill(black)
			Game.surface.blit(game.bg, [0, 0])
			self.printText("Name goes here", size=100)
			label = myfont.render('testing', True, white)
			Game.surface.blit(label, (100, 10))

			pygame.display.update()
			fpsClock.tick(FPS)