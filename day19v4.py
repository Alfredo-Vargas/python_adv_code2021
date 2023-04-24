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
    # if [68,-1246,-43] in uniques:
    #     print("yep")

    magic_index = 0
    if max(counts) >= 12:
        # print(f"Uniques are {uniques}")
        # print(f"Indices are {indices}")
        # print(f"Index")
        # print(f"Counts are {counts}")
        max_value = max(counts)
        magic_index = counts.tolist().index(max_value)
        # print(f"Index of max is: {counts.tolist().index(max_value)}")
        # print(f"Max counts is {counts[magic_index]}")
        # print(f"The translation vector is: {uniques[magic_index]}")

        return (True, max(counts), uniques[magic_index])
    else:
        return (False, max(counts), uniques[magic_index])


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
        return oriented_scanner
    elif n == 9:
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 10:
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 11:
        oriented_scanner[:, 1] = oriented_scanner[:, 1] * -1
        return oriented_scanner[:, [0, 2, 1]]

    # negative y
    elif n == 12:
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        return oriented_scanner
    elif n == 13:
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, 2] = oriented_scanner[:, 2] * -1
        return oriented_scanner[:, [0, 2, 1]]
    elif n == 14:
        oriented_scanner[:, 0] = oriented_scanner[:, 0] * -1
        oriented_scanner[:, [1, 2]] = oriented_scanner[:, [1, 2]] * -1
        return oriented_scanner
    elif n == 15:
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


def get_directions(scn: np.ndarray) -> list:
    sign_orientations = list()
    sign_orientations.append(scn)
    temp = scn.copy()
    temp[:, 0] = temp[:, 0] * -1
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, 1] = temp[:, 1] * -1
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, 2] = temp[:, 2] * -1
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, [0, 1]] = temp[:, [0, 1]] * -1
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, [0, 2]] = temp[:, [0, 2]] * -1
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, [1, 2]] = temp[:, [1, 2]] * -1
    sign_orientations.append(temp)
    sign_orientations.append(scn * -1)
    return sign_orientations


def main() -> None:
    scanner_list = read_scanners()

    beacon_counter = 0
    for scanner in scanner_list:
        beacon_counter += len(scanner)

    # for axis_selection in [(0,1,2), (0,2,1), (1,0,2),(1,2,0),(2,0,1),(2,1,0)]:
    #     print(axis_selection)
    #     print(scanner_list[0][:, axis_selection])
    # for sign_selection in [1, -1]:
    # print(scanner_list[0])
    # for i in range(3):
    #     temp = scanner_list[0].copy()
    #     temp[:, i] = temp[:, i] * -1
    #     print(temp)

    # print(scanner_list[0] * -1)

    print(f"IDB is {beacon_counter} beacons and {len(scanner_list)} scanners.")
    for i in range(len(scanner_list)):
        for j in range(i + 1, len(scanner_list)):
            # for i in range(1):
            #     for j in range(i + 1, 2):
            for axis_selection in [
                (0, 1, 2),
                (0, 2, 1),
                (1, 0, 2),
                (1, 2, 0),
                (2, 0, 1),
                (2, 1, 0),
            ]:
                signed_list = get_directions(scanner_list[j][:, axis_selection])
                for k in range(len(signed_list)):
                    # for sign_orientation in signed_list:
                    overlap_result = get_beacons_diff(scanner_list[i], signed_list[k])
                    if overlap_result[0]:
                        print(
                            f"Scanners {i}, {j} have {overlap_result[1]} common beacons."
                        )
                        beacon_counter -= overlap_result[1]
                        print(
                            f"The axis selection is {axis_selection}, and the sign index is {k}"
                        )
                        print(f"The difference vector is: {overlap_result[2]}\n")
    #         for k in range(24):
    #             overlap_result = get_beacons_diff(scanner_list[i], rotate90_scanner(scanner_list[j], k))
    #             if overlap_result[0]:
    #                 beacon_counter -= overlap_result[1]
    #                 print(f"Scanners {i}, {j} have {overlap_result[1]} common beacons.")
    #                 print(f"The difference vector is: {overlap_result[2]}\n")
    #                 print("----------------------------------------")

    print(f"The total number of unique beacons is: {beacon_counter}")


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
# 311 wrong
