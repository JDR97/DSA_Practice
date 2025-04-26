class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LLSize(root):
    if root is None:
        return 0
    size = 0
    while(root):
        size += 1
        root = root.next

    return size

def removeNode(head, idx):
    if head is None:
        return None
    
    if head.next is None and idx == 1:
        return None
    
    fast = head
    slow = head

    for _ in range(idx):
        fast = fast.next

    if fast is None:
        return head.next
    
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head
    

def printLL(root):
    if root is None:
        return
    while(root):
        print(root.data, end=" ")
        root = root.next

    print()


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Linked List Before: ", end = " " )
    printLL(head)
    head = removeNode(head, 3)
    print("Linked List After: ", end= " ")
    printLL( head)