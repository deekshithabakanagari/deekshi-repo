# This code is used to print the element of a doubly linked list in backward direction
# Defining the class ListNode to make the nodes of a doubly linked list
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

# Creating a few nodes to make a doubly linked list
head = ListNode(1)
second = ListNode(10)
third = ListNode(15)
tail = ListNode(25)

# Connecting the ListNodes to form a doubly linked list
head.next = second
second.next, second.prev = third, head
third.next, third.prev = tail, second
tail.prev = third

# Printing the doubly linked list in forward direction
print_dll_fwd(head)

# Printing the doubly linked list in backward direction
print_dll_bwd(tail)