# Advent of Code 2021

# Day 11 part 1 and 2
import math
import numpy as np

print(" ")
print("----------------------------------------")
print("For day 11 Part 1")

# We add -infinity to the border lines so it will never flash as an octopus
# Another matrix with the same dimension will keep track if they flashed
with open("./data/day11.txt", "r") as file:
    lines = file.readlines()
    octopuses_energy = np.ones((len(lines) + 2, len(lines[0].strip()) + 2))
    temp_matrix = np.ones((len(lines) + 2, len(lines[0].strip()) + 2))
    octopuses_flashed = temp_matrix != 1
    octopuses_energy[0, :] = -math.inf
    octopuses_energy[len(lines) + 1, :] = -math.inf
    octopuses_energy[:, 0] = -math.inf
    octopuses_energy[:, len(lines) + 1] = -math.inf
    for i in range(len(lines)):
        temp_list = [int(char) for char in lines[i].rstrip()]
        octopuses_energy[i + 1, 1:-1] = np.array(temp_list)


def adjacent_interaction():
    for i in range(1, len(octopuses_energy[:, 0]) - 1, 1):
        for j in range(1, len(octopuses_energy[0, :]) - 1, 1):
            flashed = octopuses_flashed[i, j]
            current_energy = octopuses_energy[i, j]
            if not flashed and current_energy > 9:
                octopuses_energy[i - 1][j - 1] += 1
                octopuses_energy[i - 1][j] += 1
                octopuses_energy[i - 1][j + 1] += 1
                octopuses_energy[i][j - 1] += 1
                octopuses_energy[i][j + 1] += 1
                octopuses_energy[i + 1][j - 1] += 1
                octopuses_energy[i + 1][j] += 1
                octopuses_energy[i + 1][j + 1] += 1
                octopuses_flashed[i, j] = True


flash_counters = []
for _ in range(2):
    octopuses_energy += 1  # we start by adding one to every octopus
    # get coordinates of the points with energy > 9
    (x, y) = np.where((octopuses_energy > 9))
    print(x, y)
    # DO WHILE ENERGY VALUES ARE > 9 AND FLASHED IS FALSE
    # iterate over those coordinates
    # update the energy values and flash states

    # adjacent_interaction()
    # print(f"The point is: {i}, {j} with value {octopuses_energy[i, j]}")
    # octopuses_energy[octopuses_energy > 9] = 0
    # octopuses_flashed[octopuses_flashed == True] = False  # reset flash state

print(octopuses_energy)
# All loops must run from 1, to 10 (borders are minus infinity)
