# Advent of Code 2021
import numpy as np

# Day 8 part 1 and 2

print(" ")
print("----------------------------------------")
print("For day 8 Part 1")

unique_patterns = []
output_values = []

with open("./data/day8.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        signals = line.rstrip().split("|")
        unique_patterns.append(signals[0].split())
        output_values.append(signals[1].split())


# Solution for Part 1
counter = 0
for output in output_values:
    for seg in output:
        if (len(seg) == 2 or len(seg) == 4 or len(seg) == 3 or len(seg) == 7):
            counter += 1

print(counter)
print(" ")
print("----------------------------------------")
print("For day 8 Part 2")
