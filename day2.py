# Advent of Code 2021

# Day 2 part 1
# Relative position of the submarine with respect to the surface
horizontal_pos = 0
depth_pos = 0

# The operations are commutative, so we can counter the commands values
# regardless of the order of the commands
commands = {"forward": 0, "up": 0, "down": 0}

with open("./data/day2.txt", "r") as file:
    raw_buffer = file.readlines()
    for line in raw_buffer:
        command_value = line.split()
        commands[command_value[0]] += int(command_value[1])

print(commands["forward"] * (commands["down"] - commands["up"]))


# Day 2 part 2
# Relative position of the submarine with respect to the surface
coordinates = {"horizontal": 0, "depth": 0, "aim": 0}

# The operations are NOT commutative, then we update the values at every step

with open("./data/day2.txt", "r") as file:
    raw_buffer = file.readlines()
    for line in raw_buffer:
        command_value = line.split()
        if (command_value[0] == "down"):
            coordinates["aim"] += int(command_value[1])
        elif (command_value[0] == "up"):
            coordinates["aim"] -= int(command_value[1])
        else:
            coordinates["horizontal"] += int(command_value[1])
            coordinates["depth"] += coordinates["aim"] * int(command_value[1])

print(coordinates["horizontal"] * coordinates["depth"])
