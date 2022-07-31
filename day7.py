# Advent of Code 2021

# Day 7 part 1 and 2

print("----------------------------------------")
print("----------------------------------------")
print("For day 7")
with open("./data/day7.txt", "r") as file:
    crabs = file.readline().rstrip().split(",")
    crabs_positions = np.array([int(x) for x in crabs])


length = max(crabs_positions) - min(crabs_positions)
sum_pos = sum(crabs_positions)
position = int(sum(crabs_positions) / length)
# Manually tweaked deviation and position (inspect the minimum)
deviation = 100
position = 400
list_fuels = []

for i in range(position - deviation, position + deviation, 1):
    fuel = 0
    for crab_position in crabs_positions:
        # fuel += abs(i - crab_position)  # fuel for part 1
        fuel += abs(i - crab_position) * (abs(i - crab_position) + 1) / 2
    list_fuels.append(int(fuel))
    # print(fuel, i)

print(min(list_fuels))
# Answers:
# 355521 with position 337
# 100148777 with position 493
