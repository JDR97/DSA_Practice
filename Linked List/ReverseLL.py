class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next =  next_node

def reverse_ll(head):
    temp = head
    prev = None

    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev

#Recursive Approach
def reverse_ll2(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverse_ll2(head.next)

    front = head.next
    front.next = head
    head.next = None

    return new_head
    



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
print("Original LL:", end="")
print_ll(head)

head = reverse_ll2(head)

print("Reversed Linked List:", end="")
print_ll(head)
