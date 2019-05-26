import pygame
import random

class Desk(pygame.sprite.Sprite):

	def __init__(self, screen):
		"""
		initializes the screen and desk, makes the desk a rectangle and puts the desks on the screen
		args: screen(display)
		return: N/A
		"""
                #initializes sprite group
		pygame.sprite.Sprite.__init__(self)

                #initializes screen
		self.screen = screen

                #initializes the desk
		self.image = pygame.image.load('pics/desk.png').convert_alpha()

                #makes the desks different sizes
		self.width = random.randint(100, 400)
		self.height = self.width
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

                #makes the desk a rectangle
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(300, 1700)
		self.rect.y = random.randint(200, 1100)

	        #puts the desks on the screen
		self.screen.blit(self.image, (self.rect.x, self.rect.y))
		pygame.display.update()

