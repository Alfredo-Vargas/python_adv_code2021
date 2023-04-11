import numpy as np
import os


def get_beacons_diff(scanner_a: np.ndarray, scanner_b: np.ndarray) -> int:
    point_diff = list()
    overlapping_points = list()
    pos_beacon = list()

    # for beacon_a in scanner_a:
    #     for beacon_b in scanner_b:
    #         point_diff.append(tuple(beacon_a - beacon_b))
    # return len(scanner_a) * len(scanner_b) - len(set(point_diff))

    for i in range(len(scanner_a)):
        for j in range(len(scanner_b)):
            point_diff.append(tuple(scanner_a[i] - scanner_b[j]))
            pos_beacon.append((i, j))

    uniques, counts = np.unique(point_diff, return_counts=True)

    are_overlapped_scanners = False

    while not are_overlapped_scanners:
        for i in range(len(point_diff)):
            if counts[i] >= 12:
                pos_beacon.append((i, j))

    return point_diff



def get_axis_representations(scanner: np.ndarray) -> list:
    sar = list()  # scanner axis representation
    sar.append(scanner[:, [0, 1, 2]])
    sar.append(scanner[:, [0, 2, 1]])
    sar.append(scanner[:, [1, 2, 0]])
    sar.append(scanner[:, [1, 0, 2]])
    sar.append(scanner[:, [2, 0, 1]])
    sar.append(scanner[:, [2, 1, 0]])
    return sar


def get_direction_representations(scanner: np.ndarray) -> list:
    sdr = list()  # scanner direction representation
    # single axis inversion
    for i in range(3):
        temp = scanner.copy()
        temp[:, i] = temp[:, i] * -1
        sdr.append(temp)
    # double axis inversion
    for i in range(3):
        for j in range(i + 1, 3):
            temp = scanner.copy()
            temp[:, [i, j]] = temp[:, [i, j]] * -1
            sdr.append(temp)
    # no inversion and all axis inversion
    sdr.append(scanner)
    sdr.append(scanner * -1)
    return sdr


# def get_rotation_representations(scanner: np.ndarray) -> list:
#     srr = list()  # scanner rotation representation
#     return srr


def read_scanners() -> list:
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
            # else:
            #     print("empty line found, nothing to do")
            #     f.seek(-2, os.SEEK_CUR)
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
    # print(len(get_axis_representations(scanner_list[0])))
    # print(len(get_direction_representations(scanner_list[0])))

    diff_points = int()
    for i in range(len(scanner_list)):
        diff_points = 0
        for j in range(i + 1, len(scanner_list)):
            if diff_points >= 12:
                break
            # print(i,j)
            given_scanner = scanner_list[i]
            axis_representations = get_axis_representations(given_scanner)
            for ar in axis_representations:
                if diff_points >= 12:
                    break
                direction_representations = get_direction_representations(ar)
                for dr in direction_representations:
                    diff_points = get_beacons_diff(dr, scanner_list[j])
                    if diff_points >= 12:
                        print("------------------------------------------------------------")
                        print(f"Found overlapped scanners {i} and {j}, with {diff_points} common beacons.")
                        # print(f"Scanners {i} and {j} have {diff_points} overlapping points")
                        break

    print("------------------------------------------------------------")
    # print(get_beacons_diff(scanner_list[1], scanner_list[3]))

    # print(f"Beacons diff when there are 11 matches: \n{scanner_list[1] - scanner_list[3]}")
    # for beaca in scanner_list[1]:
    #     for beacb in scanner_list[2]:
    #         print(beaca - beacb)
    # print(scanner_list[1] - scanner_list[2])

    # for scanner in scanner_list:
    #     distances_list.append(get_beacon_relative_distances(scanner))

    # for scanner in scanner_list:

    # for scanner in scanner_list:
    #     print(type(scanner), scanner.shape, type(scanner[0]), scanner[0].shape)
    # print(len(scanner_list))
    # scanners_list.append(np.array(scanner))
    # swapped = scanners_list[0].copy()
    # inverted = scanners_list[0].copy()
    # swapped[:, [0, 2]] = swapped[:, [2, 0]]
    # inverted[:, [0]] = -inverted[:, [0]]
    # print(scanners_list[0])
    # print(swapped)
    # print(inverted)
    # print(inverted.tolist())
    # orientations = get_orientations(scanners_list[0])
    # print(orientations)
    # print(len(orientations))
    # print(len(scanners_list))
    # for scanner in scanners_list:
    #     print(type(scanner), scanner.shape, type(scanner[0]), scanner[0].shape)


# def get_rotations(scn: np.ndarray) -> list:
#     rotations = list()
#     xy_rot = scn.copy()
#     yz_rot = scn.copy()
#     xz_rot = scn.copy()
#     yz_rot[:, [1, 2]] = xy_rot[:, [2, 1]]  # rot along x axis
#     xz_rot[:, [0, 2]] = xz_rot[:, [2, 0]]  # rot along y axis
#     xy_rot[:, [0, 1]] = xy_rot[:, [1, 2]]  # rot along z axis
#     rotations.append(yz_rot)
#     rotations.append(xz_rot)
#     rotations.append(xy_rot)
#     return rotations


# def get_inversions(scn: np.ndarray) -> list:
#     inversions = list()
#     pxpypz = scn.copy()
#     pxmypz = scn.copy()
#     mxpypz = scn.copy()
#     mxmypz = scn.copy()
#     pxpymz = scn.copy()
#     pxmymz = scn.copy()
#     mxpymz = scn.copy()
#     mxmymz = scn.copy()
#     # no inversion at all
#     inversions.append(pxpypz)
#     # only y inverted
#     pxmypz[:, [1]] = -pxmypz[:, [1]]
#     inversions.append(pxmypz)
#     # only x inverted
#     mxpypz[:, [0]] = -mxpypz[:, [0]]
#     inversions.append(mxpypz)
#     # x and y inverted
#     mxmypz[:, [0, 1]] = -mxmypz[:, [0, 1]]
#     inversions.append(mxmypz)
#     # only z inverted
#     pxpymz[:, [2]] = -pxpymz[:, [2]]
#     inversions.append(pxpymz)
#     # y and z inverted
#     pxmymz[:, [1, 2]] = -pxmymz[:, [1, 2]]
#     inversions.append(pxmymz)
#     # x and z inverted
#     mxpymz[:, [0, 2]] = -mxpymz[:, [0, 2]]
#     inversions.append(mxpymz)
#     # x y and z inverted
#     mxmymz[:, [0, 1, 2]] = -mxmymz[:, [0, 1, 2]]
#     inversions.append(mxmymz)
#     return inversions


# def get_orientations(scn: np.ndarray) -> list:
#     orientations = list()
#     rotations = get_rotations(scn)
#     for rotation in rotations:
#         inversions = get_inversions(rotation)
#         for inversion in inversions:
#             orientations.append(inversion)
#     return orientations

# def get_beacon_relative_distances(scanner: np.ndarray) -> list:
#     distances_list = list()
#     for i in range(len(scanner)):
#         for j in range(1, len(scanner)):
#             distances_list.append(np.linalg.norm(scanner[i] - scanner[j]))
#     return distances_list

if __name__ == "__main__":
    main()
