# This code is to insert a node at a given position in a linked list
# Creating a class to create listnodes
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

# Defining a function to insert a node at start
def insert_start(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# Defining a function to insert a node at end
def insert_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Defining a function to insert node at a given position
def insert_at_position(head, val, position):
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
    return None # The position is out of range for the linked list

# Creating a few listnodes for the linked list
head = ListNode(10)
second = ListNode(1)
third = ListNode(8)
fourth = ListNode(11)

# Connecting the listnodes to form a linked list
head.next = second
second.next = third
third.next = fourth

# Printing the linked list before insertion
print_ll(head)
print(f'The length is {length_ll(head)}')

# Inserting a node at postion 2 using the function
head = insert_at_position(head, 5, 2)

# Inserting a node at start
head = insert_start(head, 4)

# Inserting a node at end
head = insert_end(head, 3)

# Printing the linked list after insertion
print_ll(head)
print(f'The length is {length_ll(head)}')