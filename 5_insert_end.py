# This code adds a new node at the end of a linked list
# The class definition to create listnodes 
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

# Defining a function to count the elements of a linked list
def length_ll(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

# Defining a function to insert a node at the start of linked list
def insert_start(head, val):
    new_head = ListNode(val)
    new_head.next = head
    head = new_head

# Defining a function to insert a node at the end of linked list
def insert_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Creating a few nodes to make the linked list
head = ListNode(10)
second = ListNode(1)
third = ListNode(8)
fourth = ListNode(11)

# Connecting the listnodes to form a linked list
head.next = second
second.next = third
third.next = fourth

# Printing the linked list before inserting an element
print_ll(head)
print(f'The length is {length_ll(head)}')

# Inserting an element at the end of the linked list
head = insert_end(head, 4)

# Printing the linked list after inserting an element
print_ll(head)
print(f'The lenght is {length_ll(head)}')