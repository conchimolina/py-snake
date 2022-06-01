"""
Classic Snake with PyGame.

@authors
Conchi Molina <conchimb110@gmail.com>
Jaime Tomás <jaitomuuu8@gmail.com>
Ana Subiela <anasubiela0@gmail.com>
Miriam Gonzalez <miriamgonzalezfernandez2003@gmail.com>
Alex Botella <alexbot61.ab@gmail.com>
@license MIT
Copyright (c) 2022 Snake Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import settings
from script import init_game
from script import direction_manager
from script import move_snake
from script import eat_food
from script import respawn_food
from script import update_gui


def main():
    init_game()

    while True:
        # Calculate the new direction (based on hooks)
        direction_manager()

        # Moving the Snake
        move_snake()

        # Snake body growing
        eat_food()

        # Respawn food
        respawn_food()

        # Update the GUI
        update_gui()

        # Clock tick
        settings.fps_controller.tick(settings.difficulty)


if __name__ == "__main__":
    main()
