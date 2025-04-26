##We can use Morris traversal but that needs understanding. Will do later
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isIdentical(r1, r2):
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False
    
    d1 = deque([r1])
    d2 = deque([r2])

    while d1 and d2:
        n1 = d1.popleft()
        n2 = d2.popleft()

        if n1.data != n2.data:
            return False
        
        if n1.left and n2.left:
            d1.append(n1.left)
            d2.append(n2.left)
        elif n1.left or n2.left:
            return False
        
        if n1.right and n2.right:
            d1.append(n1.right)
            d2.append(n2.right)
        elif n1.right or n2.right:
            return False
        
    return not d1 and not d2


    
if __name__ == "__main__":
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(5)

    r2 = Node(1)
    r2.left = Node(2)
    r2.right = Node(3)
    r2.left.left = Node(4)

    if(isIdentical(r1, r2)):
        print("Yes")
    else:
        print("NO")