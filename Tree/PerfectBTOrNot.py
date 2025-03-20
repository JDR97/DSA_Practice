from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def depth(root):
    if root is None:
        return 0
    else:
        return 1 + max(depth(root.left), depth(root.right))
    
def isPerfectRecurr(root, d):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return d == 1
    
    if root.left is None or root.right is None:
        return False
    
    return isPerfectRecurr(root.left, d-1) and isPerfectRecurr(root.right, d-1)
    
def isPerfect(root):
    d = depth(root)
    return isPerfectRecurr(root, d)

#Using queue and checking the number of node from condition
def isPerfect2(root):
    
    if root is None:
        return True
    
    q = deque([root])
    
    # to store the expected node 
    # count at a given level.
    nodeCnt = 1
    
    while q:
        size = len(q)
        
        # If number of expected nodes is 
        # not same, return False.
        if size != nodeCnt:
            return False
        
        while size > 0:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            size -= 1
        
        # Next level will contain twice
        # number of nodes.
        nodeCnt *= 2
    
    return True


if __name__ == "__main__":
    
    # Binary tree 
    #           10
    #        /     \  
    #      20       30  
    #     /  \     /  \
    #   40    50  60   70
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    if isPerfect(root):
        print("True")
    else:
        print("False")