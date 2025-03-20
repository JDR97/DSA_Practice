class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def isBalanced(root):
    if root is None:
        return True
    
    lheight = height(root.left)
    rheight = height(root.right)

    if( abs(lheight - rheight) > 1):
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)

#Optimizing by calculating height with recursive function 
def isBalancedRec(root):
  
    # Base case: Height of empty tree is zero
    if root is None:
        return 0

    # Find Heights of left and right subtrees
    lHeight = isBalancedRec(root.left)
    rHeight = isBalancedRec(root.right)

    # If either of the subtrees are unbalanced or the absolute difference  
    # of their heights is greater than 1, return -1
    if lHeight == -1 or rHeight == -1 or abs(lHeight - rHeight) > 1:
        return -1

    # Return the height of the tree
    return max(lHeight, rHeight) + 1

# Function to check if the tree is height balanced
def isBalanced2(root):
    return isBalancedRec(root) > 0


if __name__ == "__main__":
    # Representation of input BST:
    #            1
    #           / \
    #          2   3
    #         /  \
    #        4   5 
    #       /
    #      8
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    print("True" if isBalanced(root) else "False")

