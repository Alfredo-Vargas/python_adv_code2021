# Advent of Code 2021

# Day 10 part 1 and 2

print(" ")
print("----------------------------------------")
print("For day 10 Part 1")
chunks = []

with open("./data/day10.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        chunks.append(line.rstrip())

corrupted_chunks = []
print(chunks)

for chunk in chunks:
    chunk_dict = {"(": 0, ")": 0, "[": 0, "]": 0, "{": 0, "}": 0, "<": 0, ">": 0}
    for char in chunk:
        chunk_dict[char] += 1
    print(chunk_dict)
    if (
        chunk_dict["("] < chunk_dict[")"]
        or chunk_dict["["] < chunk_dict["]"]
        or chunk_dict["{"] < chunk_dict["}"]
        or chunk_dict["<"] < chunk_dict[">"]
    ):
        corrupted_chunks.append(chunk)

print(corrupted_chunks)
