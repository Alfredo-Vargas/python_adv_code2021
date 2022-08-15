# Advent of Code 2021

# Day 14 part 1 and 2
import sys
from collections import defaultdict, Counter

file = sys.argv[1] if len(sys.argv) > 1 else 'please input the 14 day data'
file_content = open(file)

# Data structures to be used
insertion_rules = defaultdict(str)

# Reading data
template = file_content.readline().rstrip()
file_content.readline()

for line in file_content:
    temp_key, temp_value = line.rstrip().split('->')
    key, value = temp_key.rstrip(), temp_value.lstrip()
    insertion_rules[key] = value

polymer = list(template)
N = 10  # number of iterations
for _ in range(N):
    temp_polymer = polymer.copy()
    for i in range(len(polymer) - 1):
        key = polymer[i] + polymer[i + 1]
        value = insertion_rules[key]
        temp_polymer.insert(2 * i + 1, value)
    polymer = temp_polymer
    print("".join(polymer))

# frequency_counter = dict(Counter(polymer))
#
# max_value = max(frequency_counter.values())
# min_value = min(frequency_counter.values())
#
# print(max_value - min_value)
