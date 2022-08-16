# Advent of Code 2021

# Day 14 part 1 and 2
import sys
import math
from collections import defaultdict, Counter

file = sys.argv[1] if len(sys.argv) > 1 else 'please input the 14 day data'
file_content = open(file)

# Data structures to be used
insertion_rules = defaultdict(str)

# Reading data
template = file_content.readline().rstrip()
file_content.readline()

answer = defaultdict(int)
for line in file_content:
    temp_key, temp_value = line.rstrip().split('->')
    key, value = temp_key.rstrip(), temp_value.lstrip()
    insertion_rules[key] = value
    answer[value] = 0


# INSIGHT:
# Every pair of letters produce two pair of letters!!!
# It is better to change the insertion rules to duplication rules

duplication_rules = defaultdict(tuple)
pair_counter = defaultdict(int)
for rule in insertion_rules:
    a = rule[0] + insertion_rules[rule]
    b = insertion_rules[rule] + rule[1]
    duplication_rules[rule] = (a, b)
    pair_counter[rule] = 0

# Initialize pair counter with given template
polymer = list(template)
for i in range(len(polymer) - 1):
    pair = polymer[i] + polymer[i + 1]
    pair_counter[pair] += 1

N = 40
for i in range(N):
    temp_counter = pair_counter.copy()
    for pair in temp_counter:
        if temp_counter[pair] != 0:
            temp_value1 = duplication_rules[pair][0]
            temp_value2 = duplication_rules[pair][1]
            pair_counter[temp_value1] += temp_counter[pair]
            pair_counter[temp_value2] += temp_counter[pair]
            pair_counter[pair] -= temp_counter[pair]
    # print(f"The number of pairs after {i+1}th iteration:")
    # print(pair_counter)


# We calculate the number of letters
for letter in answer:
    for pair in pair_counter:
        if letter in pair:
            if letter + letter != pair:
                answer[letter] += pair_counter[pair]
            else:
                answer[letter] += 2 * pair_counter[pair]

final_answer = list(answer.values())

# A pair in the pair_counter doubles the correct value
print(math.ceil(max(final_answer) / 2)  - math.ceil(min(final_answer) / 2))

