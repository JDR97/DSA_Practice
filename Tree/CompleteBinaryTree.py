class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildBST(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    q = [root]
    i = 1
    while i < len(nums):
        cur = q.pop(0)
        if i < len(nums):
            cur.left = TreeNode(nums[i])
            q.append(cur.left)
            i += 1
        if i < len(nums):
            cur.right = TreeNode(nums[i])
            q.append(cur.right)
            i += 1
    return root

def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.data, end=" ")
    printTree(root.right)



nums = [1, 2, 3, 4, 5, 6, 6, 6, 6]
root = buildBST(nums)
printTree(root)
