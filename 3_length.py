# This code is used to get the length of a linked list
# The class definition to create a ListNode
class ListNode:

    # The instance variables are defined in init method
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Defining a function to print the elements of the linked list
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

# Creating ListNode objects to create a linked list
head = ListNode(10)
second = ListNode(1)
third = ListNode(8)
fourth = ListNode(11)

# Connecting the ListNodes to form a linked list
head.next = second
second.next = third
third.next = fourth

# Calling the print and length functions
print_ll(head)
print(f'The length is {length_ll(head)}')