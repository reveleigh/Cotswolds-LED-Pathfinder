from cotswolds import towns
from machine import Pin
import utime
import random
from neopixel import Neopixel

numpix = 145
strip = Neopixel(numpix, 0, 22, "GRB")
strip.brightness(200)

# Function to fade towns by criteria
def fade(type, town, start_town=None, end_town=None):
    # Don't fade the start and end towns
    if town != start_town and town != end_town and start_town != None:
        # All the fade in options
        if type == "in":
            if town.visited: # Bright red if visited
                start_r, start_g, start_b = 255, 0, 0  
            else:
                start_r, start_g, start_b = 10, 0, 0
            end_r, end_g, end_b = 255, 255, 255  # Current town is white
        # All the fade out options
        elif type == "out": # Fade out to red
            start_r, start_g, start_b = 255, 255, 255
            if town.visited:
                end_r, end_g, end_b = 255, 0, 0
            else:
                end_r, end_g, end_b = 10, 0, 0
        elif type == "neighbour_in" and not town.visited:
            start_r, start_g, start_b = 10, 0, 0
            end_r, end_g, end_b = 255, 0, 0
        elif type == "neighbour_out" and not town.visited:
            start_r, start_g, start_b = 255, 0, 0
            end_r, end_g, end_b = 10, 0, 0
    elif type == "terminal":
        start_r, start_g, start_b = 10, 0, 0
        end_r, end_g, end_b = 255, 255, 255
    else:
        return

    steps = 50  # Number of steps in the fade
    delay = 0.02  # Delay between each step (in seconds)

    for i in range(steps + 1):
        # Calculate the current RGB values for this step
        r = int(start_r + (end_r - start_r) * (i / steps))
        g = int(start_g + (end_g - start_g) * (i / steps))
        b = int(start_b + (end_b - start_b) * (i / steps))

        for led in town.leds:
            strip[led] = (r, g, b)
        strip.show()
        utime.sleep(delay)

# Function to pick two different random towns
def pick_towns(towns):
    town1 = random.choice(towns)
    town2 = random.choice(towns)
    while town2 == town1:
        town2 = random.choice(towns)
    return town1, town2

# Function to get the euclidean distance between two towns when given x and y coordinates of each
def get_distance(town1, town2):
    return ((town1.x - town2.x) ** 2 + (town1.y - town2.y) ** 2) ** 0.5

# Function to get the town with the smallest distance that has not been visited
def get_smallest_distance(towns):
    smallest_distance = 9999
    smallest_town = None
    for town in towns:
        if not town.visited and town.distance < smallest_distance:
            smallest_distance = town.distance
            smallest_town = town
    return smallest_town


def dijkstras(towns, stop_callback):
    while True:
        if stop_callback():
            return
        for town in towns:
            town.visited = False
            town.distance = 9999
            town.previous = None

        for i in range(numpix):
            strip[i] = (10, 0, 0)
        strip.show()

        # Pick two towns
        start_town, end_town = pick_towns(towns)
        

        # Set distance of start town to 0
        start_town.distance = 0

        # Fade in the start and end towns
        utime.sleep(1)
        fade("terminal", start_town)
        fade("terminal", end_town)
        utime.sleep(1)

        # Set the current town to the start town
        current_town = start_town

        while True:
            if stop_callback():
                return
            # Set current path to an empty list
            current_path = []

            # Generate the path from the start town to the current town
            stepping_town = current_town
            current_path.append(stepping_town)
            while stepping_town.previous:
                current_path.append(stepping_town.previous)
                stepping_town = stepping_town.previous

            # Reverse the path so it goes from the start town to the current town
            current_path.reverse()

            # Fade in the path from the start town to the current town
            for town in current_path:
                if stop_callback():
                    return
                fade("in", town, start_town, end_town)
            current_path.reverse()

            # If the current town is the end town, reset the towns
            # and break the loop
            if current_town == end_town:
                utime.sleep(5)
                break

            # Get the neighbours of the current town and fade them in red
            for neighbour in current_town.neighbours:
                if stop_callback():
                    return
                if not neighbour.visited:
                    fade("neighbour_in", neighbour, start_town, end_town)

            # Calculate the distance from the start town to each neighbour
            # and update the distance if it is less than the current distance
            for neighbour in current_town.neighbours:
                if not neighbour.visited:
                    distance = get_distance(current_town, neighbour)
                    if neighbour.distance > current_town.distance + distance:
                        neighbour.distance = current_town.distance + distance
                        neighbour.set_previous(current_town)

            # Mark the current town as visited
            current_town.visited = True

            # Fade out the neighbours back to pale red
            for neighbour in current_town.neighbours:
                if stop_callback():
                    return
                if not neighbour.visited:
                    fade("neighbour_out", neighbour, start_town, end_town)

            # Fade out the path back to the start town
            for town in current_path:
                if stop_callback():
                    return
                fade("out", town, start_town, end_town)
            utime.sleep(1)

            # Find the town with the smallest distance that has not been visited 
            # and set it as the current town
            current_town = get_smallest_distance(towns)











