###Reverse the linked list from given start and end index
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

def reverse_ll_II(head, start, end):
    if not head or start == end:
        return head
    
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for _ in range(start-1):
        prev = prev.next

    cur = prev.next

    for _ in range(end-start):
        temp = cur.next
        cur.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next



def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data, end="")
        temp = temp.next

    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print("Original LL:", end="")
print_ll(head)
start = 2
end = 4
head = reverse_ll_II(head, start, end)

print("Reversed Linked List:", end="")
print_ll(head)