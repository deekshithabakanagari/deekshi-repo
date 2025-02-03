# This code is to delete a node at a given position from a linked list
# Defining a class to create ListNodes
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Defining a function to print a linked list
def print_ll(head):
    while head:
        print(head.data, end=' --> ')
        head = head.next
    print('None')

# Defining a function to get the length of a linked list
def length_ll(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

# Defining a function to insert a node at the start of a linked list
def insert_start(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# Defining a function to insert a node at the end of a linked list
def insert_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Defining a function to insert a node at a given position of a linked list
def insert_pos(head, val, position):
    new_node = ListNode(val)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    cur_pos = 0
    while current:
        if cur_pos + 1 == position:
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next
        cur_pos += 1
    return None # The position is out of range of the linked list

# Defining a function to delete a node from the start of a linked list
def delete_start(head):
    if head:
        return head.next
    return None

# Defining a function to delete a node from the end of a linked list
def delete_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

# Defining a function to delete a node at a given position from a linked list
def delete_pos(head, position):
    if position == 0:
        return head.next
    current = head
    cur_pos = 0
    while current:
        if cur_pos + 1 == position:
            current.next = current.next.next
            return head
        current = current.next
        cur_pos += 1
    return None # The position is out of range for the linked list

# Creating a few nodes to make a linked list
head = ListNode(10)
second = ListNode(8)
third = ListNode(1)
fourth = ListNode(11)

# Connecting the nodes to form a linked list
head.next = second
second.next = third
third.next = fourth

# Printing the linked list before performing any operations
print_ll(head)
print(f'The length is {length_ll(head)}')

# Performing the operations using the defined functions
head = delete_pos(head, 2)

# Printing the linked list after performing the desired operations
print_ll(head)
print(f'The length is {length_ll(head)}')