# Advent of Code 2021

# Day 14 part 1 and 2
import sys
from collections import defaultdict, Counter

file = sys.argv[1] if len(sys.argv) > 1 else 'please input the 14 day data'
risk_map = []
for line in open(file):
    row = [int(x) for x in line.rstrip()]
    risk_map.append(row)
