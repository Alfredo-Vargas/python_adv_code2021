import numpy as np
import os


def get_beacons_diff(scanner_a: np.ndarray, scanner_b: np.ndarray) -> tuple:
    point_diff = list()
    overlapping_points = list()
    pos_beacon = list()

    # scanner_a & scanner_b do not always have the same dimension so I cannot simply take the vector difference
    # instead:

    for i in range(len(scanner_a)):
        for j in range(len(scanner_b)):
            point_diff.append(tuple(scanner_a[i] - scanner_b[j]))
            pos_beacon.append((i, j))
    
    uniques, indices, counts = np.unique(point_diff, return_index=True, return_counts=True, axis=0)

    for i in range(len(counts)):
        if counts[i] >= 12:
            overlapping_points.append(pos_beacon[indices[i]])

    n_overlapped_points = len(scanner_a) * len(scanner_b) - len(uniques) + 1

    # are_overlapped_scanners = False

    # while not are_overlapped_scanners:
    #     for i in range(len(point_diff)):
    #         if counts[i] >= 12:
    #             pos_beacon.append((i, j))

    return (n_overlapped_points, overlapping_points)



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
