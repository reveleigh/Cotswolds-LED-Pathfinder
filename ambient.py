# Import towns
from cotswolds import towns

# Set up NeoPixels
from machine import Pin
import utime
import random
from neopixel import Neopixel

numpix = 145

strip = Neopixel(numpix, 0, 22, "GRB")

strip.brightness(200)

# Function to fade towns in 

def fade(type, start, end):
    if type == "on":
        start_r, start_g, start_b = 0, 0, 0
        end_r, end_g, end_b = 10, 5, 6
    elif type == "white":
        start_r, start_g, start_b = 10, 5, 6
        end_r, end_g, end_b = 255, 255, 255
    elif type == "dim":
        start_r, start_g, start_b = 255, 255, 255
        end_r, end_g, end_b = 10, 5, 6

    # Number of steps in the fade
    steps = 50
    # Delay between each step (in seconds)
    delay = 0.02
    for i in range(steps + 1):
        # Calculate the current RGB values for this step
        r = int(start_r + (end_r - start_r) * (i / steps))
        g = int(start_g + (end_g - start_g) * (i / steps))
        b = int(start_b + (end_b - start_b) * (i / steps))
        for i in range(start, end):
            strip[i] = (r, g, b)
        strip.show()
        utime.sleep(delay)


fade("on", 0, 144)
utime.sleep(1)

# Choose 5 random towns form the 41 towns with no repeats
chosen_towns = []
while len(chosen_towns) < 5:
    new_town = random.choice(range(0, 41))
    if new_town not in chosen_towns:
        chosen_towns.append(new_town)

#fade in the chosen towns leds by passing the start and end led number
for town in chosen_towns:
    fade("white", towns[town].leds[0], towns[town].leds[-1])

while True:
    # Fade out the first chosen town and remove it from the list
    fade("dim", towns[chosen_towns[0]].leds[0], towns[chosen_towns[0]].leds[-1])
    chosen_towns.pop(0)

    # Add a new random town to chosen_towns not already in the list
    new_town = random.choice(range(0, 41))
    while new_town in chosen_towns:
        new_town = random.choice(range(0, 41))
    chosen_towns.append(new_town)

    # Fade in the new town
    fade("white", towns[new_town].leds[0], towns[new_town].leds[-1])


