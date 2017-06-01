from microbit import *
compass.calibrate()

while True:
    sleep(100)
    needle = ((15 - compass.heading())//30)%12
    """
    The clock starts from 1
    The clock turns the opposite side, so we want the hand in reverse order
    and offset it by 15
    - // means integer division
    """
    display.show(Image.ALL_CLOCKS[needle])
