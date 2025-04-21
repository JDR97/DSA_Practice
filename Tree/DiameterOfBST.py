class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameterRecur(root, res):
    if root is None:
        return 0
    
    leftHeight = diameterRecur(root.left, res)
    rightHeight = diameterRecur(root.right, res)

    res[0] = max(res[0], leftHeight + rightHeight)

    return 1 + max(leftHeight, rightHeight)


def diameter(root):
    res = [0]
    diameterRecur(root, res)
    return res[0]

if __name__ == "__main__":

    # Constructed binary tree is
    #          5
    #        /   \
    #       8     6
    #      / \   /
    #     3   7 9
    root = Node(5)
    root.left = Node(8)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(9)

    print(diameter(root))