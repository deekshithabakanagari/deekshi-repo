# This code is used to find the length of a doubly linked list
# Defining a class to create ListNodes for doubly linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

# Defining a function to print the elements of a doubly linked list in forward direction
def print_dll_fwd(head):
    if head:
        print('None', end=' <--> ')
    while head:
        print(head.data, end=' <--> ')
        head = head.next
    print('None')

# Defining a function to print the elements of a doubly linked list in backward direction
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

# Creating a few nodes to make a linked list
head = ListNode(1)
second = ListNode(10)
third = ListNode(15)
fourth = ListNode(20)
tail = ListNode(25)

# Connecting the nodes to form a doubly linked list
head.next = second
second.next, second.prev = third, head
third.next, third.prev = fourth, second
fourth.next, fourth.prev = tail, third
tail.prev = fourth

# Printing the doubly linked list in forward direction
print_dll_fwd(head)

# Printing the doubly linked list in backward direction
print_dll_bwd(tail)

# Getting and printing the length of the doubly linked list
print(f'The length is {length_dll(head)}')