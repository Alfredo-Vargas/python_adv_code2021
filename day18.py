import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "18.in"


class Node:
    """A Node for the binary tree (SnailFishNumber)"""

    def __init__(self, leftchild=None, rightchild=None, value=-1) -> None:
        if value != -1:
            self.value: int = value
        if leftchild is not None:
            self.leftchild: Node = leftchild
        if rightchild is not None:
            self.rightchild: Node = rightchild


class SnailFishNumber:
    """Binary Tree is the SnailFishNumber"""

    def __init__(self, root: Node) -> None:
        self.root = root

    def get_height(self, parent: Node) -> int:
        if parent is None:
            return -1
        leftchild_height = self.get_height(parent.leftchild)
        rightchild_height = self.get_height(parent.rightchild)
        return max(leftchild_height, rightchild_height) + 1

    def read_snailfish_number(self, head=None, values: list) -> Node:
        if head is None:
            head: Node = self.root
        if len(values) <= 1:
            return self.root
        else:
            left_element, right_element = values[0], values[1]
            left_node: Node = Node()
            right_node: Node = Node()
            head.leftchild = left_node
            head.rightchild = right_node
            if left_element.isinstance(int):
                head.leftchild.value = left_element
            if right_element.isinstance(int):
                head.rightchild.value = right_element
        return self.root


# llc = Node(None, None, 0)
# lrc = Node(None, None, 0)
# lc = Node(llc, lrc, 0)
# rc = Node(None, None, 0)
# root = Node(lc, rc, 0)

# snf_number = SnailFishNumber(root)

# height = snf_number.get_height(root)

# print(f"The height of this tree is: {height}")
root = Node(None, None, 0)

for line in open(infile):
    print(line.rstrip()[1:-1].split(","))
