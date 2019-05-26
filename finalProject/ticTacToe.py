import pygame
import random

class TicTacToe(pygame.sprite.Sprite):
        def __init__(self, width = 2000, height = 2000):
                """
                initializes the background, text and game board
                args: width(int)
                      height(int)
                return: none
                """
                #initializes sprite group
                pygame.sprite.Sprite.__init__(self)

                #initializes pygame, sound and text
                pygame.init()
                pygame.mixer.init()
                pygame.font.init()
                
                #set up the screen
                self.width = width
                self.height = height
                self.screen = pygame.display.set_mode((self.width, self.height))

                #initializes the backgound image, board image, x image and o image
                self.background = pygame.Surface(self.screen.get_size()).convert()
                self.board = pygame.image.load('pics/board.jpg').convert_alpha()
                self.board = pygame.transform.scale(self.board, (2000, 2000))
                self.x = pygame.image.load('pics/x3.png').convert_alpha()
                self.x = pygame.transform.scale(self.x, (500, 500))
                self.o = pygame.image.load('pics/o.png').convert_alpha()
                self.o = pygame.transform.scale(self.o, (500, 500))

                #sets up text 
                self.white = (255, 255, 255)
                self.red = (255, 0, 0)
                self.green = (0, 255, 0)
                self.blue = (0, 0, 255)
                self.quiz = pygame.font.SysFont("Times New Roman", 80)
                self.quiz_text = self.quiz.render('Quiz Time', False, self.white)
                self.directions = pygame.font.SysFont("Times New Roman", 50)
                self.directions_text = self.directions.render("Directions: The tic-tac-toe board corresponds to your number key pad, i.e.: 7 = the top left box", False, self.white)
                self.won = pygame.font.SysFont("Arial", 200)
                self.won_text = self.won.render('You Passed!', False, self.green)
                self.lost = pygame.font.SysFont("Arial", 200)
                self.lost_text = self.lost.render('You Failed', False, self.red)
                self.tie = pygame.font.SysFont("Arial", 145)
                self.tie_text = self.tie.render("You tied with the teacher!", False, self.blue)

                #initializes the board array
                self.spaces = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        def board(self):
                """
                puts the board and text on the screen
                args: none
                return: N/A
                """
                self.screen.blit(self.board, (0, 0))
                self.screen.blit(self.quiz_text, (800, 0))
                self.screen.blit(self.directions_text, (50, 75))
                pygame.display.flip()
        
        
        
        def isBoardFilled(self):
                """
                checks if the board is filled
                args: none
                return: true or false
                """
                if(self.spaces[0][0] != 0 and self.spaces[0][1] != 0 and self.spaces[0][2] != 0 and self.spaces[1][0] != 0 and self.spaces[1][1] != 0 and self.spaces[1][2] != 0 and self.spaces[2][0] != 0 and self.spaces[2][1] != 0 and self.spaces[2][2] != 0):
                        return True
                
                return False
    
        def pTurn(self, choice):
                """
                moves the x for the player based on the input put in by the player
                args: choice(input)
                return: true
                """
                if(choice == pygame.K_KP7):
                        if(self.isSpotFilled(0,0) == False):
                                self.spaces[0][0] = 1
                                self.screen.blit(self.x, (100, 200))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP8):
                        if(self.isSpotFilled(0,1) == False):
                                self.spaces[0][1] = 1
                                self.screen.blit(self.x, (800, 200))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP9):
                        if(self.isSpotFilled(0,2) == False):
                                self.spaces[0][2] = 1
                                self.screen.blit(self.x, (1400, 200))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP4):
                        if(self.isSpotFilled(1,0) == False):
                                self.spaces[1][0] = 1
                                self.screen.blit(self.x, (100, 800))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP5):
                        if(self.isSpotFilled(1,1) == False):
                                self.spaces[1][1] = 1
                                self.screen.blit(self.x, (800, 800))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP6):
                        if(self.isSpotFilled(1,2) == False):
                                self.spaces[1][2] = 1
                                self.screen.blit(self.x, (1400, 800))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP1):
                        if(self.isSpotFilled(2,0) == False):
                                self.spaces[2][0] = 1
                                self.screen.blit(self.x, (100, 1400))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP2):
                        if(self.isSpotFilled(2,1) == False):
                                self.spaces[2][1] = 1
                                self.screen.blit(self.x, (800, 1400))
                                pygame.display.update()
                                        
                if(choice == pygame.K_KP3):
                        if(self.isSpotFilled(2,2) == False):
                                self.spaces[2][2] = 1
                                self.screen.blit(self.x, (1400, 1400))
                                pygame.display.update()
                return True

        def isSpotFilled(self, x, y):
                """
                checks if a space is filled yet
                args: x(int)
                      y(int)
                return: true or false
                """
                if(self.spaces[x][y] != 0):
                        return True
                else:
                        return False                                       
        
        def compTurn(self):
                """
                randomly takes the computer place a piece in an open spot
                args: none
                return: N/A
                """
                while(True):
                        spot1 = random.randint(0,2)
                        spot2 = random.randint(0,2)
                        if(self.isSpotFilled(spot1, spot2) == False):
                                self.spaces[spot1][spot2] = 2
                                onscreen1 = (spot2 * 700) + 100
                                onscreen2 = (spot1 * 700) + 100
                                self.screen.blit(self.o, (onscreen1, onscreen2))
                                pygame.display.update()
                                break

        def showPWinText(self):
                """
                puts the text on the screen and runs sound
                args: none
                return: N/A
                """
                self.screen.blit(self.won_text, (500, 900))
                pygame.display.update()
                clap = pygame.mixer.Sound('fx/app.wav')
                clap.play()

        def showCWinText(self):
                """
                puts the text on the screen and runs sound
                args: none
                return: N/A
                """
                self.screen.blit(self.lost_text, (550, 900))
                pygame.display.update()
                boo = pygame.mixer.Sound('fx/boo.wav')
                boo.play()

        def showTieText(self):
                """
                puts the tie text on the screen
                args: none
                return: N/A
                """
                self.screen.blit(self.tie_text, (200, 900))
                pygame.display.update()

        def isWinner(self):
                """
                checks if anyone has won
                args: none
                return: true or false
                """
                if(self.spaces[0][0] == self.spaces[0][1] == self.spaces[0][2] == 1 or self.spaces[1][0] == self.spaces[1][1] == self.spaces[1][2] == 1 or self.spaces[2][0] == self.spaces[2][1] == self.spaces[2][2] == 1 or self.spaces[0][0] == self.spaces[1][0] == self.spaces[2][0] == 1 or self.spaces[0][1] == self.spaces[1][1] == self.spaces[2][1] == 1 or self.spaces[0][2] == self.spaces[1][2] == self.spaces[2][2] == 1 or self.spaces[0][0] == self.spaces[1][1] == self.spaces[2][2] == 1 or self.spaces[0][2] == self.spaces[1][1] == self.spaces[2][0] == 1):
                        return True

                elif(self.spaces[0][0] == self.spaces[0][1] == self.spaces[0][2] == 2 or self.spaces[1][0] == self.spaces[1][1] == self.spaces[1][2] == 2 or self.spaces[2][0] == self.spaces[2][1] == self.spaces[2][2] == 2 or self.spaces[0][0] == self.spaces[1][0] == self.spaces[2][0] == 2 or self.spaces[0][1] == self.spaces[1][1] == self.spaces[2][1] == 2 or self.spaces[0][2] == self.spaces[1][2] == self.spaces[2][2] == 2 or self.spaces[0][0] == self.spaces[1][1] == self.spaces[2][2] == 2 or self.spaces[0][2] == self.spaces[1][1] == self.spaces[2][0] == 2):
                        return True 
                
                return False

