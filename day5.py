# Advent of Code 2021
import numpy as np

# Day 5 part 1 and 2 (Comment/Uncommnet lines 45, 51)

# Field of hydrothermal vents
field = np.zeros((1000, 1000))

# List of Segments where each segment contains points
segments = []


# Function to retrieve a segment (list of points) given the extreme points
def get_segment(p1, p2):
    segment = []
    # Segment points when only x is constant
    if p1[0] == p2[0] and p1[1] != p2[1]:
        for i in range(min(p1[1], p2[1]), max(p2[1], p1[1]) + 1, 1):
            segment.append(((p1[0]), i))
    # Segment points when only y is constant
    elif p1[0] != p2[0] and p1[1] == p2[1]:
        for i in range(min(p1[0], p2[0]), max(p2[0], p1[0]) + 1, 1):
            segment.append((i, p1[1]))
    # Segment with a single point (not really a segment but a point)
    elif p1[0] == p2[0] and p1[1] == p2[1]:
        segment.append((p1[0], p1[1]))
    # General case when the line is diagonal
    else:
        print("Diagonal line detected")
        a = (p1[1] - p2[1]) / (p1[0] - p2[0])
        b = (p1[0] * p2[1] - p1[1] * p2[0]) / (p1[0] - p2[0])
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1, 1):
            y = a * x + b
            segment.append((x, y))
    return segment


# We load the pair of coordinates to define the line (finite segment)
with open("./data/day5.txt", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        points = line.split(" -> ")
        pre_p1, pre_p2 = points[0].split(","), points[1].split(",")
        p1, p2 = [int(x) for x in pre_p1], [int(x) for x in pre_p2]
        # For part one only vertical and horizontal lines are considered, then
        # if p1[0] == p2[0] or p1[1] == p2[1]:
        #     segment = get_segment(p1, p2)
        #     segments.append(segment)

        # For part two also diagonals at 45 degrees are considered
        if p1[0] != p2[0] and p1[1] != p2[1]:
            a = abs((p1[1] - p2[1]) / (p1[0] - p2[0]))
        else:
            a = 0
        if p1[0] == p2[0] or p1[1] == p2[1] or a == 1:
            segment = get_segment(p1, p2)
            segments.append(segment)

for segment in segments:
    for point in segment:
        print(point)
        field[int(point[0]), int(point[1])] += 1

flatten_output = field.flatten()
print(len(flatten_output))

dangerous_areas = sum(x > 1 for x in flatten_output)
print(dangerous_areas)

# Answer Part 1: 6007
# Answer Part 2: 19349
