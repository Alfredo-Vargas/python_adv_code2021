import sys
import re

# infile = sys.argv[1] if len(sys.argv) > 1 else "18.in"
input0 = "[[3,4],5]"
input1 = "[[[[[9,8],1],2],3],4]"
input2 = "[[[[0,9],2],3],4]"
input3 = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"

input4 = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
input5 = "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"


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
    print(left_part)
    update_left(left_part, values[0])
    print(left_part[::-1])
    print(values)
    print(right_part)
    return sfn


print("Testing explodability")
print(is_explodable(input0))
print(is_explodable(input1))
print(is_explodable(input2))
print(is_explodable(input3))
print("")
print("Testing splitability")
print(is_splitable(input4))
print(is_splitable(input5))

print("")
explode(input1, 4)
print("")
explode(input3, 10)
# parsing


# index = input.find("]")
# slice = input[: index + 1]
# print(index)
# print(slice)
