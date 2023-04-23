import numpy as np
import os


def get_beacons_diff(scanner_a: np.ndarray, scanner_b: np.ndarray) -> tuple:
    point_diff = list()
    overlapping_points = list()
    # pos_beacon = list()
    # scanner_a & scanner_b do not always have the same dimension so I cannot simply take the vector difference
    # instead:

    for i in range(len(scanner_a)):
        for j in range(len(scanner_b)):
            point_diff.append(tuple(scanner_a[i] - scanner_b[j]))
            # pos_beacon.append((i, j))

    uniques, indices, counts = np.unique(
        point_diff, return_index=True, return_counts=True, axis=0
    )

    if max(counts) >= 12:
        return (True, max(counts), uniques[0])
    else:
        return (False, max(counts), uniques[0])


def rotate90_scanner(scanner: np.ndarray, n: int) -> np.ndarray:
    oriented_scanner = scanner.copy()
    # 0-3, four possible orientations of the scanner along the positive x-axis
    # 4-7, four possible orientations of the scanner along the negative x-axis
    # 8-11 four possible orientations of the scanner along the positive y-axis
    # 12-15 four possible orientations of the scanner along the negative y-axis
    # 16-19 four possible orientations of the scanner along the positive z-axis
    # 19-23 four possible orientations of the scanner along the negative z-axis

    # positive x
    if n == 0:
        return oriented_scanner
    elif n == 1:
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 2:
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 3:
        oriented_scanner[:, 1] = oriented_scanner[:, 1] * -1
        return oriented_scanner[:, [0, 2, 1]]

    # negative x
    elif n == 4:
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        return oriented_scanner
    elif n == 5:
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 6:
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 7:
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, 1] = oriented_scanner[:, 1] * -1
        return oriented_scanner[:, [0, 2, 1]]

    # positive y
    if n == 8:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        return oriented_scanner
    elif n == 9:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 10:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 11:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        oriented_scanner[:, 1] = oriented_scanner[:, 1] * -1
        return oriented_scanner[:, [0, 2, 1]]

    # negative y
    elif n == 12:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        return oriented_scanner
    elif n == 13:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 14:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 15:
        oriented_scanner = oriented_scanner[:, [1, 0, 2]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, 1] = oriented_scanner[:, 1] * -1
        return oriented_scanner[:, [0, 2, 1]]
    # positive z
    if n == 16:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        return oriented_scanner
    elif n == 17:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 18:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 19:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        oriented_scanner[:, 1] = oriented_scanner[:, 1] * -1
        return oriented_scanner[:, [0, 2, 1]]

    # negative z
    elif n == 20:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        return oriented_scanner
    elif n == 21:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 22:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 23:
        oriented_scanner = oriented_scanner[:, [2, 1, 0]]
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, 1] = oriented_scanner[:, 1] * -1
        return oriented_scanner[:, [0, 2, 1]]
    else:
        print("Invalid number for rotations. No rotation performed")
        return oriented_scanner


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

    print(f"IDB is {beacon_counter} beacons and {len(scanner_list)} scanners.")
    for i in range(len(scanner_list)):
        for j in range(i + 1, len(scanner_list)):
            for k in range(24):
                overlap_result = get_beacons_diff(scanner_list[i], rotate90_scanner(scanner_list[j], k))
                if overlap_result[0]:
                    beacon_counter -= overlap_result[1]
                    print(f"Scanners {i}, {j} have {overlap_result[1]} common beacons.")
                    print(f"The difference vector is: {overlap_result[2]}\n")
                    print("----------------------------------------")
            # for scanner_oriented in get_orientations(scanner_list[j]):
            #     overlap_result = get_beacons_diff(scanner_list[i], scanner_oriented)
            #     if overlap_result[0]:
            #         beacon_counter -= overlap_result[1]
            #         print(
            #             "------------------------------------------------------------"
            #         )
            #         print(f"Scanners {i}, {j} have {overlap_result[1]} common beacons.")
            #         print(f"The scanner {j} has the orientation: {orientation}")
            #         print(f"The difference vector is: {overlap_result[2]}\n")
            #     orientation += 1

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
# 491 wrong
