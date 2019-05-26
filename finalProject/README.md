# Welcome to School!
## CS 110 Final Project
### Spring, 2018

https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none.git

[link to demo presentation slides](#)

### Team: .titanic (float:none)
#### Team Names: Mackenzie Murphy, Matthew Bradshaw, Jaewoo Kim
                 

***
FINAL ATP: https://docs.google.com/document/d/1QnCburOmXsI9Yv-sDnuCjhX1gKEjSCiH1oF1JTUgO0A/edit?usp=sharing

[ ATP done on Google Docs AND Markdown, but it looks A LOT better on Google Docs, so please look at that :) ]
***

## Project Description

Mini games, known as short video games, are contained in the main game. These are usually offered as bonus stages with different rules. The purpose of mini games is to allow users to enjoy various styles of playing the main game. Although they seem to be restricted on their small sizes and simplicity, they are beloved by many people. Two mini games that our team created are for those who love playing mini games. As mentioned, we have two mini games called “Quiz” (Tic-Tac-Toe) and “Get to Class”. The game starts as soon as the player chooses one of two doors on the start screen. Since this is a school themed collection of mini games, a player becomes a student, takes a quiz and has to get to class on time. 
***    

## User Interface Design
### II. UI Design

#### 1. Start Screen

As soon as a player runs the game he sees the text, “Welcome to School” and “Pick a door to begin” with a brick wall background and a school bell ringing. There are two doors that the player can enter as the student character. The player can choose the first door by pressing the left key, the second door by pressing the right key, or the player can exit the game by click the ‘x’ which is on the top right of the screen. 

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/menu.jpg.png "Start Menu") 

#### 2. The Game Menu

Tic-tac-toe: A user plays against the computer on a three by three tic-tac-toe board on the screen. The player marks X and the computer marks O on the board. To win the game, the player has to get three X’s in a row. The player can mark on the board by pressing the number keys from 1 to 9.

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/ttt.jpg.png "ttt menu")

Get to Class: A player needs to dodge randomly generated desks that are scattered throughout the screen. The size of each desk, as well as the placement of each desk is random. If the player gets to other other side of the screen in a certain amount of time, he wins the game.

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/class.jpg.png "Get to Class")

#### 3. Game Over Menu

This screen appears when the player finishes the game. If the player wins, he can see the text “You Passed”. If the player loses, the text “You Failed” comes up. Finally, “You tied with the teacher” screen pops up if the player ties in the game. The player can exit the game while he/she is playing by clicking the ‘x’ button on the upper righthand corner. After finishing the game, the player automatically returns to the start screen.  (Screenshots are shown in the next section)

#### 4. Final GUI Interface (Tic-Tac-Toe)

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/quizdoor.jpg.png "quiz door")

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/passed.jpg.png "you passed")

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/fail.jpg.png "your failed")

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/tie.jpg.png "tie")

#### 4. Final GUI Interface (Get To Class)

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/classdoor.jpg.png "door to class")

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/timeup.jpg.png "you're late")

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/yay.jpg.png "You Made It!")


***        

## Program Design

### Non Standard Libraries and Modules Used
* Pygame (https://www.pygame.org/) - Pygame is a module set that incorporates many common game functions into Python.  This was created by Pete Shinners and the pygame community.  This module includes graphical elements and a music playback function. 

### Class and File Relationships (Flow Chart)

![alt text](https://github.com/binghamtonuniversity-cs110/final-project-spr18-titanic-float-none/blob/master/atp_pics/00001.jpg "Flow Chart")

### List of Classes
* Controller : A class that defines the logistics of the relationships between all of the other classes being imported.  This class also plays sound effects with the pygame.mixer() functionalities, as well as allowing user input from the keyboard and interpreting it.  Also, this class keeps track of time, which becomes useful within the various game loops because time can determine if the user is successful or not.  The menu (start screen) is defined here, and depending on the user input, the various game windows are called from this class.  His/her input decides which game he/she is going to play, and therefore, which game menu pops up. It shows two doors that represent which games players may choose to play.  This class also implements methods within the other classes that determine whether or not the user has won or lost his/her game of choice.  Based on the outcome, the Controller class generates the “Game Over” screen for each game, whether it be a Win, Loss, or Tie (in the case of Tic-Tac-Toe or “Quiz”).

* ticTacToe : A class that defines the entirety of the Tic-tac-toe game.  This includes setting the entire board up, giving the instructions, and placing the previously made game pieces (“X” and “O”) in their proper spots based on the user input taken in as a parameter from the Controller class.  There is a function that checks if the spot chosen is filled, as well as another function checking if the entirety of the board is filled.  A key component of this class is the function that checks if there is a winner (isWinner(self)), because this will determine when a “Game Over” screen pops up in the Controller.
		
* Desk : A class that defines each “desk” - a rectangle of random size that is placed at a random place upon the surface.  It remains stationary throughout the entire game, and it is the player’s job to avoid it.  This class also displays the rules of the “Get to Class!” game.

* Player : A class that defines the user-controlled character in the game. It has a base level of speed, and it can be moved in increments of that set speed by pressing the arrow keys on the keyboard. It also includes a function that tests if the player has collided with a desk, which is implemented in the Controller to test whether or not a “Game Over” screen should be shown.

***

## Tasks and Responsibilities
### Software Lead - Jaewoo Kim

The Software Lead managed the tasks schedule, updated the readme, and made most of the proposal for the project. He also worked with both the Front End and the Back End so that both can work very easily together without much friction, facilitating the process of collaborating on such a long project. He talked about theme of the game with Front End so that she can think of proper images to use in each game, and simultaneously, he worked with Front End to add sound effects, and help further compartmentalize the classes for each game. He also got the team, as a whole, to debug the code. 

### Front End Specialist - Mackenzie Murphy

Front-end lead created the visual aspects of the project, as well as implementing the functions created by the Back End Specialist. She used door images in the start menu so the player can notice that each door is assigned to a different game. She used many images such as various backgrounds, pieces like “X” and “O,” a character, desks, etc. to strengthen the presentation of the project as a whole. She worked with on-screen text so that players can easily follow the instructions of each game. She used this information to design and program a consistent UI to help players get used to the game quickly. In addition to adding various visual elements for the UI, she worked with the Software Lead to add different sound effects based on the result of the games.. She also worked with Back End Specialist to improve UI by debugging the code near the end of the project.

### Back End Specialist - Matthew Bradshaw

The back end specialist wrote the major classes that would be used in the each game, as well as implementing the majority of the pygame library. He made significant progress in the mechanics that went into each game, such as the placement of each game piece in the “Quiz” (Tic-Tac-Toe). In Tic-tac-toe, he came up with the idea of using the grid of the number pad, to make it easier for users to visualize which spaces the linear keys on the keyboard actually represent.  In “Get to Class,” he made the basic movements of the character possible, as well as other advanced settings of the game such as randomizing the sizes of desks, and scattering them throughout the screen. He also collaborated with the Front End Specialist and Software Lead so that the game runs smoothly with other visual elements and the sound effects of the game.

***

## Testing

### Menu Testing

First, we pressed left key to check that a character enters into the first door and Tic-tac-toe automatically starts. We pressed right key to check that the character enters into the third door and Get to Class automatically starts. We also clicked ‘x’ button on the right top of the start screen to end the program.

### Game Testing

When “Tic-tac-toe” runs, first we check that the instructions are placed on the top of the game screen.  We make sure the player and computer can place a piece once when it is their own turn. We could mark in the place where we want by pressing a number key from 1 to 9. The computer marks a random place on the board that is not where we already played. It also does not mark on the same place it did itself. If we win the game, the “You Passed” text came out. If we lose, the “You Failed” came out.  We can also see the “You tied with the teacher!” if we tie. The Start Menu appears automatically after playing the game.

When “Get to Class” runs, first we check that the instructions are placed on the bottom of the screen. We make sure that starting point of the character is at bottom. We press the right, left, up and down keys to check if the character moves in the direction of keys being pressed. We also check if the desks are created in random sizes, and scattered throughout the screen. When the character gets hit by a desk, or the character does not make it to the other side in time, the “You Are Late” text comes out. If it gets to the other side on time, the “You Made it” text pops up.  Lastly, we check that “Get to Class” does not reappear in this game screen, but rather, we are returned to the Start Menu automatically after playing the game.

***
## Acceptance Test Procedure

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Running Controller()  | 1) Pressing left key leads to "Quiz" 2) Pressing right key leads to "Get to Class" 3) Bell should sound at the appearance of the start screen  |          |
|  2  | Running Tic-Tac-Toe  | Start Menu Starts automatically |                 |
|  3  | Checking text on the Tic-Tac-Toe  | 1) “Quiz Time” text places at the top of the screen 2) At the bottom of “Quiz Time”, there is a text “Directions: The tic-tac-toe board corresponds to your number pad, i.e.: 7 = the top left box”  |                 |
 |  4  | User marks on the screen  | A player can mark on the screen by pressing number keys |                 |
 |  5  | Computer marks on the screen  | 1) Computer does not mark over where the player did 2) Computer does not mark on the gameboard when it’s player’s turn. |                 |
|  6  | Check game over text  | 1) “You Passed!” text comes out if the player wins 2) “You Failed” text comes out if he loses  3) “You tied with the teacher” text comes out if he ties |                 |
|  7  | Check sound effect after the game  | 1) If a player wins, clapping sound should be played 2) If he loses, “boo” sounds should be heard |                 |
|  8  | Returning to the Start Screen  | Automatically returns to the start screen after the game |                 |
|  9  | Running ‘Get to Class’   | Start Menu Starts automatically |                 |
|  10  | Check desks   | 1) Desks should be random sizes 2) Desks should be randomly scattered throughout the screen |                 |
|  11  | Moving Character  | 1) Pressing right key to move to the right. 2) Pressing left key to move to the left. 3) Pressing up key to move up. 4) Pressing down key to move down. |                 |
|  12  | Check collision happens  | “You’re Late!” text should come out when the character is hit by a desk |                 |
|  13  | Check text after the game  | 1) “You Made It!” text comes out when a player gets to the other side in time. 2) “You tie with the teacher!” text should never come out 3) “You’re Late!” should also come out when the player does not get to the other side in time |                 |
|  14  | Returning start screen  | Automatically returns to the start screen after the game. |                 |
|  15  | Click ‘x’ button on right top of the screen  | The window should be closed |                 |
