import sys
import numpy as np


def get_rotations(scn: np.ndarray) -> list:
    rotations = list()
    xy_rot = scn.copy()
    yz_rot = scn.copy()
    xz_rot = scn.copy()
    yz_rot[:, [1, 2]] = xy_rot[:, [2, 1]]  # rot along x axis
    xz_rot[:, [0, 2]] = xz_rot[:, [2, 0]]  # rot along y axis
    xy_rot[:, [0, 1]] = xy_rot[:, [1, 2]]  # rot along z axis
    rotations.append(yz_rot)
    rotations.append(xz_rot)
    rotations.append(xy_rot)
    return rotations


def get_inversions(scn: np.ndarray) -> list:
    inversions = list()
    pxpypz = scn.copy()
    pxmypz = scn.copy()
    mxpypz = scn.copy()
    mxmypz = scn.copy()
    pxpymz = scn.copy()
    pxmymz = scn.copy()
    mxpymz = scn.copy()
    mxmymz = scn.copy()
    # no inversion at all
    inversions.append(pxpypz)
    # only y inverted
    pxmypz[:, [1]] = -pxmypz[:, [1]]
    inversions.append(pxmypz)
    # only x inverted
    mxpypz[:, [0]] = -mxpypz[:, [0]]
    inversions.append(mxpypz)
    # x and y inverted
    mxmypz[:, [0, 1]] = -mxmypz[:, [0, 1]]
    inversions.append(mxmypz)
    # only z inverted
    pxpymz[:, [2]] = -pxpymz[:, [2]]
    inversions.append(pxpymz)
    # y and z inverted
    pxmymz[:, [1, 2]] = -pxmymz[:, [1, 2]]
    inversions.append(pxmymz)
    # x and z inverted
    mxpymz[:, [0, 2]] = -mxpymz[:, [0, 2]]
    inversions.append(mxpymz)
    # x y and z inverted
    mxmymz[:, [0, 1, 2]] = - mxmymz[:, [0, 1, 2]]
    inversions.append(mxmymz)
    return inversions


def get_orientations(scn: np.ndarray) -> list:
    orientations = list()
    rotations = get_rotations(scn)
    for rotation in rotations:
        inversions = get_inversions(rotation)
        for inversion in inversions:
            orientations.append(inversion)
    return orientations


def main() -> None:
    file_loc = sys.argv[1] if len(sys.argv) > 1 else "Missing data for day 19"
    scanners_list = list()
    scanner = list()

    for line in open(file_loc):
        if "scanner" in line:
            pass
        elif line == "\n":
            scanners_list.append(np.array(scanner))
            scanner.clear()
        else:
            raw_coords = list(line.strip().split(','))
            beacon_coords = [int(coord) for coord in raw_coords]
            scanner.append(beacon_coords)
    scanners_list.append(np.array(scanner))
    swapped = scanners_list[0].copy()
    inverted = scanners_list[0].copy()
    swapped[:, [0, 2]] = swapped[:, [2, 0]]
    inverted[:, [0]] = -inverted[:, [0]]
    # print(scanners_list[0])
    # print(swapped)
    # print(inverted)
    # print(inverted.tolist())
    orientations = get_orientations(scanners_list[0])
    print(orientations)
    print(len(orientations))


if __name__ == "__main__":
    main()
