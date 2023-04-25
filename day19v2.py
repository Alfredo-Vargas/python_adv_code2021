import numpy as np
import os


def get_beacons_diff(scanner_a: np.ndarray, scanner_b: np.ndarray) -> tuple:
    point_diff = list()

    for i in range(len(scanner_a)):
        for j in range(len(scanner_b)):
            point_diff.append(tuple(scanner_a[i] - scanner_b[j]))

    uniques, _, counts = np.unique(
        point_diff, return_index=True, return_counts=True, axis=0
    )
    magic_index = 0
    if max(counts) >= 12:
        max_value = max(counts)
        magic_index = counts.tolist().index(max_value)

        return (True, max(counts), uniques[magic_index])
    else:
        return (False, max(counts), uniques[magic_index])


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
    sign_orientations.append(scn)  # 0
    temp = scn.copy()
    temp[:, 0] = temp[:, 0] * -1  # 1
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, 1] = temp[:, 1] * -1  # 2
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, 2] = temp[:, 2] * -1  # 3
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, [0, 1]] = temp[:, [0, 1]] * -1  # 4
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, [0, 2]] = temp[:, [0, 2]] * -1  # 5
    sign_orientations.append(temp)
    temp = scn.copy()
    temp[:, [1, 2]] = temp[:, [1, 2]] * -1  # 6
    sign_orientations.append(temp)
    sign_orientations.append(scn * -1)  # 7
    return sign_orientations


def revert_rotation(scn: np.ndarray, k: int) -> np.ndarray:
    temp = scn.copy()
    if k == 0:  # 0
        return temp
    elif k == 1:
        temp[0] = temp[0] * -1  # 1
        return temp
    elif k == 2:
        temp[1] = temp[1] * -1  # 2
        return temp
    elif k == 3:
        temp[2] = temp[2] * -1  # 3
        return temp
    elif k == 4:
        temp[[0, 1]] = temp[[0, 1]] * -1  # 4
        return temp
    elif k == 5:
        temp[[0, 2]] = temp[[0, 2]] * -1  # 5
        return temp
    elif k == 6:
        temp[[1, 2]] = temp[[1, 2]] * -1  # 6
        return temp
    elif k == 7:
        temp = temp * -1
        return temp
    else:
        print("Invalid rotation. Returning same value ...")
        return temp


def create_mapping(results: list, n: int) -> list:
    final_list = list()
    t = dict()

    for result in results:
        if result[1] not in t:
            t[result[1]] = (result[0], result[2], result[3], result[4])
    print("The initial mapping is")
    print(t)
    print("")
    final_list.append((results[0][1], results[0][4]))

    for result in results:
        if result[0] != 0:
            print(f"\nThe final list is: {final_list}\n\n")
            if result[0] in t:
                while result[0] != 0:
                    transf = t[result[0]]
                    # result[4] = revert_rotation(result[4][transf[1]], transf[2])
                    result[4] = revert_rotation(result[4], transf[2])
                    result[0] = transf[0]
                    result[4] += transf[3]  ##
                    if result[0] == 0:
                        # result[4] += results[0][4]
                        final_list.append((result[1], result[4]))
                    else:
                        result[4] += transf[5]
            elif result[1] in t:
                result[0], result[1] = result[1], result[0]
                result[4] *= -1
                print("entering recursion with result:")
                print(result)
                if result[0] in t:
                    while result[0] != 0:
                        print(f"recursion: {result[0]}")
                        transf = t[result[0]]
                        # result[4] = revert_rotation(result[4][transf[1]], transf[2])
                        result[4] = revert_rotation(result[4], transf[2])
                        result[3] = transf[2]
                        result[2] = transf[1]
                        result[0] = transf[0]
                        result[4] += transf[3]  # always
                        print(result)
                        if result[0] == 0:
                            # result[4] += results[0][4]
                            final_list.append((result[1], result[4]))
                        # else:
                        #     result[4] += transf[3]  # always

    return final_list


def main() -> None:
    scanner_list = read_scanners()

    beacon_counter = 0
    for scanner in scanner_list:
        beacon_counter += len(scanner)

    # print(f"IDB is {beacon_counter} beacons and {len(scanner_list)} scanners.")
    axis_set = [
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    ]
    performed_rotations = list()
    for i in range(len(scanner_list)):
        for j in range(i + 1, len(scanner_list)):
            for axis_selected in axis_set:
                signed_list = get_directions(scanner_list[j][:, axis_selected])
                for k in range(len(signed_list)):
                    overlap_result = get_beacons_diff(scanner_list[i], signed_list[k])
                    if overlap_result[0]:
                        # print("----------------------------------------")
                        # print(
                        #     f"Scanners {i}, {j} have {overlap_result[1]} common beacons."
                        # )
                        beacon_counter -= overlap_result[1]
                        # print(
                        #     f"The axis selection is {axis_selected}, and the direction index is {k}"
                        # )
                        # print(f"The raw difference vector is: {overlap_result[2]}")
                        performed_rotations.append(
                            [i, j, list(axis_selected), k, overlap_result[2]]
                        )

    # print(f"The total number of unique beacons is: {beacon_counter}\n")
    print(performed_rotations)
    print("")
    print(create_mapping(performed_rotations, len(scanner_list)))


if __name__ == "__main__":
    main()
