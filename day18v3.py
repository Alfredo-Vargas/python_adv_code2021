import sys

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
    new_lefty = ""


def explode(sfn: str, index0: int) -> str:
    indexf = sfn[index0:].find("]")
    left_part = sfn[:index0]
    index1 = len(left_part) + indexf + 1
    right_part = sfn[index1:]
    middle_part = sfn[index0:index1]
    values = [int(value) for value in middle_part[1:-1].split(",")]
    print(left_part)
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
