# Space Hunt
A Shoot-em-up Game run with the Pygame module


## How To Run
### Software Requirements
Space Hunt is written in python 3, so being able to run python code is required. The only module used that is not in the Python Standard Library is the pygame module, a set of modules meant to assist in creating animations and handling collisions(and a number of other game-related functionalities). It's largely a wrapper for SDL(Simple DirectMedia Layer), and it is not unlikely that if you have a computer with which you can code in and run python, the pygame module will work with it.    
To download the latest version of python, go to https://www.python.org/downloads/ and follow the instructions for your OS.  
Your version of python will likely come with python's standard package installer, pip(package installer for python), but if it does not you can download it following the instructions at this link: https://pip.pypa.io/en/stable/installation/    
Finally, if you have pip installed you should be able to use the command
`python3 -m pip install -U pygame`
in your command line to install pygame, but if this does not work and you want more detailed instructions go to https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation
### Running the game
The file containing the main "run_game" function that runs the entire game is "space_hunt.py". Once you have met the software requirements and have compiled the files in the project, all you need to do to run the space_hunt file. So navigating to the project directory in the command line and 

## Gameplay
The basic idea of the game is modeled after the famous arcade game "Space Invaders", developed by Tomohiro Nishikado. The player controls a ship that moves and shoots bullets to defeat descending fleet of aliens and prevent them from reaching the ship or the bottom of the screen, gaining points for each alien defeated. It can also collide with powerups that fall down the screen and give temporary advantageous abilities to the user ship. The game inevitably ends only once the player runs out of lives from failing to do so a given number of times. The goal is to get the highest score possible. As the game progresses and the level increases, the speed of game elements increases, making the game more difficult.
![Space Hunt Gameplay Screenshot MarkedUp](https://user-images.githubusercontent.com/54511402/167519382-28087212-6dd0-45ca-b90f-3a07256bce16.png)  


## Game Elements
The game has a number of elements that interact with one another on collision

### 1. User Ship
![ship](https://user-images.githubusercontent.com/54511402/167516018-eea1c70b-c6c8-4bf8-b4b3-03d34f97e297.png)  
The user ship can be moved left and right by pressing and holding down the left and right arrow keys respectively. This can be done to catch powerups and avoid alien bullets. The ship can fire bullets from it's current position by using the spacebar. These bullets move up the screen and eliminate aliens on collision with alien elements. The ship loses a life if it collides with an alien or an alien bullet.

### 2. Aliens
![alien](https://user-images.githubusercontent.com/54511402/167516065-8509ab59-777a-4801-8a5b-4939eb9c5e08.png)  
Aliens come at the beginning of each level in fleets that always move in unison. The fleet always moves to the left or right, and when any alien collides with either side of the screen, the fleet changes direction from left to right (or vice-versa) and moves a set interval down the screen. If any alien either collides with the ship or reaches the bottom of the screen, the player loses a life. Aliens can also fire bullets, which take a ship life on collision with the ship.

### 3. Bullets
- ***3a. Ship bullets***  
  Ship bullets are fired by the ship using the spacebar, and eliminate an alien and themself on collision with the alien. The amount of ship bullets that can exist on screen is limited unless the unlimited bullet powerup is in effect.  
- ***3b. Alien Bullets***  
  Aliens shoot bullets at random intervals of time that can take a ship life on collision with the ship. A random group of aliens of random number (limited by a game setting) are chosen to sometimes shoot bullets at set intervals of time.
  
### 4. Powerups
- ***4a. Powerups***  
  Powerups appear randomly on screen and fall down the screen, dissapearing off the bottom of the screen. On collision with the user ship they activate effects that give the user a boost.  
    - **Unlimited Bullets**  
    ![unlimited_bullets](https://user-images.githubusercontent.com/54511402/167512895-fa18fae5-5da8-4f3e-b8ad-d2bea9e3d263.png)  
    The unlimited bullets powerup eliminates the limit on bullets allowed on screen so that the ship can fire an unlimited number of bullets regardless of the number of ship bullets already on screen.  
    - **Superspeed Bullets**  
    ![superspeed_bullets](https://user-images.githubusercontent.com/54511402/167512893-e494a305-a857-4aa5-a468-915f1de34978.png)  
    The superspeed bullets powerup makes ship bullets go up the screen super fast.  
    - **Superspeed Ship**  
    ![superspeed_ship](https://user-images.githubusercontent.com/54511402/167512894-c4f8360c-4a24-4a68-a265-4304ef7dd30d.png)  
    The superspeed bullets powerup makes the ship move around the screen super fast.  
    - **Widened Bullets**  
    ![widened_bullets](https://user-images.githubusercontent.com/54511402/167512896-b2e7008f-c748-4702-8e4c-a142982d84fd.png)  
    Allows the ship to shoot very wide bullets that can collide with and eliminate multiple aliens at a time.  
    - **Destroyo Bullet**  
    ![destroyo_bullet](https://user-images.githubusercontent.com/54511402/167515770-549b1083-1f60-4601-8823-99b48baf45dd.png)  
    Allows the ship to shoot bullets that can collide with an unlimited number of aliens and eliminate them without itself being eliminated.  
    - **Alien Bullet Shields**  
    ![alien_bullet_shields](https://user-images.githubusercontent.com/54511402/167512889-6b70548d-652a-412c-829d-9d98d5ac6d01.png)  
    Makes the ship immune to losing lives from collisions with alien bullets.  
    - **Double Points**  
    ![double_points](https://user-images.githubusercontent.com/54511402/167512892-b032a0b4-edd3-4ab2-9310-2fcb76ee6a67.png)  
    Causes the ship to earn double points per alien eliminated.  
- ***4b. Powerup panel***  
  The powerup panel exists in the top left corner of the screen beneath the lives left panel. It shows which powerups are still active by printing the powerup's icon to the screen while it is active.

### 5. Scoreboard
The scoreboard lists the current game score, the highscore, and the current game level.
  - a. **5a. Score**  
  The score is listed in the top-right corner and is updated during the game as it changes.
  - b. **5b. Highscore**  
  The highscore is listed on the top-center of the screen and changes at the end of a game if the current game score is greater than the high score. The high score is kept in a .json file to be maintained between game sessions.
  - c. **5c. Level**  
  The level is listed in the top-right corner of the screen beneath the current score, and increases by one every time an alien fleet is defeated.

### 6. Lives panel
The lives panel is in the top-left corner of the screen. It represents the number of lives left by printing that number of ship icons, and is updated every time the player loses a life.


##


