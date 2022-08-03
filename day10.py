# Advent of Code 2021

# Day 10 part 1 and 2

print(" ")
print("----------------------------------------")
print("For day 10 Part 1")
chunks = []

with open("./data/day10.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        chunks.append([char for char in line.rstrip()])

simplified_chunks = []

for chunk in chunks:
    temp_chunk = chunk.copy()
    index = 0
    # We first remove consecutive openings and close brackets
    while index < (len(temp_chunk) - 1):
        is_parenth = temp_chunk[index] == "(" and temp_chunk[index + 1] == ")"
        is_square = temp_chunk[index] == "[" and temp_chunk[index + 1] == "]"
        is_curly = temp_chunk[index] == "{" and temp_chunk[index + 1] == "}"
        is_angle = temp_chunk[index] == "<" and temp_chunk[index + 1] == ">"
        if is_parenth or is_square or is_curly or is_angle:
            # Pop elements by index is a NON commutative operation!
            temp_chunk.pop(index + 1)
            temp_chunk.pop(index)
            index = index - 1
        else:
            index = index + 1
    simplified_chunks.append(temp_chunk)

illegals_dict = {")": 0, "]": 0, "}": 0, ">": 0}
for chunk in simplified_chunks:
    for i in range(1, len(chunk), 1):
        if chunk[i] == ")" and (
            chunk[i - 1] == "[" or chunk[i - 1] == "{" or chunk[i - 1] == "<"
        ):
            illegals_dict[")"] += 1
        elif chunk[i] == "]" and (
            chunk[i - 1] == "(" or chunk[i - 1] == "{" or chunk[i - 1] == "<"
        ):
            illegals_dict["]"] += 1
        elif chunk[i] == "}" and (
            chunk[i - 1] == "(" or chunk[i - 1] == "[" or chunk[i - 1] == "<"
        ):
            illegals_dict["}"] += 1
        elif chunk[i] == ">" and (
            chunk[i - 1] == "(" or chunk[i - 1] == "[" or chunk[i - 1] == "{"
        ):
            illegals_dict[">"] += 1

answer = (
    illegals_dict[")"] * 3
    + illegals_dict["]"] * 57
    + illegals_dict["}"] * 1197
    + illegals_dict[">"] * 25137
)
print(f"The total syntax error score is: {answer}")

print(" ")
print("----------------------------------------")
print("For day 10 Part 2")

legal_chunks = []
for chunk in simplified_chunks:
    if (
        ")" not in chunk
        and "]" not in chunk
        and "}" not in chunk
        and ">" not in chunk
    ):
        legal_chunks.append(chunk[::-1])  # we append in reverse order

scores = []
for chunk in legal_chunks:
    score = 0
    for element in chunk:
        score *= 5
        if element == "(":
            score += 1
        elif element == "[":
            score += 2
        elif element == "{":
            score += 3
        elif element == "<":
            score += 4
    scores.append(score)

sorted_scores = sorted(scores)
middle_score = sorted_scores[len(sorted_scores) // 2]
print(f"The middle score is {middle_score}")
