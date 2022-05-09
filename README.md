# space_hunt
A Shoot-em-up Game run with the Pygame module

## Gameplay
The basic idea of the game is modeled after the famous arcade game "Space Invaders", developed by Tomohiro Nishikado. The player controls a ship that moves and shoots bullets to defeat descending fleet of aliens and prevent them from reaching the ship or the bottom of the screen, gaining points for each alien defeated. It can also collide with powerups that fall down the screen and give temporary advantageous abilities to the user ship. The game inevitably ends only once the player runs out of lives from failing to do so a given number of times. The goal is to get the highest score possible. As the game progresses the speed of game elements increases, making the game more difficult.

![Space Hunt Gameplay Screenshot](https://user-images.githubusercontent.com/54511402/167507357-ae505139-2a17-41d3-a9cc-440e4b559048.png)

## Game Elements
The game has a number of elements that interact with one another on collision
### 1. User Ship
The user ship can be moved left and right by pressing and holding down the left and right arrow keys respectively. This can be done to catch powerups and avoid alien bullets. The ship can fire bullets from it's current position by using the spacebar. These bullets move up the screen and eliminate aliens on collision with alien elements. The ship loses a life if it collides with an alien or an alien bullet.
### 2. Aliens
Aliens come at the beginning of each level in fleets that always move in unison. The fleet always moves to the left or right, and when any alien collides with either side of the screen, the fleet changes direction from left to right (or vice-versa) and moves a set interval down the screen. If any alien either collides with the ship or reaches the bottom of the screen, the player loses a life. Aliens can also fire bullets, which take a ship life on collision with the ship.
### 3. Bullets
- ***Ship bullets***  
  Ship bullets are fired by the ship using the spacebar, and eliminate an alien and themself on collision with the alien. The amount of ship bullets that can exist on screen is limited unless the unlimited bullet powerup is in effect.  
- ***Alien Bullets***  
  Aliens shoot bullets at random intervals of time that can take a ship life on collision with the ship. A random group of aliens of random number (limited by a game setting) are chosen to sometimes shoot bullets at set intervals of time.  
### 4. Powerups
- ***Powerups***  
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


- ***Powerup panel***
  The powerup panel exists in the top left corner of the screen beneath the lives left panel. It shows which powerups are still active by printing the powerup's icon to the screen while it is active.
### 5. Scoreboard
  a. Score
  b. Highscore
  c. Level
### 6. Lives panel
