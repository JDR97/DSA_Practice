#Traversing a BST level order, Queue

class Node:
    def __init__(self, val):
        self.data =  val
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return []
    
    q = [] #do not need deque (can use though), as always 0th element will be removed
    res = []

    q.append(root)
    curr_level = 0

    while q:
        len_q = len(q)
        res.append([])

        for _ in range(len_q):
            node = q.pop(0)
            res[curr_level].append(node.data)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

        curr_level += 1 #Increases only adding element to queue of one level is done, so res.append([]) at the beginnig of while makes sense
    
    return res



if __name__ == '__main__':
    #      5
    #     / \
    #   12   13
    #   /  \    \
    #  7    14   2
    # /  \   /  \  / \
    #17 23 27  3  8  11

    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    # Perform level order traversal and get the result
    res = level_order(root)

    # Print the result in the required format
    for level in res:
        print('[', end='')
        print(', '.join(map(str, level)), end='')
        print('] ', end='')