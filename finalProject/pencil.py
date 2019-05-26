import pygame
import random

class Pencil(pygame.sprite.Sprite):

	def __init__(self, screen):
		"""
		initializes the screen and pencil and makes the pencil a rectangle
		args: screen(display)
		return: N/A
		"""
                #initializes the sprites
		pygame.sprite.Sprite.__init__(self)
		
                #initializes the screen
		self.screen = screen

                #loads pencil image
		self.image = pygame.image.load('pics/pencil.png').convert_alpha()

                #makes pencil different sizes
		self.width = random.randint(60, 200)
		self.height = self.width + 100

                #transforms pencil, makes it into a rect, and puts the pencil on the screen
		self.image = pygame.transform.scale(self.image, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0, 2000)
		self.rect.y = 0 #top of screen
		self.screen.blit(self.image, (self.rect.x, self.rect.y))
		pygame.display.update()
		
                #initializes the speed
		self.speed = 5
	
	#this will make every subsequent pencil created move more quickly, making the game more challenging
	def incSpeed(self):
		"""
		increases the speed of the pencil, making the game more difficult
		args: none
		return: N/A
		"""
		self.speed += 5

	#moves the pencil
	def update(self):
		"""
		moves the pencil
		args: none
		return: N/A
		"""
		self.rect.y += self.speed

	
