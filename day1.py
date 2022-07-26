# Advent of Code 2021

# Day 1 part 1
# Counter measurements that are larger than the previous one
counter_by_single_value = 0

with open("./data/day1.txt", "r") as file:
    raw_buffer = file.readlines()
    for i in range(1, len(raw_buffer), 1):
        if int(raw_buffer[i]) > int(raw_buffer[i - 1]):
            counter_by_single_value += 1

print(counter_by_single_value)


# Day 2 part 2
# Counter measurements of three consecutive single measurements
counter_by_sliding_window = 0

with open("./data/day1.txt", "r") as file:
    raw_buffer = file.readlines()
    prev_sum = 0
    current_sum = 0
    # The sliding window has a size of 3, to be able to compare we need
    # to start from the fourth element
    for i in range(3, len(raw_buffer), 1):

        prev_sum = int(raw_buffer[i - 3]) + \
            int(raw_buffer[i - 2]) + \
            int(raw_buffer[i - 1])

        current_sum = int(raw_buffer[i - 2]) + \
            int(raw_buffer[i - 1]) + \
            int(raw_buffer[i])

        if current_sum > prev_sum:
            counter_by_sliding_window += 1


print(counter_by_sliding_window)
