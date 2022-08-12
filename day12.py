# Only manage to solve first part, for second part took inspiration from:
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/12.py
# Advent of Code 2021

# Day 12 part 1 and 2
import sys
from collections import defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else '12.in'

# if issubclass(defaultdict, dict):
#     print("defaultdict is a subclass of a dictionary")

# DEFAULT DICTIONARIES
# The default values of non defined keys will be callable such int, float, list, set, ...
# Whenever a key is passed that was not previously defined with its value
# The key will automatically be created with a value equal to the given default callable
# INSIGHT: A dictionary key can have a list as value!!! 

# adjacent list - for each vertex, what vertices does it have edgest to?
next_steps = defaultdict(list)
for line in open(file):
    a,b = line.rstrip().split('-')
    next_steps[a].append(b)
    next_steps[b].append(a)


start = ('start', set(['start']), None)
ans = 0
# We initialize or deck!
# Every value on our deck is a tuple containing current position, neighbors and wether it has visited twice
Q = deque([start])
while Q:
    current_position, current_path, is_visited_twice = Q.popleft()  # the next step
    if current_position == 'end':
        ans += 1
        continue
    # we iterate over the list that contains the adjacent points to the current position
    for position in next_steps[current_position]:
        if position not in current_path:
            new_path = set(current_path)
            if position.lower() == position:
                new_path.add(position)
            Q.append((position, new_path, is_visited_twice))
        elif position in current_path and is_visited_twice is None and position not in ['start', 'end']:
            Q.append((position, current_path, position))

print(ans)
