
# Python GUI Snake Game
This project is a simple implementation of the classic Snake game using Python’s turtle module. The game includes a snake that moves around the screen, eating food and growing in length. The game ends if the snake collides with the wall or with its own body.

# Game Components
The game consists of three main components: the snake, the food, and the score board.

# Snake
The snake is represented as a series of squares. The snake moves in a straight line and can be directed using the arrow keys. The snake grows in length each time it eats food.

# Food
The food is represented as a small circle. Each time the snake eats the food, the food disappears and reappears at a random location on the screen.

# Score Board
The score board keeps track of the player’s score, which increases each time the snake eats food. The score is displayed at the top of the screen. When the game ends, a “GAME OVER!” message is displayed.

# Libraries Used
turtle: This is a pre-installed Python library that enables users to create pictures and shapes by providing them with a virtual canvas. The onscreen pen that you use for drawing is called the “turtle”.
random: This module implements pseudo-random number generators for various distributions including integer and float. We use it to generate random locations for the food.
time: This module provides various time-related functions. We use it to control the speed of the game.
