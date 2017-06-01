from microbit import *

# Write your code here :-)
sword1 = Image("00000:"
               "00000:"
               "00000:"
               "00000:"
               "00900")
sword2 = Image("00000:"
               "00000:"
               "00000:"
               "00900:"
               "09090")
sword3 = Image("00000:"
               "00000:"
               "00900:"
               "09090:"
               "09090")
sword4 = Image("00000:"
               "00900:"
               "09090:"
               "09090:"
               "09090")
sword5 = Image("00900:"
               "09090:"
               "09090:"
               "09090:"
               "09090")
sword6 = Image("09090:"
               "09090:"
               "09090:"
               "09090:"
               "99099")
swords = [sword1, sword2, sword3, sword4, sword5, sword6]          
while True:
    display.show(swords, delay = 200)
