# Advent of Code 2021

# Day 15 part 1 and 2
import sys
import numpy as np
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else 'please input the 15 day data'

# read contents
pre_map = []
for line in open(file):
    row = [int(x) for x in line.rstrip()]
    pre_map.append(row)

# store the contents on a 2x2 matrix
risk_map = np.zeros((len(pre_map), len(pre_map[0])), dtype=int)
for i in range(len(pre_map)):
    risk_map[i, :] = pre_map[i]

n_rows = len(risk_map[:, 0]) - 1
n_cols = len(risk_map[0, :]) - 1
number_of_moves = n_rows + n_cols
# print(f"\nNumber of moves is {number_of_moves}")

def sum_after_n_steps(px, py, current_sum, steps):
    root_node = (px, py, current_sum)
    Q = deque([root_node])
    total_nodes = 2 ** steps
    # print(f"\nThe number of nodes is: {total_nodes}")
    while len(Q) < total_nodes:
        node = Q.popleft()  # LIFO operation pretty common on Queue data structures (deque)
        right_node, down_node = bifurcate(node)
        Q.append(down_node)
        Q.append(right_node)

    min_sum = Q[0][2]  # first node and third value (current_sum)
    # print(min_sum)
    for i in range(1, len(Q), 1):
        if min_sum > Q[i][2]:
            min_sum = Q[i][2]
    return min_sum

# TODO: Need to include edge cases
def bifurcate(node):
    px, py, current_sum = node[0], node[1], node[2]
    if px < n_cols and py < n_rows:  # not any boundary
        rsum = current_sum + risk_map[px, py + 1]
        dsum = current_sum + risk_map[px + 1, py]
        return ((px, py + 1, rsum), (px + 1, py, dsum))
    elif px < n_cols and py == n_rows:  # we reach the right wall
        dsum = current_sum + risk_map[px + 1, py]  # we can only go down
        return ((px + 1, py, dsum), (px + 1, py, dsum))
    elif px == n_cols and py < n_rows:  # we reach the bottom wall
        rsum = current_sum + risk_map[px, py + 1]  # we can only go right
        return ((px, py + 1, rsum), (px, py + 1, rsum))
    else:
        return ((n_cols, n_rows, current_sum), (n_cols, n_rows, current_sum))

i, j = 0, 0
path_value = 0
number_of_moves = 198
while number_of_moves > 0:
    if i < n_rows and j < n_cols:
        n_steps = 19  # how much ahead will you explore
        right_sum = sum_after_n_steps(i, j + 1, path_value + risk_map[i, j + 1], n_steps)
        down_sum = sum_after_n_steps(i + 1, j, path_value + risk_map[i + 1, j], n_steps)

        if right_sum < down_sum:
            j += 1  # we walk right
        elif down_sum < right_sum: 
            i += 1  # we walk down
        else:
            # print("Ambiguity found when choosing a path")
            if risk_map[i, j + 1] < risk_map[i + 1, j]:
                j += 1
            elif risk_map[i, j + 1] < risk_map[i + 1, j]:
                i += 1
            else:
                # print("Super ambiguity detected")
                i += 1

    elif i == n_cols and j != n_rows:
        j = j + 1  # we can only walk down
    elif i != n_cols and j == n_rows:
        i = i + 1  # we can only wak right
    path_value += risk_map[i, j]
    number_of_moves -= 1
    # print(f"--------  Move # {14 - number_of_moves}  ----------------------")
    # print(f"At point ({i}, {j}) the path value is : {path_value}")

print(f"At point ({i}, {j}) the path value is : {path_value}")

# Wrong Answers:
# 810  # Too high
# 704  # Too high
# 702  # Too high

# The above code is not able to calculate for n_steps larger takes too much time!
# FAILED
