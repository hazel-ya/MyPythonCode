"""
File: Heart.py
Name: Hazel:
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def turn_right():
    for i in range(3):
        turn_left()


def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    put_beeper()
    #1

    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    #2

    move()
    turn_left()
    move()
    put_beeper()
    #3

    turn_right()
    move()
    put_beeper()
    #4

    move()
    turn_right()
    move()
    put_beeper()
    #5

    move()
    turn_right()
    move()
    put_beeper()
    #6
    turn_left()
    move()
    turn_left()
    move()
    put_beeper()
    #7

    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    #8


    move()
    put_beeper()
    #9


    turn_right()
    move()
    turn_left()
    move()
    put_beeper()
    #10

    move()
    turn_right()
    move()
    turn_left()
    move()
    #11



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
