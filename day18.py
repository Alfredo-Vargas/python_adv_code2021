import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "18.in"


class Node:
    """A Node for the binary tree (SnailFishNumber)"""
    def __init__(self, leftchild, rightchild, value):
        self.value: int = value
        self.leftchild: Node = leftchild
        self.rightchild: Node = rightchild


class SnailFishNumber:
    """Binary Tree is the SnailFishNumber"""
    def __init__(self, root: Node):
        self.root = root

    def get_height(self, parent: Node) -> int:
        if parent is None:
            return - 1
        leftchild_height = self.get_height(parent.leftchild)
        rightchild_height = self.get_height(parent.rightchild)
        return max(leftchild_height, rightchild_height) + 1


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
