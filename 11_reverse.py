# This code is to reverse a linked list
# Creating a class ListNode to create nodes of a linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Defining a function to print the elements of a linked list
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
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Defining a function to insert a node at a given position in a linked list
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
    return None # The position if out of range for the linked list

# Defining a function to delete a node from the start of a linked list
def delete_start(head):
    if head:
        return head.next
    return None

# Defining a function to delete a node from the end of a linked list
def delete_end(head):
    if head is None or head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

# Defining a function to delete a node at a given position in a linked list
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

# Defining a function to search for a given element in a linked list
def search_ll(head, search_key):
    while head:
        if head.data == search_key:
            return True
        head = head.next
    return False

# Defining a function to reverse a linked list
def reverse_ll(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

# Creating a few nodes for the linked list
head = ListNode(10)
second = ListNode(8)
third = ListNode(1)
fourth = ListNode(11)

# Linking all the nodes to form the linked list
head.next = second
second.next = third
third.next = fourth

# Printing the linked list before performing any operations
print_ll(head)
print(f'The length is {length_ll(head)}')

# Performing the defined operations using functions
head = reverse_ll(head)

# Printing the linked list after performing the operations
print_ll(head)
print(f'The length is {length_ll(head)}')