# Advent of Code 2021

# Day 11 part 1 and 2
import math
import numpy as np

print(" ")
print("----------------------------------------")
print("For day 11 Part 1 and 2")
global flash_counter
flash_counter = 0

# We add -infinity to the border lines so it will never flash as an octopus
# Another matrix with the same dimension will keep track if they flashed
with open("./data/day11.txt", "r") as file:
    lines = file.readlines()
    nrows, ncols = len(lines) + 2, len(lines[0].rstrip()) + 2
    octopuses_energy = np.ones((nrows, ncols))
    octopuses_flashed = np.zeros((nrows, ncols), dtype=int)
    octopuses_energy[0, :] = -math.inf
    octopuses_energy[len(lines) + 1, :] = -math.inf
    octopuses_energy[:, 0] = -math.inf
    octopuses_energy[:, len(lines) + 1] = -math.inf
    for i in range(len(lines)):
        temp_list = [int(char) for char in lines[i].rstrip()]
        octopuses_energy[i + 1, 1:-1] = np.array(temp_list)


def adjacent_interaction(xpos, ypos):
    global flash_counter
    # Changed flashed to true immediately so inner recursion know about it
    octopuses_flashed[xpos, ypos] = 1
    flash_counter += 1
    neighbour_points = [
        (xpos - 1, ypos - 1),
        (xpos - 1, ypos),
        (xpos - 1, ypos + 1),
        (xpos, ypos - 1),
        (xpos, ypos + 1),
        (xpos + 1, ypos - 1),
        (xpos + 1, ypos),
        (xpos + 1, ypos + 1),
    ]

    for point in neighbour_points:
        if not octopuses_flashed[point[0], point[1]]:
            octopuses_energy[point[0], point[1]] += 1
            if octopuses_energy[point[0], point[1]] > 9:
                adjacent_interaction(point[0], point[1])


for index in range(1000):
    synched_number = np.count_nonzero(octopuses_energy == 0)
    if synched_number == 100:
        print(f"Synch happened at iteration: {index}")
        break

    octopuses_energy += 1  # we start by adding one to every octopus
    energetic_octopuses = np.argwhere(octopuses_energy > 9)

    for i in range(len(energetic_octopuses)):
        xpos = int(energetic_octopuses[i][0])
        ypos = int(energetic_octopuses[i][1])
        if octopuses_flashed[xpos, ypos] == 0:
            adjacent_interaction(xpos, ypos)
    octopuses_energy[octopuses_energy > 9] = 0
    octopuses_flashed = octopuses_flashed * 0

print(f"The number of flashes after {index} iterations is: {flash_counter}")
