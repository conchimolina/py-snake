"""
Game scripts.

@file This module contains all the helper methods of the Snake game logic.
@authors
Conchi Molina <conchimb110@gmail.com>
Jaime Tomás <jaitomuuu8@gmail.com>
Ana Subiela <anasubiela0@gmail.com>
Miriam Gonzalez <miriamgonzalezfernandez2003@gmail.com>
Alex Botella <alexbot61.ab@gmail.com>
@license MIT
"""

import sys
import time
import pygame
from random import randrange, randint

import settings
from utils.constants import MAX_RECOMMENDED_DIFFICULTY, WINDOW_WIDTH, WINDOW_HEIGHT
from utils.constants import UP, DOWN, LEFT, RIGHT
from utils.constants import BLACK, WHITE, GREEN
from utils.constants import GAME_TITLE
from utils.constants import SCORE_TXT
from utils.constants import PIXELS_PER_MOVE
from utils.constants import SNAKE_MIN_SIZE
from utils.constants import FOOD_SIZE
from utils.constants import GAME_OVER_TXT


#
# Initializes the game, creating the displayer and the FPS
# controller.
#
# @function init_game
# @returns {void} Nothing.
#
def init_game():
    errors = pygame.init()

    if errors[1]:
        print(f"[!] Had {errors[1]} errors, exiting...")
        sys.exit(-1)

    # Initialize the game window
    pygame.display.set_caption(GAME_TITLE)
    settings.game_window = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    # FPS (frames per second) controller
    settings.fps_controller = pygame.time.Clock()

    # Play the background music
    play_music("assets/audios/bg-music.mp3", True)


#
# Handles the keyboard events, calculating the new Snake's direction.
#
# @function direction_manager
# @returns {void} Nothing.
#
def direction_manager():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord("w"):
                settings.new_snake_direction = UP
            elif event.key == pygame.K_DOWN or event.key == ord("s"):
                settings.new_snake_direction = DOWN
            elif event.key == pygame.K_LEFT or event.key == ord("a"):
                settings.new_snake_direction = LEFT
            elif event.key == pygame.K_RIGHT or event.key == ord("d"):
                settings.new_snake_direction = RIGHT
            elif event.key == pygame.K_ESCAPE:  # Exit
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Correct the new direction
    fix_snake_direction()


#
# Corrects the new Snake's direction, making sure that it cannot move
# in the opposite direction instantaneously.
#
# @function fix_snake_direction
# @returns {void} Nothing.
#
def fix_snake_direction():
    if settings.new_snake_direction == UP and settings.snake_direction != DOWN:
        settings.snake_direction = settings.new_snake_direction
    elif settings.new_snake_direction == DOWN and settings.snake_direction != UP:
        settings.snake_direction = settings.new_snake_direction
    elif settings.new_snake_direction == LEFT and settings.snake_direction != RIGHT:
        settings.snake_direction = settings.new_snake_direction
    elif settings.new_snake_direction == RIGHT and settings.snake_direction != LEFT:
        settings.snake_direction = settings.new_snake_direction


#
# Changes the Snake position, based on its direction and the given
# number of pixels.
#
# @function move_snake
# @param {number} [pixels=10] - The number of pixels to increase/decrease
#   per movement.
# @returns {void} Nothing.
#
def move_snake(pixels=PIXELS_PER_MOVE):
    # Y-AXIS
    if settings.snake_direction == UP:
        settings.snake_pos[1] -= pixels
    elif settings.snake_direction == DOWN:
        settings.snake_pos[1] += pixels

    # X-AXIS
    elif settings.snake_direction == LEFT:
        settings.snake_pos[0] -= pixels
    elif settings.snake_direction == RIGHT:
        settings.snake_pos[0] += pixels


#
# Determines whether the food should be eaten or not, growing the Snake's
# body and incrementing the score and the game difficulty accordingly.
#
# @returns {void} Nothing.
#
def eat_food():
    settings.snake_body.insert(0, list(settings.snake_pos))  # optimistic

    if (
        settings.snake_pos[0] == settings.food_pos[0]
        and settings.snake_pos[1] == settings.food_pos[1]
    ):
        settings.score += 1

        difficulty_increment = randint(1, 2)
        if settings.difficulty + difficulty_increment \
                <= MAX_RECOMMENDED_DIFFICULTY:
            settings.difficulty += difficulty_increment

        settings.food_spawn = False
    else:
        settings.snake_body.pop()


#
# Respawns food in the map if it is not present in the current
# render.
#
# @returns {void} Nothing.
#
def respawn_food():
    if not settings.food_spawn:
        settings.food_pos = [
            randrange(1, (WINDOW_WIDTH // FOOD_SIZE)) * FOOD_SIZE,
            randrange(1, (WINDOW_HEIGHT // FOOD_SIZE)) * FOOD_SIZE,
        ]

    settings.food_spawn = True


#
# Changes the state of the graphical interface to 'Game Over'.
#
# @function game_over
# @returns {void} Nothing.
#
def game_over():
    # Play the `Game Over` audio
    play_music("assets/audios/game-over.mp3")

    # Update the UI
    my_font = pygame.font.SysFont("times new roman", 90)
    game_over_surface = my_font.render(GAME_OVER_TXT, True, GREEN)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    settings.game_window.fill(BLACK)
    settings.game_window.blit(game_over_surface, game_over_rect)
    display_score(2, GREEN, "times")
    pygame.display.flip()

    # Exit the game after 5 secs
    time.sleep(5)
    quit()


#
# Displays the provided score.
#
# @function display_score
# @param {number} [choice=1] - Choice.
# @param {string} [color=#fff] - Surface color.
# @param {string} [font='consolas'] - Text font.
# @param {number} [size=20] - Font size.
# @returns {void} Nothing.
#
def display_score(choice=1, color=WHITE, font="consolas", size=20):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(
        SCORE_TXT + str(settings.score),
        True,
        color
    )
    score_rect = score_surface.get_rect()

    if choice == 1:
        x = WINDOW_WIDTH / 10
        y = 15
    else:
        x = WINDOW_WIDTH / 2
        y = WINDOW_HEIGHT / 1.25

    score_rect.midtop = (x, y)
    settings.game_window.blit(score_surface, score_rect)


#
# Draws the Snake's body.
#
# @function draw_snake
# @returns {void} Nothing.
#
def draw_snake():
    for pos in settings.snake_body:
        pygame.draw.rect(
            settings.game_window,
            GREEN,
            pygame.Rect(pos[0], pos[1], SNAKE_MIN_SIZE, SNAKE_MIN_SIZE),
        )


#
# Draws the Snake's food.
#
# @function draw_food
# @returns {void} Nothing.
#
def draw_food():
    pygame.draw.rect(
        settings.game_window,
        WHITE,
        pygame.Rect(
            settings.food_pos[0],
            settings.food_pos[1],
            FOOD_SIZE,
            FOOD_SIZE
        ),
    )


#
# Handles the out of boundaries.
#
# @function handle_out_of_boundaries
# @returns {void} Nothing.
#
def handle_out_of_boundaries():
    if (
        settings.snake_pos[0] < 0
        or settings.snake_pos[0] > WINDOW_WIDTH - SNAKE_MIN_SIZE
    ):
        game_over()

    if (
        settings.snake_pos[1] < 0
        or settings.snake_pos[1] > WINDOW_HEIGHT - SNAKE_MIN_SIZE
    ):
        game_over()


#
# Handles the Snake's body touches.
#
# @function handle_body_touches
# @returns {void} Nothing.
#
def handle_body_touches():
    for block in settings.snake_body[1:]:
        if settings.snake_pos[0] == block[0] and settings.snake_pos[1] == block[1]:
            game_over()


#
# Updates the GUI.
#
# @function update_gui
# @returns {void} Nothing.
#
def update_gui():
    clear_screen()
    draw_snake()
    draw_food()
    handle_out_of_boundaries()
    handle_body_touches()
    display_score()
    pygame.display.update()


#
# Plays the given audio URI.
#
# @function play_music
# @param {string} uri - The audio's uri.
# @param {boolean} [loop=False] - Determines if the music should be
#   repeated indefinitely.
# @returns {void} Nothing.
#
def play_music(uri, loop=False):
    pygame.mixer.init()
    pygame.mixer.music.load(uri)
    pygame.mixer.music.play(-1 if loop else 0)


#
# Clears the screen, willing the window with a black color.
#
# @function clear_screen
# @returns {void} Nothing.
#
def clear_screen():
    settings.game_window.fill(BLACK)


#
# Exits the game.
#
# @function quit
# @returns {void} Nothing.
#
def quit():
    pygame.quit()
    sys.exit()
