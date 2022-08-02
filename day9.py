# Advent of Code 2021

# Day 9 part 1 and 2
import numpy as np

# TODO: Improvements: Use dummy values to avoid edge cases
# Because we look for the minima a border of values with 10 will do it!
print(" ")
print("----------------------------------------")
print("For day 9 Part 1")

with open("./data/day9.txt", "r") as file:
    lines = file.readlines()
    nrows, ncols = len(lines), len(lines[0].rstrip())
    terrain = np.zeros((nrows, ncols), dtype=np.int64)
    for i in range(len(lines)):
        row = list(lines[i].rstrip())
        row = [int(x) for x in row]
        terrain[i, :] = np.array(row)

minima_coordinates = []

# Upper Left Corner
if terrain[0, 0] < terrain[0, 1] and terrain[0, 0] < terrain[1, 0]:
    minima_coordinates.append((0, 0))
# Upper Right Corner
if (
    terrain[0, ncols - 1] < terrain[0, ncols - 2]
    and terrain[0, ncols - 1] < terrain[1, ncols - 1]
):
    minima_coordinates.append((0, ncols - 1))
# Lower Left Corner
if (
    terrain[nrows - 1, 0] < terrain[nrows - 1, 1]
    and terrain[nrows - 1, 0] < terrain[98, 0]
):
    minima_coordinates.append((nrows - 1, 0))
# Lower Right Corner
if (
    terrain[nrows - 1, ncols - 1] < terrain[nrows - 2, ncols - 1]
    and terrain[nrows - 1, ncols - 1] < terrain[nrows - 1, ncols - 2]
):
    minima_coordinates.append((nrows - 1, ncols - 1))
# Top edge without corners
for i in range(1, len(terrain[0, :]) - 1, 1):
    if (
        terrain[0, i] < terrain[0, i - 1]
        and terrain[0, i] < terrain[0, i + 1]
        and terrain[0, i] < terrain[1, i]
    ):
        minima_coordinates.append((0, i))
# Bottom edge without corners
for i in range(1, len(terrain[0, :]) - 1, 1):
    if (
        terrain[nrows - 1, i] < terrain[nrows - 1, i - 1]
        and terrain[nrows - 1, i] < terrain[nrows - 1, i + 1]
        and terrain[nrows - 1, i] < terrain[nrows - 2, i]
    ):
        minima_coordinates.append((nrows - 1, i))
# Left edge without corners
for i in range(1, len(terrain[:, 0]) - 1, 1):
    if (
        terrain[i, 0] < terrain[i - 1, 0]
        and terrain[i, 0] < terrain[i + 1, 0]
        and terrain[i, 0] < terrain[i, 1]
    ):
        minima_coordinates.append((i, 0))
# Right edge without corners
for i in range(1, len(terrain[:, 0]) - 1, 1):
    if (
        terrain[i, ncols - 1] < terrain[i - 1, ncols - 1]
        and terrain[i, ncols - 1] < terrain[i + 1, ncols - 1]
        and terrain[i, ncols - 1] < terrain[i, ncols - 2]
    ):
        minima_coordinates.append((i, ncols - 1))
# No edge cases
for i in range(1, len(terrain[:, 0]) - 1, 1):
    for j in range(1, len(terrain[0, :]) - 1, 1):
        if (
            terrain[i, j] < terrain[i - 1, j]
            and terrain[i, j] < terrain[i, j + 1]
            and terrain[i, j] < terrain[i + 1, j]
            and terrain[i, j] < terrain[i, j - 1]
        ):
            minima_coordinates.append((i, j))

total_risk = 0
for coordinate in minima_coordinates:
    x, y = coordinate[0], coordinate[1]
    total_risk += terrain[x, y] + 1

print(f"The sum of all risk levels is: {total_risk}")

print("----------------------------------------")
print("For day 9 Part 2")

basins_sizes = []


# We will implement breadth-first search algorithm (BFS)
def breadth_first_search(coordinate, nrows, ncols):
    x, y = coordinate[0], coordinate[1]
    global basin_size
    global trilha
    # Discovering Left
    while (
        y > 0
        and y < ncols  # can explore left
        and terrain[x, y - 1] > terrain[x, y]  # the  left one is larger
        and terrain[x, y - 1] != 9  # nine is not included
    ):
        trilha.add((x, y - 1))
        breadth_first_search((x, y - 1), nrows, ncols)  # recursively discover
        break

    # Discovering Right
    while (
        y >= 0
        and y < ncols - 1  # can explore right
        and terrain[x, y + 1] > terrain[x, y]  # the  right one is larger
        and terrain[x, y + 1] != 9  # nine is not included
    ):
        trilha.add((x, y + 1))
        breadth_first_search((x, y + 1), nrows, ncols)  # recursively discover
        break

    # Discovering Above
    while (
        x > 0
        and x < nrows  # can explore above
        and terrain[x - 1, y] > terrain[x, y]  # the above one is larger
        and terrain[x - 1, y] != 9  # nine is not included
    ):
        trilha.add((x - 1, y))
        breadth_first_search((x - 1, y), nrows, ncols)
        break

    # Discovering Below
    while (
        x >= 0
        and x < nrows - 1  # can explore below
        and terrain[x + 1, y] > terrain[x, y]  # the above one is larger
        and terrain[x + 1, y] != 9  # nine is not included
    ):
        trilha.add((x + 1, y))
        breadth_first_search((x + 1, y), nrows, ncols)
        break


for minimum in minima_coordinates:
    trilha = {minimum}  # this global variable gets overwritten every iteration
    breadth_first_search(minimum, nrows, ncols)
    basins_sizes.append(len(trilha))

reversed_basins_sizes = sorted(basins_sizes, reverse=True)
a = reversed_basins_sizes[0]
b = reversed_basins_sizes[1]
c = reversed_basins_sizes[2]
print(f"The multiplication of the three highest values is: {a * b * c}")
print("----------------------------------------")
