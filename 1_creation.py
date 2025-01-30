# This code is used to create a doubly linked list
# The class definition to create the ListNode for doubly linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

# Creating a few nodes to make the doubly linked list
head = ListNode(1)
second = ListNode(10)
third = ListNode(15)
tail = ListNode(25)

# Connecting the nodes to form a doubly linked list
head.next = second
second.next, second.prev = third, head
third.next, third.prev = tail, second
tail.prev = third

# This code only creates a doubly linked list
# There is no direct way to visualize a doubly linked list
# In the next file, I will define a function to print the elements of a doubly linked list