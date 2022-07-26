# Advent of Code 2021

# Day 3 part 1
# Rates
gamma_rate_str = ""
epsilon_rate_str = ""

# The operations are commutative, so we can counter the commands values
# regardless of the order of the commands
gamma = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "11": 0,
}

epsilon = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "11": 0,
}

input_length = 0

with open("./data/day3.txt", "r") as file:
    lines = file.read().splitlines()
    input_length = len(lines)
    for line in lines:
        for i in range(len(line)):
            if (int(line[i])) == 0:
                gamma[str(i)] += 1


for key in gamma.keys():
    if (gamma[key]) >= input_length / 2:
        gamma[key] = 0
        epsilon[key] = 1
    else:
        gamma[key] = 1
        epsilon[key] = 0

for value in gamma.values():
    gamma_rate_str += str(value)

for value in epsilon.values():
    epsilon_rate_str += str(value)

print(int(gamma_rate_str, base=2) * int(epsilon_rate_str, base=2))
print("")

# Day 3 part 2
# Ratings
generator_rating = 0
scrubber_rating = 0

# generator_list = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010"
#     ]
#
# scrubber_list = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010"
#     ]
generator_list = []
scrubber_list = []

with open("./data/day3.txt", "r") as file:
    lines = file.read().splitlines()
    generator_list = lines.copy()
    scrubber_list = lines.copy()


def getCommonAtPos(given_list, pos):
    most_common_bit = ""
    zeros_counter = 0
    ones_counter = 0
    for line in given_list:
        if line[pos] == "0":
            zeros_counter += 1
        else:
            ones_counter += 1
    if (zeros_counter > ones_counter):
        most_common_bit = "0"
    elif (zeros_counter < ones_counter):
        most_common_bit = "1"
    else:
        most_common_bit = "e"
    return most_common_bit


# Keep most common calculation
for i in range(len(lines[0])):  # loop over single number length
    if (len(generator_list) == 1):
        break
    # print(f"For position: {i}")
    filtered1 = []
    most_common_bit = getCommonAtPos(generator_list, i)
    # print(f"Most common bit is {most_common_bit}")
    if most_common_bit == "1" or most_common_bit == "e":
        filtered1 = list(filter(lambda x: (x[i] == '1'), generator_list))
        # print(filtered1)
    else:
        filtered1 = list(filter(lambda x: (x[i] == '0'), generator_list))
        # print(filtered1)
    generator_list = filtered1
    # print("The generator list is reduced to:")
    # print(generator_list)

# print("Final generator list")
# print(generator_list)
generator_rating = int(generator_list[0], base=2)
print(f"Generator in decimal is: {generator_rating}")
print("")

# Keep less common calculation
for i in range(len(lines[0])):  # loop over single number length
    if (len(scrubber_list) == 1):
        break
    filtered2 = []
    most_common_bit = getCommonAtPos(scrubber_list, i)
    if (most_common_bit == "1" or most_common_bit == "e"):
        filtered2 = list(filter(lambda x: (x[i] == '0'), scrubber_list))
    else:
        filtered2 = list(filter(lambda x: (x[i] == '1'), scrubber_list))
    scrubber_list = filtered2
    # print("The scrubber list is reduced to:")
    # print(scrubber_list)

# print("Final scrubber list")
# print(scrubber_list)
scrubber_rating = int(scrubber_list[0], base=2)
print(f"Scrubber in decimal is: {scrubber_rating}")
#
print(f"The life support is: {generator_rating * scrubber_rating}")
# Right answer is: 4 636 702
