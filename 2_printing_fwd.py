# This code is used to create and print a linked list from head to tail
# Defining the class ListNode to create the nodes 
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

# Creating a few nodes to make a doubly linked list
head = ListNode(1)
second = ListNode(10)
third = ListNode(15)
tail = ListNode(25)

# Connecting the listnodes to form the doubly linked list
head.next = second
second.next, second.prev = third, head
third.next, third.prev = tail, second
tail.prev = third

# Printing the doubly linked list using the print_dll function
print_dll_fwd(head)