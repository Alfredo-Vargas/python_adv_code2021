import sys

# infile = sys.argv[1] if len(sys.argv) > 1 else "18.in"


class Node:
    """A Node for the binary tree (SnailFishNumber)"""

    def __init__(self, parent=None, leftchild=None, rightchild=None, value=-1) -> None:
        self.parent: Node = parent
        self.value: int = value
        self.leftchild: Node = leftchild
        self.rightchild: Node = rightchild


class SnailFishNumber:
    """Binary Tree is the SnailFishNumber"""

    def __init__(self, root: Node) -> None:
        self.root = root

    def get_height(self, node: Node) -> int:
        if node is None:
            return -1
        leftchild_height = self.get_height(node.leftchild)
        rightchild_height = self.get_height(node.rightchild)
        return max(leftchild_height, rightchild_height) + 1

    def read_snailfish_number(self, head: Node, values: list) -> None:
        left_term, right_term = values[0], values[1]
        left_child = Node()
        right_child = Node()
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
        print(f"The node value is {node.value} and its height is: {self.get_height(node)}")
        left_term = node.leftchild
        right_term = node.rightchild
        if isinstance(left_term, Node):
            self.show_snail_fish_number(left_term)
        if isinstance(right_term, Node):
            self.show_snail_fish_number(right_term)


# for line in open(infile):
#     print(line.rstrip()[1:-1].split(","))
def main() -> None:
    # emtpy nodes have value equal to -1
    # the root node has value -2
    root = Node(None, None, None, -2)
    sfn = SnailFishNumber(root)
    print(f"The value of the root value is {sfn.root.value}")
    print(f"Height of the sfn at start is: {sfn.get_height(sfn.root)}")
    # reading a snail fish number:
    # given_list = [1, 2]
    # given_list = [1, [1, 2]]
    given_list = [[0, [2, 11]], [1, 2]]
    sfn.read_snailfish_number(sfn.root, given_list)
    print(f"Value of the root value is {sfn.root.value}")
    print(f"Height of the sfn after read is: {sfn.get_height(sfn.root)}")
    print("\nThe sfn values are:")
    sfn.show_snail_fish_number(sfn.root)


if __name__ == "__main__":
    main()

# TODO:
# add the depth function to implement explossions