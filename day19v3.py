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



class Scanner:
    def __init__(self, index: int, pos: np.ndarray):
        self.index = index
        self.prev = None
        self.next = None

class ScannerMap:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, index: int, pos: np.ndarray):
        new_node = Scanner(index, pos)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return

        current = self.head
        while current is not None and current.data != data:
            current = current.next

        if current is None:
            return

        if current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


def create_mapping(results: list, n: int) -> dict:
    f = dict()
    t = dict()

    # we create the starting dictionary


    print(f"The dictionary is now:\n {t}")
    print("")
    print(f"The list is now:\n {f}")
    return f


def read_scanners() -> list:
    # file_loc = "./data/day19.txt"
    file_loc = "./data/test.txt"

    with open(file_loc, "a+b") as f:
        try:
            f.seek(-2, os.SEEK_END)
            if f.read(1) != b"\n":
                print("No empty line at the end of file, adding one.")
                f.write(b"\n")
        except:
            f.seek(0)
        f.seek(0, os.SEEK_SET)

    scanners_list = list()
    scanner = list()
    for line in open(file_loc):
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
                        beacon_counter -= overlap_result[1]
                        performed_rotations.append(
                            [i, j, list(axis_selected), k, overlap_result[2]]
                        )
    print(performed_rotations)
    print("")
    print(create_mapping(performed_rotations, len(scanner_list)))


if __name__ == "__main__":
    main()
