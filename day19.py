import numpy as np
import os


def get_beacons_diff(scanner_a: np.ndarray, scanner_b: np.ndarray) -> tuple:
    point_diff = list()

    for i in range(len(scanner_a)):
        for j in range(len(scanner_b)):
            point_diff.append(tuple(scanner_a[i] - scanner_b[j]))

    uniques, indices, counts = np.unique(
        point_diff, return_index=True, return_counts=True, axis=0
    )

    if max(counts) >= 12:
        return (True, max(counts), uniques[0])
    else:
        return (False, max(counts), uniques[0])


def rotate90_scanner(scanner: np.ndarray, n: int) -> np.ndarray:
    if n == 0:
        return scanner
    elif n == 1:
        scanner[:, 2] = scanner[:, 2] * -1
        return scanner[:, [0, 2, 1]]
    elif n == 2:
        scanner[:, [1, 2]] = scanner[:, [1, 2]] * -1
        return scanner
    elif n == 3:
        scanner[:, 1] = scanner[:, 1] * -1
        return scanner[:, [0, 2, 1]]
    else:
        print("Invalid number of rotatiosn. No rotation performed")
        return scanner



def get_orientations(scanner: np.ndarray) -> list:
    orientations = list()

    # rotations along the positive x - axis
    rotxq1 = scanner.copy()
    rotxq2 = scanner.copy()
    rotxq2 = rotxq2[:, [0, 2, 1]]  # swap axis, y and z
    rotxq2[:, 1] = rotxq2[:, 1] * -1  # y becomes negative
    rotxq3 = scanner.copy()
    rotxq3[:, [1, 2]] = rotxq3[:, [1, 2]] * -1  # y and z become negative
    rotxq4 = scanner.copy()
    rotxq4 = rotxq4[:, [0, 2, 1]]  # swap axis, y and z
    rotxq4[:, 2] = rotxq4[:, 2] * -1  # z becomes negative
    orientations.append(rotxq1)
    orientations.append(rotxq2)
    orientations.append(rotxq3)
    orientations.append(rotxq4)
    # rotations along the negative x - axis
    orientations.append(rotxq1[:, [0, 2, 1]])
    orientations.append(rotxq2[:, [0, 2, 1]])
    orientations.append(rotxq3[:, [0, 2, 1]])
    orientations.append(rotxq4[:, [0, 2, 1]])

    # rotations along the positive y - axis
    rotyq1 = scanner.copy()
    rotyq2 = scanner.copy()
    rotyq2 = rotyq2[:, [2, 1, 0]]  # swap ayis, x and z
    rotyq2[:, 0] = rotyq2[:, 0] * -1  # x becomes negative
    rotyq3 = scanner.copy()
    rotyq3[:, [0, 2]] = rotyq3[:, [0, 2]] * -1  # x and z become negative
    rotyq4 = scanner.copy()
    rotyq4 = rotyq4[:, [2, 1, 0]]  # swap ayis, y and z
    rotyq4[:, 2] = rotyq4[:, 2] * -1  # z becomes negative
    orientations.append(rotyq1)
    orientations.append(rotyq2)
    orientations.append(rotyq3)
    orientations.append(rotyq4)
    # rotations along the negative y - axis
    orientations.append(rotyq1[:, [2, 1, 0]])
    orientations.append(rotyq2[:, [2, 1, 0]])
    orientations.append(rotyq3[:, [2, 1, 0]])
    orientations.append(rotyq4[:, [2, 1, 0]])

    # rotations along the positive z - axis
    rotzq1 = scanner.copy()
    rotzq2 = scanner.copy()
    rotzq2 = rotzq2[:, [1, 0, 2]]  # swap ayis, x and y
    rotzq2[:, 0] = rotzq2[:, 0] * -1  # x becomes negative
    rotzq3 = scanner.copy()
    rotzq3[:, [0, 1]] = rotzq3[:, [0, 1]] * -1  # x and y become negative
    rotzq4 = scanner.copy()
    rotzq4 = rotzq4[:, [1, 0, 2]]  # swap ayis, x and y
    rotzq4[:, 1] = rotzq4[:, 1] * -1  # y becomes negative
    orientations.append(rotzq1)
    orientations.append(rotzq2)
    orientations.append(rotzq3)
    orientations.append(rotzq4)
    # rotations along the negative z - axis
    orientations.append(rotzq1[:, [1, 0, 2]])
    orientations.append(rotzq2[:, [1, 0, 2]])
    orientations.append(rotzq3[:, [1, 0, 2]])
    orientations.append(rotzq4[:, [1, 0, 2]])

    return orientations


def read_scanners() -> list:
    # file_loc = "./data/day19.txt"
    file_loc = "./data/test.txt"

    # handle edge case
    with open(file_loc, "a+b") as f:
        try:
            f.seek(-2, os.SEEK_END)
            if f.read(1) != b"\n":
                print(
                    "No empty line at the end of file, adding an empty line to input file."
                )
                f.write(b"\n")
        except:
            f.seek(0)
        f.seek(0, os.SEEK_SET)

    # read input data
    scanners_list = list()
    scanner = list()
    for line in open(file_loc):
        # print(line.strip())
        if "scanner" in line:
            pass
        elif line == "\n":
            scanners_list.append(np.array(scanner))
            scanner.clear()
        else:
            raw_coords = list(line.strip().split(","))
            beacon_coords = [int(coord) for coord in raw_coords]
            scanner.append(np.asarray(beacon_coords))
    return scanners_list


def main() -> None:
    scanner_list = read_scanners()

    beacon_counter = 0
    for scanner in scanner_list:
        beacon_counter += len(scanner)

    print(
        f"Before subtracting overlapped beacons we have in total {beacon_counter} beacons and {len(scanner_list)} scanners."
    )
    for i in range(len(scanner_list)):
        for j in range(i + 1, len(scanner_list)):
            orientation = 0
            for scanner_oriented in get_orientations(scanner_list[j]):
                overlap_result = get_beacons_diff(scanner_list[i], scanner_oriented)
                if overlap_result[0]:
                    beacon_counter -= overlap_result[1]
                    print(
                        "------------------------------------------------------------"
                    )
                    print(f"Scanners {i}, {j} have {overlap_result[1]} common beacons.")
                    print(f"The scanner {j} has the orientation: {orientation}")
                    print(f"The difference vector is: {overlap_result[2]}\n")
                orientation += 1

    print(f"The total number of unique beacons is: {beacon_counter}")

    # for scann1_orientation in get_orientations(scanner_list[1]):
    #     print(get_beacons_diff(scanner_list[0], scann1_orientation))


if __name__ == "__main__":
    main()

# attempts part1:
# if no overlaps we have 719 beacons
# 527 wrong too high
# 526 wrong too high
# 524 wrong too high
# 523 wrong
# 479 wrong
# 383 wrong
# 479 wrong
# 491 wrong
