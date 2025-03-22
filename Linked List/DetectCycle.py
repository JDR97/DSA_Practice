class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def detect_loop(head):
    temp = head
    node_set = set()
    while temp is not None:
        if temp in node_set:
            return True
        node_set.add(temp)
        temp = temp.next

    return False


#Optimized Method
def detect_loop2(head):
    slow = head
    fast = head

    while(fast and fast.next):
        slow =  slow.next
        fast = fast.next.next

        if(slow == fast):
            return True

    return False



if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if detect_loop2(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")