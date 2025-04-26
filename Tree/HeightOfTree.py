class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    
    left_h = height(root.left)
    right_h = height(root.right)

    return max(left_h, right_h) + 1


if __name__ == "__main__":
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(10)

    print(height(root))