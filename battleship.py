from microbit import *
from random import randint
# random module

com_board = [[0 for i in range(5)] for j in range(5)]
"""
- can initialise with other values
- initialising the board as "00000:"
                           "00000:"
                           "00000:"
                           "00000:"
                           "00000"
"""
while not button_a.is_pressed():
    display.scroll("Hold A to start")

com_board[randint(0, 4)][randint(0, 4)] = 1
com_board[randint(0, 4)][randint(0, 4)] = 1
# computer will randomly place two ships in the board
# ship might overlap :(

display.scroll("Game start!")
sleep(200)  # delay function
display.clear()

player_point = 0
current = 0
for turns in range(20):
    if player_point == 2:
        break  # if the player has 2 hit points, he wins and game ends
    x_coord = 0
    y_coord = 0
    # cursor position
    while True:
        display.set_pixel(x_coord, y_coord, 9)  # display the current position
        if button_a.is_pressed() and button_b.is_pressed():  # attack
            if com_board[y_coord][x_coord] == 0:  # the attack missed
                display.set_pixel(x_coord, y_coord, 2)
                sleep(3000)
            else:  # it hit the target
                display.set_pixel(x_coord, y_coord, 9)
                player_point += 1
                display.show(Image.HAPPY)
                sleep(1000)
            break

        elif button_a.is_pressed() or button_b.is_pressed():
            display.set_pixel(x_coord, y_coord, current)
            if button_a.is_pressed():
                x_coord = (x_coord + button_a.get_presses()) % 5
            else:
                y_coord = (y_coord - button_b.get_presses()) % 5

if player_point == 2:
    display.show("player wins!")
else:
    display.show("computer wins!")
