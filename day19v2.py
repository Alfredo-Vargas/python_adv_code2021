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


def get_rotations(scanner: np.ndarray) -> list:
    rotations = list()

    identity = np.identity(3)

    mpx = np.array(
        [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
    )  # 90 rotation matrix along positive x

    mnx = np.array(
        [[-1, 0, 0], [0, 0, -1], [0, 1, 0]]
    )  # 90 rotation matrix along negative x

    postive_xrotations = [identity, mpx, np.matmul(mpx, mpx), np.matmul(mpx, np.matmul(mpx, mpx))]
    negative_xrotations = [identity, mnx, np.matmul(mnx, mnx), np.matmul(mnx, np.matmul(mnx, mnx))]

    rotations.append(scanner)
    rotated_scanner = np.array(scanner.shape)
    for i in range(len(scanner)):
        rotated_scanner[i] = np.matmul(mpx, scanner[i])
    rotations.append(rotated_scanner)
    rotated_scanner = np.array(scanner.shape)
    for i in range(len(scanner)):
        rotated_scanner[i] = np.matmul(mpx, np.matmul(mpx, scanner[i]))
    rotations.append(rotated_scanner)
    rotated_scanner = np.array(scanner.shape)
    for i in range(len(scanner)):
        rotated_scanner[i] = np.matmul(mpx, np.matmul(mpx, np.matmul(mpx, scanner[i])))
    rotations.append(rotated_scanner)

    scanner_inverted = scanner.copy()
    scanner_inverted[:0] = scanner_inverted[:0] * -1
    rotations.append(scanner_inverted)
    rotated_scanner = np.array(scanner.shape)
    for i in range(len(scanner)):
        rotated_scanner[i] = np.matmul(mpx, scanner[i])
    rotations.append(rotated_scanner)
    rotated_scanner = np.array(scanner.shape)
    for i in range(len(scanner)):
        rotated_scanner[i] = np.matmul(mpx, np.matmul(mpx, scanner[i]))
    rotations.append(rotated_scanner)
    rotated_scanner = np.array(scanner.shape)
    for i in range(len(scanner)):
        rotated_scanner[i] = np.matmul(mpx, np.matmul(mpx, np.matmul(mpx, scanner[i])))
    rotations.append(rotated_scanner)

    return rotations


def get_orientations(scanner: np.ndarray) -> list:
    orientations = list()

    # rotations along the positive x - axis
    rotxq1 = scanner.copy()[:, [0, 1, 2]]
    rotxq2 = rotxq1.copy()
    rotxq2 = rotxq2[:, [0, 2, 1]]  # swap axis, y and z
    rotxq2[:, 1] = rotxq2[:, 1] * -1  # y becomes negative
    rotxq3 = rotxq1.copy()
    rotxq3[:, [1, 2]] = rotxq3[:, [1, 2]] * -1  # y and z become negative
    rotxq4 = rotxq1.copy()
    rotxq4 = rotxq4[:, [0, 2, 1]]  # swap axis, y and z
    rotxq4[:, 2] = rotxq4[:, 2] * -1  # z becomes negative
    orientations.append(rotxq1)
    orientations.append(rotxq2)
    orientations.append(rotxq3)
    orientations.append(rotxq4)
    # rotations along the negative x - axis
    rotxqn1 = rotxq1.copy()
    rotxqn1[:, 0] = rotxqn1[:, 0] * -1
    orientations.append(rotxq1[:, [0, 2, 1]])
    orientations.append(rotxq2[:, [0, 2, 1]])
    orientations.append(rotxq3[:, [0, 2, 1]])
    orientations.append(rotxq4[:, [0, 2, 1]])

    # rotations along the positive y - axis
    rotyq1 = scanner.copy()[:, [1, 0, 2]]
    rotyq2 = rotyq1.copy()
    rotyq2 = rotyq2[:, [0, 2, 1]]
    rotyq2[:, 1] = rotyq2[:, 1] * -1
    rotyq3 = rotyq1.copy()
    rotyq3[:, [1, 2]] = rotyq3[:, [1, 2]] * -1
    rotyq4 = rotyq1.copy()
    rotyq4 = rotyq4[:, [0, 2, 1]]
    rotyq4[:, 2] = rotyq4[:, 2] * -1
    orientations.append(rotyq1)
    orientations.append(rotyq2)
    orientations.append(rotyq3)
    orientations.append(rotyq4)
    # rotations along the negative y - axis
    orientations.append(rotyq1[:, [0, 2, 1]])
    orientations.append(rotyq2[:, [0, 2, 1]])
    orientations.append(rotyq3[:, [0, 2, 1]])
    orientations.append(rotyq4[:, [0, 2, 1]])

    # rotations along the positive z - axis
    rotzq1 = scanner.copy()[:, [2, 0, 1]]
    rotzq2 = rotzq1.copy()
    rotzq2 = rotzq2[:, [0, 2, 1]]
    rotzq2[:, 1] = rotzq2[:, 1] * -1
    rotzq3 = rotzq1.copy()
    rotzq3[:, [1, 2]] = rotzq3[:, [1, 2]] * -1
    rotzq4 = rotzq1.copy()
    rotzq4 = rotzq4[:, [0, 2, 1]]
    rotzq4[:, 2] = rotzq4[:, 2] * -1
    orientations.append(rotzq1)
    orientations.append(rotzq2)
    orientations.append(rotzq3)
    orientations.append(rotzq4)
    # rotations along the negative z - axis
    orientations.append(rotzq1[:, [0, 2, 1]])
    orientations.append(rotzq2[:, [0, 2, 1]])
    orientations.append(rotzq3[:, [0, 2, 1]])
    orientations.append(rotzq4[:, [0, 2, 1]])

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
# 491 wrong
