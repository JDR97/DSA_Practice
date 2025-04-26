###This can be solved be O(n) TC also. Finding inorder and postorder traversal or
## inorder and preorder traversal. Then the arrays need to sub array of the first tree's 
# array.

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    # Check if data and left/right subtrees are identical
    return (root1.data == root2.data and
            isIdentical(root1.left, root2.left) and
            isIdentical(root1.right, root2.right))

def isSubtree(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False
    
    # Check if the current node of root1 matches
    # the root of root2
    if isIdentical(root1, root2):
        return True

    # Recur for left and right subtrees of root1
    return isSubtree(root1.left, root2) or isSubtree(root1.right, root2)


if __name__ == "__main__":
  
    # Construct Tree root1
    #          26
    #         /  \
    #        10   3
    #       / \    \
    #      4   6    3
    #       \
    #        30
    root1 = Node(26)
    root1.right = Node(3)
    root1.right.right = Node(3)
    root1.left = Node(10)
    root1.left.left = Node(4)
    root1.left.left.right = Node(30)
    root1.left.right = Node(6)

    # Construct Tree root2
    #          10
    #         /  \
    #        4    6
    #         \
    #          30
    root2 = Node(10)
    root2.right = Node(6)
    root2.left = Node(4)
    root2.left.right = Node(30)

    if isSubtree(root1, root2):
        print("true")
    else:
        print("false")