import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		"""
		initializes the player and makes it a rectangle
		args: x(int)
			y(int)
		return: none
		"""

		pygame.mixer.init()

		#initializes it as a sprite
		pygame.sprite.Sprite.__init__(self)

		#initializes width and height
		self.width = 200
		self.height = 100

		#sets up the player's appearance
		self.image = pygame.image.load('pics/player.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		#makes the player a rectangle
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		#initializes the player's speed
		self.speed = 40


	def redrawGetToClass(self, deskList, screen):
		#Setting up and Displaying Background
		self.background = pygame.Surface(screen.get_size()).convert()
		self.background = pygame.image.load('pics/bg1.png').convert_alpha()
		self.background = pygame.transform.scale(self.background, (2000, 2000))
		screen.blit(self.background, (0, 0))

		#Setting Up the Directions
		self.red = (255, 0, 0)
		self.white = (255, 255, 255)
		self.title = pygame.font.SysFont("Times New Roman", 80)
		self.title_text = self.title.render('Get to Class!!!', False, self.red)
		self.directions = pygame.font.SysFont("Times New Roman", 50)
		self.directions_text = self.directions.render("Directions: Avoid the Desks and Get to the Other Side Before Time Runs out!!", False, self.red)
		self.directions2 = pygame.font.SysFont("Times New Roman", 50)
		self.directions2_text = self.directions2.render("Use the Arrow Keys to Move!", False, self.red)

		#Displaying the Directions
		screen.blit(self.title_text, (800, 0))
		screen.blit(self.directions_text, (175, 1895))
		screen.blit(self.directions2_text, (750, 1935))

		deskList.draw(screen)
		pygame.display.flip()


	def moveUp(self):
		"""
		moves the player upwards
		args: none
		return: N/A
		"""
		self.rect.y -= self.speed
		self.rect.move(self.rect.x, self.rect.y)
	

	def moveDown(self):
		"""
		moves the player downwards
		args: none
		return: N/A
		"""
		self.rect.y += self.speed
		self.rect.move(self.rect.x, self.rect.y)


	def moveLeft(self):
		"""
		moves the player to the left
		args: none
		return: N/A
		"""
		self.rect.x -= self.speed
		self.rect.move(self.rect.x, self.rect.y)
	

	def moveRight(self):
		"""
		moves the player to the right
		args: none
		return: N/A
		"""
		self.rect.x += self.speed
		self.rect.move(self.rect.x, self.rect.y)


	def pencilCollide(self, playerList, pencilList):
		"""
		detects if the pencil collides with the player
		args: playerList(sprite group)
		pencilList(sprite group)
		return: True or False
		"""
		if(self.rect.collidelist(list(pencilList)) != -1):
			return True
		return False


	def deskCollide(self, playerList, deskList):
		"""
		detects if the desk collides with the player
		args: playerList(sprite group)
		deskList(sprite group)
		return: True or False
		"""
		if(self.rect.collidelist(list(deskList)) != -1):
			return True
		return False


	def isWinner(self):
		"""
		detects if the the player has won the game 
		args: none
		return: True or False
		"""
		if(self.rect.y <= 50):
			return True
		return False


	def lateText(self, screen):
		"""
		shows text that signifies that the player has lost
		args: screen(Display)
		return: N/A
		"""
		screen.fill((255, 0, 0))
		self.times_up = pygame.font.SysFont("Times New Roman", 200)
		self.times_up_text = self.times_up.render("You're Late!", True, (255,255,255))
		screen.blit(self.times_up_text, (570, 900))

		self.getPass = pygame.font.SysFont("Times New Roman", 170)
		self.getPass_text = self.times_up.render("Get a Pass", True, (255,255,255))
		screen.blit(self.getPass_text, (600, 1100))
		pygame.display.update()


	def madeIt(self, screen):
		"""
		shows text that signifies that the player has won
		args: screen(Display)
		return: N/A
		"""
		screen.fill((0, 255, 0))
		self.madeIt = pygame.font.SysFont("Times New Roman", 200)
		self.madeIt_text = self.madeIt.render("You Made It!", True, self.white)
		screen.blit(self.madeIt_text, (500, 900))
		pygame.display.update()
