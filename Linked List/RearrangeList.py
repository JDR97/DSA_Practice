class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverseLL(node):
    prev = None
    curr = node
    nextt = None

    while curr is not None:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt

    node = prev
    return node

def rearrange(node):
    #Find mid point using slow fast pointer
    slow = node
    fast = slow.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    #Divide the list in two halves
    node1 = node
    node2 = slow.next
    slow.next = None
    
    #Reverse the second half list
    node2 = reverseLL(node2)
   
    #Merge alternate nodes of two lists
    node = Node(0)
    curr = node

    while node1 is not None or node2 is not None:
        if node1 is not None:
            curr.next = node1
            curr = curr.next
            node1 = node1.next

        if node2 is not None:
            curr.next = node2
            curr = curr.next
            node2 = node2.next

    return node.next

def printlist(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = rearrange(head)
printlist(head)