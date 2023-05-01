import os.path
import pytest
import copy

INPUT_TXT = os.path.join(os.path.dirname(__file__), "./data/day20.txt")
INPUT_S = os.path.join(os.path.dirname(__file__), "./data/test.txt")
EXPECTED = 35

algorithm = str()
input_image = None
n_padding = 8

with open(INPUT_S, 'r') as file:
    lines = file.readlines()
    algorithm = lines[0].strip()
    image_size = len(lines[2:])
    input_image = [[] for _ in range(n_padding + image_size)]
    horizontal_padding = ['.' for _ in range(int(n_padding / 2))]
    vertical_padding = ['.' for _ in range(image_size + n_padding)]

    for i in range(int(n_padding / 2)):
        input_image[i] += vertical_padding

    for idx in range(len(lines[2:])):
        row = horizontal_padding + list(lines[2:][idx].strip()) + horizontal_padding
        input_image[idx + int(n_padding / 2)] +=  row

    for i in range(int(n_padding / 2)):
        input_image[-1 - i] += vertical_padding

def compute(algorithm, input_image) -> int:
    answer = int()
    output_image = input_image[:]

    return answer

@pytest.mark.parametrize(
        ("input_s", "expected"),
        ((INPUT_S, EXPECTED),),
        )
def test(algortihm: str, input_s: str, expected: int) -> None:
    assert compute(algortihm, input_s) == expected

def main() -> int:

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
