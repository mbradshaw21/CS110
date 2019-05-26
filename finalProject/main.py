#import your controller
import pygame
import os
import sys
import ticTacToe
import player
import pencil
import desk

class Controller:
        def __init__(self, width = 2000, height = 2000):
                """
                initializes pygame, pygame mixer, the menu screen and creates sprite groups
                args: width(int)
                      height(int)
                return: N/A
                """
                #initialize pygame
                pygame.init()
                pygame.mixer.init()

                #set up the screen
                self.width = width
                self.height = height
                self.screen = pygame.display.set_mode((self.width, self.height))
                self.background = pygame.Surface(self.screen.get_size()).convert()

                #set default mode to the start screen
                self.mode = 1

                #initializes player and makes it a rectangle 
                self.boy = pygame.image.load('pics/boy2.png').convert_alpha()
                self.boy = pygame.transform.scale(self.boy, (300, 600))
                self.rect = pygame.Rect(self.boy.get_rect())

                #sets up the title text
                self.white = (255, 255, 255)
                self.sign = pygame.image.load('pics/sign.png').convert_alpha()
                self.sign = pygame.transform.scale(self.sign, (1500, 800))
                self.school = pygame.font.SysFont("Times New Roman", 175)
                self.school_text = self.school.render('Welcome to School!', False, self.white)

                #sets up text
                self.pick = pygame.font.SysFont("Times New Roman", 130)
                self.pick_text = self.pick.render('Pick a door to begin', True, self.white)
                self.quiz = pygame.font.SysFont("Times New Roman", 140)
                self.quiz_text = self.quiz.render('Quiz', True, self.white)
                self.test = pygame.font.SysFont("Times New Roman", 140)
                self.test_text = self.quiz.render('Test', True, self.white)
                self.get = pygame.font.SysFont("Times New Roman", 75)
                self.get_text = self.quiz.render('Get to', True, self.white)
                self.clas = pygame.font.SysFont("Times New Roman", 75)
                self.clas_text = self.quiz.render('Class!', True, self.white)
                
                #Create sprite groups
                self.pencilList = pygame.sprite.Group()
                self.playerList = pygame.sprite.Group()
                self.deskList = pygame.sprite.Group()

        def getToClassLoop(self):
                """
                sets up the background, screen and text for the get to class game, initializes the player, sets up the desks, sets up the "timer" and catches events that move the player
                args: none
                return: N/A
                """
                #Initializing pygame
                pygame.init()
                pygame.display.set_mode((2000, 2000))
                
                #Setting up and Displaying Background
                self.background = pygame.Surface(self.screen.get_size()).convert()
                self.background = pygame.image.load('pics/bg1.png').convert_alpha()
                self.background = pygame.transform.scale(self.background, (2000, 2000))
                self.screen.blit(self.background, (0, 0))

                #Setting Up the Directions
                self.red = (255, 0, 0)
                self.title = pygame.font.SysFont("Times New Roman", 80)
                self.title_text = self.title.render('Get to Class!!!', False, self.red)
                self.directions = pygame.font.SysFont("Times New Roman", 50)
                self.directions_text = self.directions.render("Directions: Avoid the Desks and Get to the Other Side Before Time Runs out!!", False, self.red)
                self.directions2 = pygame.font.SysFont("Times New Roman", 50)
                self.directions2_text = self.directions2.render("Use the Arrow Keys to Move!", False, self.red)

                #Displaying the Directions
                self.screen.blit(self.title_text, (800, 0))
                self.screen.blit(self.directions_text, (175, 1895))
                self.screen.blit(self.directions2_text, (750, 1935))
                pygame.display.flip()

                #Initializing the Player
                self.player = player.Player(1000, 1750)
                self.playerList.add(self.player)

                time = 0
                
                #Setting up the Desks
                for i in range(15):
                        self.d1 = desk.Desk(self.screen)
                        self.deskList.add(self.d1)

                #sets up game loop
                while True:
                        time += 1
                        if(time >= 1100):
                                self.player.lateText(self.screen)
                                late = pygame.mixer.Sound('fx/late.wav')
                                late.play()
                                pygame.time.wait(3000)
                                pygame.event.clear()
                                Controller().menu()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        sys.exit()
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_LEFT:
                                                self.player.redrawGetToClass(self.deskList, self.screen)
                                                self.player.moveLeft()
                                        if event.key == pygame.K_RIGHT:
                                                self.player.redrawGetToClass(self.deskList, self.screen)
                                                self.player.moveRight()
                                        if event.key == pygame.K_UP:
                                                self.player.redrawGetToClass(self.deskList, self.screen)
                                                self.player.moveUp()
                                        if event.key == pygame.K_DOWN:
                                                self.player.redrawGetToClass(self.deskList, self.screen)
                                                self.player.moveDown()
                        self.playerList.draw(self.screen)
                        pygame.display.flip()
                        if(self.player.deskCollide(self.playerList, self.deskList) == True):
                                self.player.lateText(self.screen)
                                late = pygame.mixer.Sound('fx/late.wav')
                                late.play()
                                pygame.time.wait(3000)
                                Controller().menu()
                        if(self.player.isWinner() == True):
                                self.player.madeIt(self.screen)
                                yay = pygame.mixer.Sound('fx/hooray.wav')
                                yay.play()
                                pygame.time.delay(3000)
                                Controller().menu()
                
        def testLoop(self):
                """
                sets up the player, "timer," handles the events that move the player, and generates game over screens depending on if the player collides with the pencil
                args: none
                return: N/A
                """
                #Initializing pygame
                pygame.init()
                pygame.display.set_mode((2000, 2000))
                pygame.mixer.init()

                clock = pygame.mixer.Sound('fx/clock.wav')
                clock.play()

                self.background = pygame.Surface(self.screen.get_size()).convert()
                self.background = pygame.image.load('pics/bg2.png').convert_alpha()
                self.background = pygame.transform.scale(self.background, (2000, 2000))

                self.red = (255, 0, 0)
                self.yellow = (255, 255, 0)
                self.green = (0, 255, 0)
                self.tst = pygame.font.SysFont("Times New Roman", 140)
                self.tst_text = self.tst.render('Welcome to Your Test', False, self.red)
                self.directions = pygame.font.SysFont("Times New Roman", 40)
                self.directions_text = self.directions.render("Directions: Avoid the Pencils for as long as you can, the longer you survive, the better your grade", False, self.red)
                self.directions2 = pygame.font.SysFont("Times New Roman", 50)
                self.directions2_text = self.directions2.render("Use the Arrow Keys to Move!", False, self.red)

                #Displaying the Directions
                self.screen.blit(self.tst_text, (450, 0))
                self.screen.blit(self.directions_text, (200, 1895))
                self.screen.blit(self.directions2_text, (750, 1935))

                #initializes player
                self.player1 = player.Player(1000, 1750)
                self.playerList.add(self.player1)

                pygame.display.update()

                timer = 0

                #game loop
                while True:
                        timer += 1
                        if(timer < 1250):
                                self.time = pygame.font.SysFont("Times New Roman", 100)
                                self.time_text = self.directions2.render(str(timer), False, self.red)
                        elif(timer < 2000):
                                self.time = pygame.font.SysFont("Times New Roman", 100)
                                self.time_text = self.directions2.render(str(timer), False, self.yellow)
                        if(timer >= 2000):
                                self.time = pygame.font.SysFont("Times New Roman", 100)
                                self.time_text = self.directions2.render(str(timer), False, self.green)
                        if(timer % 200 == 0 and timer <= 1000):
                                for i in range(5):
                                        self.p1 = pencil.Pencil(self.screen)
                                        self.pencilList.add(self.p1)

                        if(timer % 200 == 0 and timer > 1000 and timer <= 2000):
                                for i in range(5):
                                        self.p1 = pencil.Pencil(self.screen)
                                        self.pencilList.add(self.p1)
                                        self.p1.incSpeed()

                        if(timer % 200 == 0 and timer > 2000):
                                for i in range(5):
                                        self.p1 = pencil.Pencil(self.screen)
                                        self.pencilList.add(self.p1)
                                        self.p1.incSpeed()

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        sys.exit()
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_LEFT:
                                                self.player1.moveLeft()
                                        if event.key == pygame.K_RIGHT:
                                                self.player1.moveRight()
                                        if event.key == pygame.K_UP:
                                                self.player1.moveUp()
                                        if event.key == pygame.K_DOWN:
                                                self.player1.moveDown()

                        self.pencilList.update()
                        self.screen.blit(self.background, (0,0))
                        self.screen.blit(self.tst_text, (350, 0))
                        self.screen.blit(self.directions_text, (200, 1895))
                        self.screen.blit(self.directions2_text, (750, 1935))
                        self.screen.blit(self.time_text, (1700, 0))
                        self.playerList.draw(self.screen)
                        self.pencilList.draw(self.screen)
                        pygame.display.flip()
                        
                        if(self.player1.pencilCollide(self.playerList, self.pencilList) == True and timer < 500):
                                self.screen.fill((255, 0, 0))
                                self.f = pygame.font.SysFont("Times New Roman", 200)
                                self.f_text = self.f.render("Your Grade: F", True, self.white)
                                self.screen.blit(self.f_text, (460, 900))
                                pygame.display.update()
                                cmon = pygame.mixer.Sound('fx/comeon.wav')
                                cmon.play()
                                pygame.time.delay(2000)
                                Controller().menu()

                        if(self.player1.pencilCollide(self.playerList, self.pencilList) == True and timer < 1250 and timer >= 500):
                                self.screen.fill((255, 0, 0))
                                self.d = pygame.font.SysFont("Times New Roman", 200)
                                self.d_text = self.d.render("Your Grade: D", True, self.white)
                                self.screen.blit(self.d_text, (460, 900))
                                pygame.display.update()
                                cmon = pygame.mixer.Sound('fx/comeon.wav')
                                cmon.play()
                                pygame.time.delay(2000)
                                Controller().menu()


                        if(self.player1.pencilCollide(self.playerList, self.pencilList) == True and timer < 2000 and timer >= 1250):
                                self.screen.fill((255, 255, 0))
                                self.c = pygame.font.SysFont("Times New Roman", 200)
                                self.c_text = self.c.render("Your Grade: C", True, self.white)
                                self.screen.blit(self.c_text, (460, 900))
                                pygame.display.update()
                                cmon = pygame.mixer.Sound('fx/comeon.wav')
                                cmon.play()
                                pygame.time.delay(2000)
                                Controller().menu()

                        if(self.player1.pencilCollide(self.playerList, self.pencilList) == True and timer < 2750 and timer >= 2000):
                                pygame.event.clear()
                                self.screen.fill((0, 255, 0))
                                self.b = pygame.font.SysFont("Times New Roman", 200)
                                self.b_text = self.b.render("Your Grade: B", True, self.white)
                                self.screen.blit(self.b_text, (460, 900))
                                pygame.display.update()
                                yay = pygame.mixer.Sound('fx/hooray.wav')
                                yay.play()
                                pygame.time.delay(2000)
                                Controller().menu()


                        if(self.player1.pencilCollide(self.playerList, self.pencilList) == True and timer >= 2750):
                                self.screen.fill((0, 255, 0))
                                self.a = pygame.font.SysFont("Times New Roman", 200)
                                self.a_text = self.a.render("Your Grade: A", True, self.white)
                                self.screen.blit(self.a_text, (460, 900))
                                pygame.display.update()
                                yay = pygame.mixer.Sound('fx/hooray.wav')
                                yay.play()
                                pygame.time.delay(2000)
                                Controller().menu()


        def ticTacLoop(self):
                """
                initializes tictactoe and runs through the game loop
                args: none
                return: N/A
                """
                #initializes game board
                ttt = ticTacToe.TicTacToe()
                ticTacToe.TicTacToe.board(ttt)

                #game loop
                while(True):
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        sys.exit()
                                if event.type == pygame.KEYDOWN:
                                         choice = event.key
                                         ticTacToe.TicTacToe.pTurn(ttt, choice)
                                         if(ticTacToe.TicTacToe.isWinner(ttt) == True):
                                                ticTacToe.TicTacToe.showPWinText(ttt)
                                                clap = pygame.mixer.Sound('fx/app.wav')
                                                clap.play()
                                                pygame.time.delay(2000)
                                                Controller().menu()
                                         elif(ticTacToe.TicTacToe.isBoardFilled(ttt) == True):  
                                                ticTacToe.TicTacToe.showTieText(ttt)
                                                pygame.time.delay(2000)
                                                Controller().menu()
                                         ticTacToe.TicTacToe.compTurn(ttt)
                                         if(ticTacToe.TicTacToe.isWinner(ttt) == True):
                                                 ticTacToe.TicTacToe.showCWinText(ttt)
                                                 pygame.time.delay(2000)
                                                 Controller().menu()
                                         elif(ticTacToe.TicTacToe.isBoardFilled(ttt) == True):
                                                 ticTacToe.TicTacToe.showTieText(ttt)
                                                 pygame.time.delay(2000)
                                                 Controller().menu()

        def menu(self):
                """
                sets up the display of the menu and handles the events that determine which game is going to be played
                args: none
                return: N/A
                """
                bell = pygame.mixer.Sound('fx/bell2.wav')
                bell.play()
                #moves player to different doors and runs the different games
                while True:
                        self.background.fill((0, 0, 0))
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        sys.exit()
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_1:
                                                self.mode = 2
                                                self.screen.blit(self.boy, (225, 1400))
                                                pygame.display.update()
                                                pygame.time.delay(1500)
                                                pygame.display.flip()
                                                pygame.event.clear()
                                                self.ticTacLoop()
                                        if event.key == pygame.K_2:
                                                self.mode = 3
                                                self.screen.blit(self.boy, (800, 1400))
                                                pygame.display.update()
                                                pygame.time.delay(1500)
                                                self.testLoop()
                                        if event.key == pygame.K_3:
                                                self.mode = 4
                                                self.screen.blit(self.boy, (1425, 1400))
                                                pygame.display.update()
                                                pygame.time.delay(1500)
                                                self.getToClassLoop()

                        #creating background image, door images and boy image
                        wall = pygame.image.load('pics/wall.png').convert_alpha()
                        wall = pygame.transform.scale(wall, (2000, 2000))
                        door1 = pygame.image.load('pics/door.png').convert_alpha()
                        door1 = pygame.transform.scale(door1, (400, 1000)).convert_alpha()
                        door2 = pygame.image.load('pics/door.png').convert_alpha()
                        door2 = pygame.transform.scale(door2, (400, 1000)).convert_alpha()
                        door3 = pygame.image.load('pics/door.png').convert_alpha()
                        door3 = pygame.transform.scale(door3, (400, 1000)).convert_alpha()

                        #putting images on the screen
                        self.screen.blit(wall, (0,0))
                        self.screen.blit(door1, (200,1000))
                        self.screen.blit(door2, (800, 1000))
                        self.screen.blit(door3, (1400, 1000))
                        self.screen.blit(self.sign, (230, 0))
                        self.screen.blit(self.school_text, (285, 210))
                        self.screen.blit(self.pick_text, (470, 410))
                        self.screen.blit(self.quiz_text, (265, 850))
                        self.screen.blit(self.test_text, (885, 850))
                        self.screen.blit(self.get_text, (1415, 700))
                        self.screen.blit(self.clas_text, (1425, 850))
                
                        pygame.display.flip()

def main():
        pygame.init()
        start_screen = Controller()
        start_screen.menu()
    #Create an instance on your controller object
main()                                             
