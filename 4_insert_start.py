# This code is to insert a new ListNode at the start of a linked list
# Creating a ListNode class for creating a linked list
class ListNode:

    # Defining the init method with instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Defining a function to print the elements of linked list
def print_ll(head):
    while head:
        print(head.data, end=' --> ')
        head = head.next
    print('None')

# Defining a function to count the no. of elements
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

# Creating a few ListNode objects to create a linked list
head = ListNode(10)
second = ListNode(1)
third = ListNode(8)
fourth = ListNode(11)

# Connecting these ListNodes to form a linked list
head.next = second
second.next = third
third.next = fourth

# Printing the linked list before inserting a new node
print_ll(head)
print(f'The length of ll is {length_ll(head)}')

# Inserting a new node using the function
head = insert_start(head, 2)

# Printing the linked list after inserting a new node
print_ll(head)
print(f'The length of ll is {length_ll(head)}')