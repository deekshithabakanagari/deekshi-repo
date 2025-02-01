# This is the code to create a linked list
# The class to implement a ListNode
class ListNode:

    # The init method with one instance variable
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Creating ListNode objects 
head = ListNode(10)
second = ListNode(1)
third = ListNode(8)
fourth = ListNode(11)

# Connecting the nodes of the list 
head.next = second
second.next = third
third.next = fourth


# This code only creates a linked list
# There is no direct way to visualize a linked list
# In the next file, I will define a function to print a linked list