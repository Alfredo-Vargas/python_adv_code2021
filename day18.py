import sys
import gc

# infile = sys.argv[1] if len(sys.argv) > 1 else "18.in"


class Node:
    """A Node for the binary tree (SnailFishNumber)"""

    def __init__(self, parent=None, leftchild=None, rightchild=None, value=-1) -> None:
        self.parent: Node = parent
        self.leftchild: Node = leftchild
        self.rightchild: Node = rightchild
        self.value: int = value

    def depth(self) -> int:
        head = self
        depth = 0
        while head.parent is not None:
            depth += 1
            head = head.parent
        return depth

    def height(self) -> int:
        if self.leftchild is None and self.rightchild is None:
            return 0
        leftchild_height = self.leftchild.height()
        rightchild_height = self.rightchild.height()
        return max(leftchild_height, rightchild_height) + 1


class SnailFishNumber:
    """Binary Tree is the SnailFishNumber"""

    def __init__(self, root: Node) -> None:
        self.root = root

    def read_snailfish_number(self, head: Node, values: list) -> None:
        left_term, right_term = values[0], values[1]
        left_child = Node(parent=head)
        right_child = Node(parent=head)
        head.leftchild = left_child
        head.rightchild = right_child
        if isinstance(left_term, int):
            head.leftchild.value = left_term
        else:
            self.read_snailfish_number(head.leftchild, left_term)
        if isinstance(right_term, int):
            head.rightchild.value = right_term
        else:
            self.read_snailfish_number(head.rightchild, right_term)

    def show_snail_fish_number(self, node: Node) -> None:
        # print(f"Node value is {node.value}, its height is: {self.get_height(node)}")
        print(f"{node.value, node.height(), node.depth()}")
        left_term = node.leftchild
        right_term = node.rightchild
        if isinstance(left_term, Node):
            self.show_snail_fish_number(left_term)
        if isinstance(right_term, Node):
            self.show_snail_fish_number(right_term)

    def explode(self) -> Node:
        if self.root.height() < 5:
            print(f"Height of sfn is too low: {self.root.height()} (min 5)")
            print("No explosion performed")
            return self.root

        # identify the Node to remove using traverse walking
        head = self.root

        while head.leftchild is not None and head.rightchild is not None:
            head = head.rightchild if head.leftchild.height() < head.rightchild.height() else head.leftchild
        print(f"The node to explode is {head.value, head.height(), head.depth()}")

        # we explode the nood and free the memory properly
        head.value = 0
        left_value = head.leftchild.value
        right_value = head.rightchild.value
        head.leftchild.parent = None  # avoids dangling pointer
        head.rightchild.parent = None  # avoids dangling pointer
        del head.leftchild  # deallocates memory from heap
        del head.rightchild  # deallocates memory from heap
        gc.collect()  # frees the memory

        return self.root


def main() -> None:
    # nodes with empty values are equal to -1
    # the root node has value -2
    root = Node(None, None, None, -2)
    sfn = SnailFishNumber(root)
    print(f"The value of the root value is {sfn.root.value}")
    print(f"Height of the sfn at start is: {sfn.root.height()}")
    # reading a snail fish number:
    # given_list = [1, 2]
    # given_list = [1, [1, 2]]
    # given_list = [[0, [2, 11]], [1, 2]]
    # given_list = [[[[[9, 8], 1], 2], 3], 4]
    # given_list = [7,[6,[5,[4,[3,2]]]]]
    # given_list = [[6,[5,[4,[3,2]]]],1]
    given_list = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
    sfn.read_snailfish_number(sfn.root, given_list)
    print(f"Value of the root value is {sfn.root.value}")
    print(f"Height of the sfn after read is: {sfn.root.height()}")
    print("\nThe sfn values, height and depth for each node are:")
    sfn.show_snail_fish_number(sfn.root)
    sfn.explode()

    # for line in open(infile):
    #     print(line.rstrip()[1:-1].split(","))


if __name__ == "__main__":
    main()
