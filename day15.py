# Advent of Code 2021

# Day 14 part 1 and 2
import sys
import numpy as np

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
print(f"Number of moves is {number_of_moves}")

def next_sum(px, py, current_sum):
    if (px > n_cols or py > n_rows):
        return (0, 0)
    elif px == n_cols and py == n_rows:
        answer = current_sum + risk_map[n_rows, n_cols]
        return (answer, answer)
    elif px == n_cols and py < n_rows:
        down_sum = current_sum + risk_map[px + 1, py]
        return (999, down_sum)
    elif px < n_cols and py == n_rows:
        right_sum = current_sum + risk_map[px, py + 1]
        return (right_sum, 999)
    else:
        right_sum = current_sum + risk_map[px, py + 1]
        down_sum = current_sum + risk_map[px + 1, py]
        return (right_sum, down_sum)


def explore_path(i, j, path_value):
    r, d = next_sum(i, j, path_value)

    rr, rd = next_sum(i, j + 1, r)
    dr, dd = next_sum(i + 1, j, d)

    rrr, rrd = next_sum(i, j + 2, rr)
    drr, drd = next_sum(i + 1, j + 1, rd)
    rdr, rdd = next_sum(i + 1, j + 1, dr)
    ddr, ddd = next_sum(i + 2, j, dd)

    minimum = min(rrr, rrd, drr, drd, rdr, rdd, ddr, ddd)
    right_list = [rrr, rrd, drr, drd]
    down_list = [rdr, rdd, ddr, ddd]

    if minimum in right_list and minimum in down_list:
        return "ambiguous"
    elif minimum in right_list:
        return "right"
    else:
        return "down"

i, j = 0, 0
path_value = 0
# number_of_moves = 10  # do for max - 2 to avoid getting out of the grid 
while number_of_moves > 0:
    if i < n_rows and j < n_cols:
        direction = explore_path(i, j, path_value)
        if direction == "ambigous":
            print("Is ambiguous")
            break
        if direction == "right":
            j = j + 1  # we walk right
        else:
            i = i + 1  # we walk down
    elif i == n_cols and j != n_rows:
        j = j + 1  # we can only walk down
    elif i != n_cols and j == n_rows:
        i = i + 1  # we can only wak right
    path_value += risk_map[i, j]
    number_of_moves -= 1
    print("------------------------------")
    print(f"At point ({i}, {j}) the path value is : {path_value}")
    if i == n_rows and j == n_cols:
        break

print(path_value)

# Wrong Answer:
# 810  # Too high

# def cummulative_sum(px, py, n_rows, n_cols):
#     # calculates the cummulative sum two steps ahead
#     if (px < n_rows - 1 and py < n_cols - 1):
#         rr = risk_map[px, py] + risk_map[px + 1, py] + risk_map[px + 2, py]
#         rd = risk_map[px, py] + risk_map[px + 1, py] + risk_map[px + 1, py + 1]
#         dr = risk_map[px, py] + risk_map[px, py + 1] + risk_map[px + 1, py + 1]
#         dd = risk_map[px, py] + risk_map[px, py + 1] + risk_map[px, py + 2]
#         return min(rr, rd, dr, dd)
#     elif (px < n_rows and py < n_cols - 1):
#         rd = risk_map[px, py] + risk_map[px + 1, py] + risk_map[px + 1, py + 1]
#         dr = risk_map[px, py] + risk_map[px, py + 1] + risk_map[px + 1, py + 1]
#         dd = risk_map[px, py] + risk_map[px, py + 1] + risk_map[px, py + 2]
#         return min(rd, dr, dd)
#     elif (px < n_rows and py < n_cols):
#         rd = risk_map[px, py] + risk_map[px + 1, py] + risk_map[px + 1, py + 1]
#         dr = risk_map[px, py] + risk_map[px, py + 1] + risk_map[px + 1, py + 1]
#         return min(rd, dr)
#     elif (px < n_rows - 1 and py < n_cols):
#         rr = risk_map[px, py] + risk_map[px + 1, py] + risk_map[px + 2, py]
#         rd = risk_map[px, py] + risk_map[px + 1, py] + risk_map[px + 1, py + 1]
#         dr = risk_map[px, py] + risk_map[px, py + 1] + risk_map[px + 1, py + 1]
#         return min(rr, rd, dr)
#     elif (px == n_rows):
#         if py < n_cols - 1:
#             dd = risk_map[px, py] + risk_map[px, py + 1] + risk_map[px, py + 2]
#         elif py < n_cols:
#             dd = risk_map[px, py] + risk_map[px, py + 1]  # check only one step ahead!
#         return dd
#     elif (py == n_cols):
#         if px < n_rows - 1:
#             rr = risk_map[px, py] + risk_map[px + 1, py] + risk_map[px + 2, py]
#         elif px < n_rows:
#             rr = risk_map[px, py] + risk_map[px + 1, py]  # check only one step ahead
#         return rr

# def next_sum(px, py):
#     if px == n_cols and py == n_rows:
#         return 0
#     if px < n_cols and py < n_rows:
#         sum_right = risk_map[px, py] + risk_map[px + 1, py]
#         sum_down = risk_map[px, py] + risk_map[px, py + 1]
#         if sum_right <= sum_down:
#             return sum_right + next_sum(px + 1, py)
#         else:
#             return sum_down + next_sum(px, py + 1)
#     elif px < n_cols and py == n_rows:
#         sum_right = risk_map[px, py] + risk_map[px + 1, py]
#         return sum_right + next_sum(px + 1, py)
#     elif px == n_cols and py < n_rows:
#         sum_down = risk_map[px, py] + risk_map[px, py + 1]
#         return sum_down + next_sum(px, py + 1)
#
