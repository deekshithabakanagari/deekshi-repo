# This code is used to create and print a linked list
# First a class ListNode is defined to create nodes
class ListNode:

    # The instance variables are defined in the init method
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Defining a function to print the elements of linked list
def print_ll(head):
    while head:
        print(head.data, end=' --> ')
        head = head.next
    print('None')

# Creating a few ListNode objects
head = ListNode(10)
second = ListNode(1)
third = ListNode(8)
fourth = ListNode(11)

# Connecting the ListNodes to form a Linked List
head.next = second
second.next = third
third.next = fourth

# Using the print_ll function to print the linked list
print_ll(head=head)