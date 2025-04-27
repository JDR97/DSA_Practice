class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

    return max(lheight, rheight) + 1

def printGivenLevel(node, level, ltr):
    if(node == None):
        return
    if level == 1:
        print(node.data, end= " ")
    else:
        if(ltr):
            printGivenLevel(node.left, level-1, ltr)
            printGivenLevel(node.right, level-1, ltr)
        else:
            printGivenLevel(node.right, level-1, ltr)
            printGivenLevel(node.left, level-1, ltr)

def printSpiral(root):
    h = height(root)

    ltr = False
    for i in range(1, h+1):
        printGivenLevel(root, i, ltr)

        ltr = not ltr

##Using two stacks and Time complexity with O(n)
def printSpiral2(root):
    if root is None:
        return
    s1 = [] ##To print level from right to left
    s2 = []  ##To print level from left to right

    s1.append(root)

    while not len(s1) == 0 or not len(s2) == 0:
        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.data, end = " ")

            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while not len(s2) == 0:
            temp = s2[-1]
            s2.pop()
            print(temp.data, end = " ")

            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    print("Spiral Order traversal of binary tree is")
    printSpiral2(root)