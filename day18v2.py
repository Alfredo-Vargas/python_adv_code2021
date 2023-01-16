import sys
import gc

infile = sys.argv[1] if len(sys.argv) > 1 else "18.in"

string1 = open(infile).read().strip()
snf1 = list(string1)


def needs_to_explode(sf_number: str) -> bool:
    counter = 0
    for char in sf_number:
        if char == "[":
            counter += 1
        elif char == "]":
            counter -= 1
        if counter == 5:
            return True
    return False


print(needs_to_explode(string1))
