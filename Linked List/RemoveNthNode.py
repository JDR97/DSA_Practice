class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

def removeNNode(arr, N):
    fastp = head
    slowp = head

    for i in range(N):
        fastp = fastp.next

    if fastp is None:
        return head.next
    
    while fastp.next is not None:
        fastp = fastp.next
        slowp = slowp.next

    delNode = slowp.next
    slowp.next = slowp.next.next
    delNode = None
    return head

def printLL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    head = removeNNode(head, N)

    printLL(head)