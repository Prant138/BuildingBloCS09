from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed(): #is the button preessed?
        display.show(Image.HAPPY)
    elif button_a.is_pressed():
        display.show(Image.HEART)
    elif button_b.is_pressed():
        display.show(Image.COW)
    else:
        display.show(Image.SAD)
