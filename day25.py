import copy

sea_floor = []

with open("./data/day25.txt") as file_handler:
    lines = file_handler.readlines()
    for line in lines:
        sea_floor.append(list(line.rstrip()))


def move_east(original_sf: list) -> tuple:
    stop_moving_east = True
    sf = copy.deepcopy(original_sf)
    for i in range(len(sf)):
        for j in range(len(sf[0]) - 1):
            if original_sf[i][j] == ">" and original_sf[i][j + 1] == ".":
                stop_moving_east = False
                sf[i][j] = "."
                sf[i][j + 1] = ">"
    for i in range(len(sf)):
        if original_sf[i][len(sf[0]) - 1] == ">" and original_sf[i][0] == ".":
            stop_moving_east = False
            sf[i][len(sf[0]) - 1] = "."
            sf[i][0] = ">"
    return (stop_moving_east, sf)


def move_south(original_sf: list) -> list:
    stop_moving_south = True
    sf = copy.deepcopy(original_sf)
    for i in range(len(sf) - 1):
        for j in range(len(sf[0])):
            if original_sf[i][j] == "v" and original_sf[i + 1][j] == ".":
                stop_moving_south = False
                sf[i][j] = "."
                sf[i + 1][j] = "v"
    for i in range(len(sf[0])):
        if original_sf[len(sf) - 1][i] == "v" and original_sf[0][i] == ".":
            stop_moving_south = False
            sf[len(sf) - 1][i] = "."
            sf[0][i] = "v"
    return (stop_moving_south, sf)


def apply_step(sf: list) -> tuple:
    cucumbers_stop_moving_completely = True
    cucumbers_stop_moving_east, sf = move_east(sf)
    cucumbers_stop_moving_south, sf = move_south(sf)
    if not cucumbers_stop_moving_south or not cucumbers_stop_moving_east:
        cucumbers_stop_moving_completely = False
    return (cucumbers_stop_moving_completely, sf)


cucumbers_stop_moving_completely = False
counter = 0
while not cucumbers_stop_moving_completely:
    cucumbers_stop_moving_completely, sea_floor = apply_step(sea_floor)
    counter += 1

# Solution of part 1
print(f"After {counter} steps the sea cucumbers are not able to move anymore!")

# Part 2 does not require output
