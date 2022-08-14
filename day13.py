# Advent of Code 2021

# Day 13 part 1 and 2
import sys
import numpy as np

file = sys.argv[1] if len(sys.argv) > 1 else 'please input the 13 day data'

points = []
instructions = []
instructions_begin = False
for line in open(file):
    key = line.rstrip()
    if not instructions_begin:
        if len(key) != 0:
            a,b = key.split(',')
            points.append([int(a), int(b)])
        else:
            instructions_begin = True
            continue
    else:
        a,b = key.split('=')
        instructions.append((a[-1], int(b)))

def mirror_point(instruction, point):
    global x0_max, y0_max
    if instruction[0] == 'x':
        if point[0] > instruction[1]:
            point[0] = instruction[1] - (point[0] - instruction[1])
            x0_max = instruction[1]
    else:
        if point[1] > instruction[1]:
            point[1] = instruction[1] - (point[1] - instruction[1])
            y0_max = instruction[1]


for i in range(len(instructions)):
    if i == 1:
        answer_part1 = set()
        for point in points:
            temp_tuple = tuple(point)
            answer_part1.add(temp_tuple)
        print(f"The number of points after the first fold is: {len(answer_part1)}")
    for point in points:
        mirror_point(instructions[i], point)


answer_part2 = set()
max_x, max_y = 0, 0
for point in points:
    if point[0] > max_x:
        max_x = point[0]
    if point[1] > max_y:
        max_y = point[1]
    temp_tuple = tuple(point)
    answer_part2.add(temp_tuple)
print(f"Final paper dimensions are: {max_x} x {max_y}\n")


transparent_paper = np.chararray((max_x + 1, max_y + 1), unicode=True)
print(transparent_paper.shape)
for i in range(max_x + 1):
    for j in range(max_y + 1):
        if (i, j) in answer_part2:
            transparent_paper[i, j] = str('#')
        else:
            transparent_paper[i, j] = str('.')

np.set_printoptions(linewidth=160)
print(transparent_paper.transpose())

