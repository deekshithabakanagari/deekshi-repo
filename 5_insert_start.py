# This code is used to insert a node at the start of a doubly linked list
# Defining the class ListNode to create nodes for the doubly linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

# Defining a function to print the elements in forward direction
def print_dll_fwd(head):
    if head:
        print('None', end=' <--> ')
    while head:
        print(head.data, end=' <--> ')
        head = head.next
    print('None')

# Defining a function to print the elements in backward direction
def print_dll_bwd(tail):
    if tail:
        print('None', end=' <--> ')
    while tail:
        print(tail.data, end=' <--> ')
        tail = tail.prev
    print('None')

# Defining a function to get the length of a doubly linked list
def length_dll(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

# Defining a function to insert a node at the start of a doubly linked list
def insert_start(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    new_node.next = head
    head.prev = new_node
    return new_node

# Creating a few nodes to make a linked list
head = ListNode(1)
second = ListNode(10)
third = ListNode(15)
tail = ListNode(65)

# Connecting the nodes to form the linked list
head.next = second
second.next, second.prev = third, head
third.next, third.prev = tail, second
tail.prev = third

# Printing the doubly linked list in fwd direction
print_dll_fwd(head)

# Printing the doubly linked list in bwd direction
print_dll_bwd(tail)

# Printing the length of doubly linked list using the function
print(f'The length is {length_dll(head)}')

# Inserting a new node at the start using a function
head = insert_start(head, 24)

# Printing the doubly linked list fwd, bwd and printing the length
print_dll_fwd(head)
print_dll_bwd(tail)
print(f'The length is {length_dll(head)}')