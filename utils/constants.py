"""
Game constants.

@file This module contains all the constants of the Snake game.
@authors
Conchi Molina <conchimb110@gmail.com>
Jaime Tomás <jaitomuuu8@gmail.com>
Ana Subiela <anasubiela0@gmail.com>
Miriam Gonzalez <miriamgonzalezfernandez2003@gmail.com>
Alex Botella <alexbot61.ab@gmail.com>
@license MIT
"""

from random import randrange
from pygame import Color

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GREEN = Color(0, 255, 0)
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
GAME_TITLE = "Snake Classic"
GAME_OVER_TXT = "Game Over"
SCORE_TXT = "Score: "
PIXELS_PER_MOVE = 10
FOOD_SIZE = 10
SNAKE_MIN_SIZE = FOOD_SIZE
INITIAL_DIFFICULTY = 25
MAX_RECOMMENDED_DIFFICULTY = 100
INITIAL_SCORE = 0
INITIAL_SNAKE_DIRECTION = RIGHT
INITIAL_SNAKE_POSITION = [100, 50]
INITIAL_SNAKE_BODY = [
    INITIAL_SNAKE_POSITION.copy(),  # important!
    [INITIAL_SNAKE_POSITION[0] - PIXELS_PER_MOVE, INITIAL_SNAKE_POSITION[1]],
    [100 - (2 * 10), 50],
]
INITIAL_FOOD_POSITION = [
    randrange(1, (WINDOW_WIDTH // FOOD_SIZE)) * FOOD_SIZE,
    randrange(1, (WINDOW_HEIGHT // FOOD_SIZE)) * FOOD_SIZE,
]
