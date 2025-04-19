class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_list(l1, l2):
    dummy = Node(-1)
    temp = dummy

    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next

        temp = temp.next

    if l1 is not None:
        temp.next = l1
    else:
        temp.next = l2

    return dummy.next

def print_linkedlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end= " ")
        temp = temp.next

    print()

if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(5)

    list2 = Node(3)
    list2.next = Node(4)
    list2.next.next = Node(7)

    print_linkedlist(list1)
    print_linkedlist(list2)

    merged_list = sorted_list(list1, list2)

    print_linkedlist(merged_list)