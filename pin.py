from microbit import *
while True:
    reading = pin0.read_analog() / 204
    pos = reading // 1
# set the position to the largest integer smaller than the reading
    columns = ['0' for i in range(5)]
    columns[int(pos)] = '9'
    img = ((''.join(columns)+':')*5)[0:-1]
# -1 refers to the last char of the string
# eg. pos = 4; img = 00009:00009:00009:00009:00009: ('00009:'*5)
# excluding the last char
    img = Image(img)
    display.show(img)
"""
Pin capabilities
Pins 0,1,2 - is_touched(), read/write digital, ,read/write analog,
set_analog_period_microseconds, set_analog_period()
Pins 3,4,10 - does all the same, excluding is_touched()
Pins 5-9, 11-16: read/write analog
"""
