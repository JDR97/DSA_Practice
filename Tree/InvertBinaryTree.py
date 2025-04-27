##Using Stack (Invert binary tree is same as finding symmetric or not)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSymmetric(root):
    if root is None:
        return True
    
    s1 = []
    s2 = []

    s1.append(root.left)
    s2.append(root.right)

    while s1 and s2:
        node1 = s1.pop()
        node2 = s2.pop()

        if node1 is None and node2 is None:
            continue

        if node1 is None or node2 is None or node1.data != node2.data:
            return False
        
        s1.append(node1.left)
        s2.append(node2.right)

        s1.append(node1.right)
        s2.append(node2.left)

    return len(s1) == 0 and len(s2) == 0
    


if __name__ == "__main__":
  
    # Creating a sample symmetric binary tree
    #        1
    #       / \
    #      2   2
    #     / \ / \
    #    3  4 4  3
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(4)

    print(isSymmetric(root))