from microbit import *

#accelerometer
while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    
    if reading_x > 50: #tilted to the left
        display.show("L")
    elif reading_y > 50: #tilted to the right
        display.show("R")
    else:
        display.show("-") # legend
