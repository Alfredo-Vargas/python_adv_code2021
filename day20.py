import os.path
import pytest
import copy

# reading and parsing input
INPUT_TXT = os.path.join(os.path.dirname(__file__), "./data/day20.txt")
INPUT_S = os.path.join(os.path.dirname(__file__), "./data/test.txt")
EXPECTED = 35


def read_input(INPUT_TXT: str, padding: int) -> tuple:
    with open(INPUT_TXT, "r") as file:
        lines = file.readlines()
        algorithm = lines[0].strip()
        image_size = len(lines[2:])
        input_image = [[] for _ in range(2 * padding + image_size)]
        horizontal_padding = ["." for _ in range(padding)]
        vertical_padding = ["." for _ in range(image_size + 2 * padding)]

        for i in range(padding):
            input_image[i] += vertical_padding

        for idx in range(len(lines[2:])):
            row = horizontal_padding + list(lines[2:][idx].strip()) + horizontal_padding
            input_image[idx + padding] += row

        for i in range(padding):
            input_image[-1 - i] += vertical_padding
    return (input_image, algorithm)

def apply_filter(input_image: list, algorithm: str, output_image: list, padding: int) -> list:
    output_image = copy.deepcopy(input_image)
    n_rows = len(input_image)
    n_cols = len(input_image[0])

    # filter sliding
    for i in range(0, n_rows - padding):
        row_filters = input_image[i : i + 3]
        for j in range(0, n_cols - padding):
            filter = [column[j : j + 3] for column in row_filters]
            string_number = str()
            for row in filter:
                for value in row:
                    if value == ".":
                        string_number += "0"
                    else:
                        string_number += "1"

            binary_number_in_dec = int(string_number, 2)
            output_image[i + 1][j + 1] = algorithm[binary_number_in_dec]
    return output_image


def count_lit_pixels(input_image: list) -> int:
    lit_counter = 0
    for row in input_image:
        lit_counter += row.count('#')
    return lit_counter

def compute(input: str) -> int:
    print_images = False
    padding = 3  # will depend on the number of the interations
    input_image, algorithm = read_input(input, padding)
    if print_images:
        print(f"The algorithm is:\n{algorithm}")


    if print_images:
        print(f"The input image is:\n")
        for line in input_image:
            print(line)

    output1 = copy.deepcopy(input_image)
    output1 = apply_filter(input_image, algorithm, output1, padding)

    padding -= 1

    if print_images:
        print("\nAfter applying the filter one time:")
        for line in output1:
            print(line)

    output2 = copy.deepcopy(output1)
    output2 = apply_filter(output1, algorithm, output2, padding)
    padding -= 1

    if print_images:
        print("\nAfter applying the filter the second time:")
        for line in output2:
            print(line)

    if print_images:
        print(f"\nThe lit counter is: {count_lit_pixels(output2)}")
    return count_lit_pixels(output2)

@pytest.mark.parametrize(
        ("input_s", "expected"),
        ((INPUT_S, EXPECTED),),
        )
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    print(f"Part 1 solution is: {compute(INPUT_TXT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
