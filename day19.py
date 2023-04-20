import numpy as np
import os


def get_beacons_diff(scanner_a: np.ndarray, scanner_b: np.ndarray) -> bool:
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
        return True
    else:
        return False

def get_two_dimensional_orientations(scanner: np.ndarray) -> list:
    plane_orientations = list()

    first_quadrant = scanner[:, [0, 1, 2]].copy()
    second_quadrant = scanner.copy()[:, [0, 2, 1]]
    second_quadrant[:, 2] = second_quadrant[:, 2] * -1
    third_quadrant = scanner.copy()
    third_quadrant[:, [1, 2]] = third_quadrant[:, [1, 2]] * -1
    fourth_quadrant = scanner.copy()[:, [0, 2, 1]]
    fourth_quadrant[:, 1] = fourth_quadrant[:, 1] * -1

    plane_orientations.append(first_quadrant)
    plane_orientations.append(second_quadrant)
    plane_orientations.append(third_quadrant)
    plane_orientations.append(fourth_quadrant)

    return plane_orientations
    

def get_axis_of_rotations(scanner: np.ndarray) -> list:
    axis_of_rotations = list()

    rot_axis_positive_x = scanner.copy()
    rot_axis_negative_x = scanner.copy()
    rot_axis_negative_x[:, 0] = rot_axis_negative_x[:, 0] * -1

    rot_axis_positive_y = scanner.copy()[:, [1, 0, 2]]
    rot_axis_negative_y = scanner.copy()[:, [1, 0, 2]]
    rot_axis_negative_y[:, 0] = rot_axis_negative_y[:, 0] * -1

    rot_axis_positive_z = scanner.copy()[:, [2, 0, 1]]
    rot_axis_negative_z = scanner.copy()[:, [1, 0, 1]]
    rot_axis_negative_z[:, 0] = rot_axis_negative_z[:, 0] * -1

    axis_of_rotations.append(rot_axis_positive_x)
    axis_of_rotations.append(rot_axis_negative_x)
    axis_of_rotations.append(rot_axis_positive_y)
    axis_of_rotations.append(rot_axis_negative_y)
    axis_of_rotations.append(rot_axis_positive_z)
    axis_of_rotations.append(rot_axis_negative_z)

    return axis_of_rotations

def get_rotation_orientations(scanner: np.ndarray) -> list:
    rot_orientations = list()

    for given_axis in get_axis_of_rotations(scanner):
        for orientation in get_two_dimensional_orientations(given_axis):
            rot_orientations.append(orientation)
    return rot_orientations


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

    for scanner in scanner_list:
        print(len(scanner))
    # print(scanner_list[1] - scanner_list[3])
    # print(get_beacons_diff(scanner_list[1], scanner_list[3]))

    # diff_points = tuple()
    # for i in range(len(scanner_list)):
    #     diff_points = 0
    #     for j in range(i + 1, len(scanner_list)):
    #         if diff_points[0] >= 12:
    #             break
    #         # print(i,j)
    #         given_scanner = scanner_list[i]
    #         axis_representations = get_axis_representations(given_scanner)
    #         for ar in axis_representations:
    #             if diff_points[0] >= 12:
    #                 break
    #             direction_representations = get_direction_representations(ar)
    #             for dr in direction_representations:
    #                 diff_points = get_beacons_diff(dr, scanner_list[j])
    #                 if diff_points[0] >= 12:
    #                     print("------------------------------------------------------------")
    #                     print(f"Found overlapped scanners {i} and {j}, with {diff_points} common beacons.")
    #                     # print(f"Scanners {i} and {j} have {diff_points} overlapping points")
    #                     break
