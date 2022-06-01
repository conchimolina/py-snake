"""
Game settings.

@file Global settings of the Snake game.
@authors
Conchi Molina <conchimb110@gmail.com>
Jaime Tomás <jaitomuuu8@gmail.com>
Ana Subiela <anasubiela0@gmail.com>
Miriam Gonzalez <miriamgonzalezfernandez2003@gmail.com>
Alex Botella <alexbot61.ab@gmail.com>
@description
As we are not using OOP, in order to have a global state in the application,
we are using this module to declare all the global stuff. See it as a provider.
@license MIT
"""

from utils.constants import INITIAL_DIFFICULTY
from utils.constants import INITIAL_SCORE
from utils.constants import INITIAL_SNAKE_POSITION
from utils.constants import INITIAL_SNAKE_BODY
from utils.constants import INITIAL_SNAKE_DIRECTION
from utils.constants import INITIAL_FOOD_POSITION

global game_window
global fps_controller
global difficulty
global score
global snake_pos
global snake_body
global snake_direction
global new_snake_direction
global food_spawn  # flag
global food_pos

difficulty = INITIAL_DIFFICULTY
score = INITIAL_SCORE
snake_pos = INITIAL_SNAKE_POSITION
snake_body = INITIAL_SNAKE_BODY
snake_direction = INITIAL_SNAKE_DIRECTION
new_snake_direction = snake_direction
food_spawn = True
food_pos = INITIAL_FOOD_POSITION
