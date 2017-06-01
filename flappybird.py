from microbit import *

#flappy bird
# generate pipes, display pipes
# generate bird, display bird, allow the bird to fly

# CONSTANTS - labels your values, and allows code to be more
# readable and are normally named with capital letters.

DELAY = 20 # delay between frames is 20ms
FRAMES_PER_WALL_SHIFT = 20 # move the walls
FRAMES_PER_NEW_WALL = 100 # generates a new wall every 100 frames
FRAMES_PER_SCORE = 50 # 50 frames for one point
# allows your entire program to live in these variables; if you change them here, 
# you won't have to change every instance of the variable/every usage of this value

# global variable
y = 50 # the bird's starting position along the y-axis, between 0-99 inclusive 
# (100 numbers)
speed = 0 # the speed of your bird, There will be a downward acceleration, and downward
# direction is taken as positive.
score = 0 # the player's score
frame = 0 # the game's instances

# let's start

def make_pipe():
    pipe = Image("00003:00003:00003:00003:00003") # only the last column is lit
    """
    00003
    00003
    00003 --> gap = 2
    00003
    00003 the pipe is something like this
    
    result:
    00003
    00003
    00000
    00000
    00003
    """
    
    gap = random.randint(0,3) # note that random is another module.
                              # we can only go from 0-3, then make a gap 2 pixels wide
    pipe.set_pixel(4,gap,0) # (x,y,brightness)
    # x-position 4 points at the column of 3's
    pipe.set_pixel(4,gap+1,0) # we don't need to edit an entire Image string
    return pipe

pipe = make_pipe() # first pipe

# game loop
while True:
    # game lives in this loop
    
    display.show(pipe) #displays the pipe each time
    
    #bird
    if button_a.is_pressed():
        # now we flap
        speed = -8 # --> upward is negative because downward is positive
        # using calculations, the bird travels 1.8 pixels upword / -36 units
        # one press
    speed += 1 #acceleration rate 1 units
    if speed > 2: # terminal velocity
        speed = 2
        
    # move the bird
    # the speed is the rate of change of the y value / y coordinate)
    # 0 <= y <= 99
    if y > 99:
        y = 99
    if y < 0:
        y = 0
        
    #draw the bird
    bird_y = int(y/20) # ignores decimal places
    display.set_pixel(1,bird_y,9) # at coordinate (1,bird_y the brightness is now 9)
    #your bird is a little red dot
    
    #check for collision
    if pipe.get_pixel(1,bird_y) != 0:
        display.show(Image.SAD) #rip
        sleep(500)
        display.scroll("Score: " + str(score))
        break # break out of the while loop
        
    #move wall left
    if frame % FRAMES_PER_WALL_SHIFT == 0:
        pipe = pipe.shift_left(1) #move it by 1 pixel
        
    #generate new pipe
    if frame % FRAMES_PER_NEW_WALL == 0:
        pipe = make_pipe() #reset pipe
        
    #increase score
    if frame % FRAMES_PER_SCORE == 0:
        score += 1
    
    #increase frame, making the game change instance
    sleep(DELAY) 
    frame += 1
