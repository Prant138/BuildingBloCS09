from microbit import *
# ^ imports all modules from the microbit like display.show()

while True:
    presses = button_a.get_presses()
    # gets the number of presses (in an integer)
    if presses > 5: # 5 presses in whatever time
        display.show(Image.HEART)
    else:
        display.show(Image.ANGRY)
    sleep(2000)
