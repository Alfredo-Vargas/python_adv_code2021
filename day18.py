import sys
import re


def is_explodable(sfn: str) -> tuple:
    pe = 0
    counter = 0

    while pe < len(sfn):
        if sfn[pe] == "[":
            counter += 1
        elif sfn[pe] == "]":
            counter -= 1
        if counter >= 5:
            return (True, pe)
        pe += 1
    return (False, pe)


def is_splitable(sfn: str) -> tuple:
    ps = 0
    while ps < len(sfn) - 1:  # clossing outer brackets does not count
        if sfn[ps].isnumeric() and sfn[ps + 1].isnumeric():
            return (True, ps)
        ps += 1
    return (False, ps)


def is_reducible(sfn: str) -> bool:
    return is_explodable(sfn)[0] or is_splitable(sfn)[0]


def update_left(lefty: str, value: int) -> str:
    reversed_lefty = lefty[::-1]
    match = re.search(r"\d", reversed_lefty)
    if match:
        pointer = match.start()
        left = reversed_lefty[:pointer]
        if reversed_lefty[pointer + 1].isnumeric():
            digit = int(reversed_lefty[pointer + 1] + reversed_lefty[pointer])
            new_value = digit + value
            right_index = pointer + 2
            right = reversed_lefty[right_index:]
            new_lefty = right[::-1] + str(new_value) + left[::-1]
            return new_lefty
        else:
            new_value = int(reversed_lefty[pointer]) + value
            right_index = pointer + 1
            right = reversed_lefty[right_index:]
            new_lefty = right[::-1] + str(new_value) + left[::-1]
            return new_lefty
    return lefty


def update_right(righty: str, value: int) -> str:
    match = re.search(r"\d", righty)
    if match:
        pointer = match.start()
        left = righty[:pointer]
        if righty[pointer + 1].isnumeric():
            new_value = int(righty[pointer] + righty[pointer + 1]) + value
            right_index = pointer + 2
            right = righty[right_index:]
            new_righty = left + str(new_value) + right
            return new_righty
        else:
            new_value = int(righty[pointer]) + value
            right_index = pointer + 1
            right = righty[right_index:]
            new_righty = left + str(new_value) + right
            return new_righty
    return righty


def explode(sfn: str, index0: int) -> str:
    indexf = sfn[index0:].find("]")
    left_part = sfn[:index0]
    index1 = len(left_part) + indexf + 1
    right_part = sfn[index1:]
    middle_part = sfn[index0:index1]
    values = [int(value) for value in middle_part[1:-1].split(",")]
    new_left = update_left(left_part, values[0])
    new_right = update_right(right_part, values[1])
    exploded_sfn = new_left + "0" + new_right
    return exploded_sfn


def split(sfn: str, index0: int) -> str:
    left_part = sfn[:index0]
    index1 = index0 + 2
    right_part = sfn[index1:]
    number = int(sfn[index0] + sfn[index0 + 1])
    value = int(number / 2)
    if number % 2 == 0:
        middle_part = "[" + str(value) + "," + str(value) + "]"
    else:
        middle_part = "[" + str(value) + "," + str(value + 1) + "]"
    return left_part + middle_part + right_part


def reduce(sfn: str) -> str:
    while is_explodable(sfn)[0]:
        sfn = explode(sfn, is_explodable(sfn)[1])
    if is_splitable(sfn)[0]:
        sfn = split(sfn, is_splitable(sfn)[1])
    return sfn


def sum(sfn_a: str, sfn_b: str) -> str:
    return "[" + sfn_a + "," + sfn_b + "]"


def pair_magnitude(mid_part: str) -> str:
    values = [int(value) for value in mid_part[1:-1].split(",")]
    magnitude = 3 * values[0] + 2 * values[1]
    return str(magnitude)


def magnitude(sfn: str) -> int:
    result = sfn
    while "," in result:
        indexr = result.find("]")
        back_counter = result[indexr::-1].find("[")
        indexl = indexr - back_counter
        left_part = result[:indexl]
        iright = indexr + 1
        right_part = result[iright:]
        middle_part = result[indexl:iright]
        pair_mag = pair_magnitude(middle_part)
        result = left_part + pair_mag + right_part
    return int(result)


def main() -> None:
    file_loc = sys.argv[1] if len(sys.argv) > 1 else "Missing data for day 18"
    sfn_list = list()
    for line in open(file_loc):
        sfn_list.append(line.strip())

    # The Solution for part 1
    sfn_a = sfn_list[0]
    for i in range(1, len(sfn_list)):
        sfn_a = sum(sfn_a, sfn_list[i])
        while is_reducible(sfn_a):
            sfn_a = reduce(sfn_a)
    print("")
    print(80 * "=")
    print("Part 1")
    print(80 * "=")
    print(f"The fish number is {sfn_a}")
    print(f"Its magnitude is {magnitude(sfn_a)}")
    print("")
    largest_magnitude = 0
    # The Solution for part 2
    print(80 * "=")
    print("Part 2")
    print(80 * "=")
    for i in range(len(sfn_list)):
      for j in range(len(sfn_list)):
          if (i != j):
            left_sum = sum(sfn_list[i], sfn_list[j])
            while (is_reducible(left_sum)):
                left_sum = reduce(left_sum)
            right_sum = sum(sfn_list[j], sfn_list[i])
            while (is_reducible(right_sum)):
                right_sum = reduce(right_sum)
            if magnitude(left_sum) > largest_magnitude:
                largest_magnitude = magnitude(left_sum)
            if magnitude(right_sum) > largest_magnitude:
                largest_magnitude = magnitude(right_sum)
    print(f"The largest magnitude given the non-commutative sum is {largest_magnitude}")


if __name__ == "__main__":
    main()
