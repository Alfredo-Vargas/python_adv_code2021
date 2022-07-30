# Advent of Code 2021

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
        if len(seg) == 2 or len(seg) == 4 or len(seg) == 3 or len(seg) == 7:
            counter += 1

print(f"Answer for Part 1 is: {counter}")
print(" ")
print("----------------------------------------")
print("For day 8 Part 2")


def get_numbers_dict(unique_pattern):
    numbers_dict = {}
    pre_one = "".join(filter(lambda x: len(x) == 2, unique_pattern))
    pre_seven = "".join(filter(lambda x: len(x) == 3, unique_pattern))
    pre_four = "".join(filter(lambda x: len(x) == 4, unique_pattern))
    six_segments_nums = list(filter(lambda x: len(x) == 6, unique_pattern))
    five_segments_nums = list(filter(lambda x: len(x) == 5, unique_pattern))
    one = "".join(sorted(pre_one))
    seven = "".join(sorted(pre_seven))
    four = "".join(sorted(pre_four))
    numbers_dict[one] = "1"
    numbers_dict[seven] = "7"
    numbers_dict[four] = "4"
    numbers_dict["abcdefg"] = "8"

    auxiliar = four[:]
    for char in one:
        auxiliar = auxiliar.replace(char, "", 1)

    # Digits of six segments
    for digit in six_segments_nums:
        contains_one = False
        contains_auxiliar = False
        if one[0] in digit and one[1] in digit:
            contains_one = True
        if auxiliar[0] in digit and auxiliar[1] in digit:
            contains_auxiliar = True
        if contains_one and contains_auxiliar:
            nine = "".join(sorted(digit))
            numbers_dict[nine] = "9"
        elif not contains_one and contains_auxiliar:
            six = "".join(sorted(digit))
            numbers_dict[six] = "6"
        else:
            zero = "".join(sorted(digit))
            numbers_dict[zero] = "0"

    # Digits of five segments
    for digit in five_segments_nums:
        contains_one = False
        contains_auxiliar = False
        if one[0] in digit and one[1] in digit:
            contains_one = True
        if auxiliar[0] in digit and auxiliar[1] in digit:
            contains_auxiliar = True
        if contains_one:
            three = "".join(sorted(digit))
            numbers_dict[three] = "3"
        elif contains_auxiliar:
            five = "".join(sorted(digit))
            numbers_dict[five] = "5"
        else:
            two = "".join(sorted(digit))
            numbers_dict[two] = "2"
    print(numbers_dict)


get_numbers_dict(unique_patterns[0])
get_numbers_dict(unique_patterns[1])
given_pattern = [
    "acedgfb",
    "cdfbe",
    "gcdfa",
    "fbcad",
    "dab",
    "cefabd",
    "cdfgeb",
    "eafb",
    "cagedb",
    "ab",
]
get_numbers_dict(given_pattern)
# siete = "zabscdve"
# uno = "sv"
# for char in uno:
#     siete = siete.replace(char, "", 1)
#
# print(siete)
