class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    ##Finding Max Depth of the Tree
    def maxDepth(self, root):
        if root is None:
            return 0
        
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return 1+max(lh, rh)
    
    ##Invert the Tree
    def invertTree(self, root):
        if not root:
            return None
        
        temp  = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
    def isSymmetric(self, root):
        # Helper function to check if two trees are mirrors of each other
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.data == t2.data) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        if not root:
            return True
        return isMirror(root.left, root.right)


if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(4)
    root.right.left = Node(9)
    
    solution = Solution()
    depth = solution.maxDepth(root)
    print("Maximum depth of the binary tree:", depth)

    if solution.isSymmetric(root):
        print("The Tree is Symmetric")
    else:
        print("Not Symmetric")