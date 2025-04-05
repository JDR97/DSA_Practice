class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

#Post-Order: Left Right Root
def postorder(root, arr):
    if root is None:
        return
    
    postorder(root.left, arr)
    postorder(root.right, arr)
    arr.append(root.data)


def post_order(root):
    arr = []
    postorder(root, arr)
    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = post_order(root)
    print("PostOrder Traversal: " , end=" ")
    for val in result:
        print(val, end=" ")
    print()