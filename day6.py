# Advent of Code 2021
import numpy as np
# import time

# Day 6 part 1

# Dictionary to hash the possible values of the given input
lanterfish_dict = {}

with open("./data/day6.txt", "r") as file:
    char_lanterfishes = file.readline().rstrip().split(",")
    lanterfishes = np.array([int(x) for x in char_lanterfishes])
    # we create the keys on the dictionary for every unique given input
    for i in range(8):  # highest possible value for each fish is 8
        lanterfish_dict[i] = 0
    for key in lanterfish_dict:
        lanterfish_dict[key] = sum(x == key for x in lanterfishes)

ndays = 256

for _ in range(ndays):
    # We create a new dictionary every day and update with accumulative values
    new_lanterfish_dict = {}
    for i in range(9):  # highest possible value for each fish is 8
        new_lanterfish_dict[i] = 0
    for key in lanterfish_dict:
        if key == 0:  # we update with respect to the the previous values
            new_lanterfish_dict[6] += lanterfish_dict[key]
            new_lanterfish_dict[8] += lanterfish_dict[key]
        else:
            new_lanterfish_dict[key - 1] += lanterfish_dict[key]
    lanterfish_dict = new_lanterfish_dict

s = 0
for key in lanterfish_dict:
    s += lanterfish_dict[key]

print(s)

# DON'T USE LONG LISTS/ARRAYS OR LONG RECURSIONS ON THIS PROBLEM
# THE MEMORY LOAD BECOMES TO BIG AND TOO SLOW
# THE ATTEMPTS BELOW FAILED MISERABLY FOR PART II

# nlf = number of lanternfish, nd = number of days
# def nlf(ndays, value):
#     # Break condition of recursion
#     if ndays <= value:
#         return 0
#     else:
#         return 1 + nlf(ndays - value - 1, 6) + nlf(ndays - value - 1, 8)
# counter = 0
# for i in range(len(lanterfishes)):
#     counter += nlf(ndays, lanterfishes[i])
# print("Using the \"nlf\" function:")
# print(counter + len(lanterfishes))


# start_time = time.time()
# for i in range(ndays):
#     nnb = sum([x == 0 for x in lanterfishes])  # number of newborns
#     new_borns = np.ones(nnb) * 8
#     lanterfishes = lanterfishes - 1
#     lanterfishes = np.where(lanterfishes < 0, 6, lanterfishes)
#     lanterfishes = np.append(lanterfishes, new_borns, 0)
#     print(f"After {i + 1} day: {lanterfishes}")
#
# print(f"Brute execution took {time.time() - start_time} seconds")
# print(f"We have {len(lanterfishes)} lanterfishes after {ndays} days.")
