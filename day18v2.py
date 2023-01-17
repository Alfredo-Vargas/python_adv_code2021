import sys


def print_snail_fish_number(sf_number: list) -> None:
    for char in sf_number:
        print(char, end="")
    print("\n")


def needs_to_explode(sf_number: list) -> tuple:
    counter = 0
    for i in range(len(sf_number)):
        if sf_number[i] == "[":
            counter += 1
        elif sf_number[i] == "]":
            counter -= 1
        if counter == 5:
            return (True, i)
    return (False, 0)


def explode(sf_number: list, index: int) -> list:
    ind = index
    exploding_term = ""
    while sf_number[ind + 1] != "]":
        exploding_term += sf_number[ind + 1]
        ind += 1
    temp_list = exploding_term.split(",")
    le, re = int(temp_list[0]), int(temp_list[1])
    new_sf_number = sf_number[0:index]
    new_sf_number.append("0")
    for char in sf_number[ind + 2 : :]:
        new_sf_number.append(char)

    left_number_found = False
    lefty = ""
    for i in reversed(range(index)):
        if new_sf_number[i].isdigit():
            lefty += new_sf_number[i]
            if not new_sf_number[i - 1].isdigit():
                left_number_found = True
                break
    if left_number_found:
        left_addition = int(lefty[::-1]) + le
    print(left_addition)
    # for char in new_sf_number[index - 1 :: -1]:
    #     if left_number_found:
    #         break
    #     if char.isdigit():
    #         print(char)
    # print(sf_number[ind])
    # print(sf_number[ind + 1])
    # print(sf_number[ind + 2 : :])
    # print(type(new_sf_number))

    # idx_left = index
    # idx_right = ind
    # while idx_left > 0:
    #     if sf_number[idx_left - 1] != "," and
    return new_sf_number


def main() -> None:
    infile = sys.argv[1] if len(sys.argv) > 1 else "18.in"
    snf0 = list(open(infile).read().strip())
    check = needs_to_explode(snf0)
    # print(snf0)
    print_snail_fish_number(snf0)
    if check[0]:
        snf0 = explode(snf0, check[1])
    print_snail_fish_number(snf0)


if __name__ == "__main__":
    main()
