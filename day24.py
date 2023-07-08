# taken from https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_24/day_24_p1.py
# steps and required list adjust to my input
from itertools import product

with open("./data/day24.txt") as fin:
    raw_data = fin.read().strip().split("\n\n")[4:5]

steps = [0, 6, 4, 2, 9, None, 10, None, None, 6, None, None, None, None]
required = [None, None, None, None, None, 2, None, 15, 10, None, 10, 4, 1, 1]

# part 1
# input_space = product(range(9, 0, -1), repeat=7)

# part 2
input_space = product(range(1, 10), repeat=7)


def works(digits):
    z = 0
    res = [0] * 14

    digits_idx = 0

    for i in range(14):
        increment, mod_req = steps[i], required[i]

        if increment == None:
            assert mod_req != None
            res[i] = (z % 26) - mod_req
            z //= 26
            if not (1 <= res[i] <= 9):
                return False

        else:
            assert increment != None
            z = z * 26 + digits[digits_idx] + increment
            res[i] = digits[digits_idx]
            digits_idx += 1

    return res


for digits in input_space:
    res = works(digits)
    if res:
        print("".join([str(i) for i in res]))
        break
