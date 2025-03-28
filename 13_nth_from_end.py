# This code is used to find the nth node from the end of a linked list
# Defining a class ListNode to create the nodes of a linked list
class ListNode:

    # The instance vairables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Defining a function to print the elements of a linked list
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

# Defining a function to insert a node at the start of a linked list
def insert_start(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# Defining a function to insert a node at the end of a linked list
def insert_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Defining a function to insert a node at a given position of a linked list
def insert_pos(head, val, position):
    new_node = ListNode(val)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    cur_pos = 0
    while current:
        if cur_pos + 1 == position:
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next
        cur_pos += 1
    return None # The position is out of range of the linked list

# Defining a function to delete a node from the start of a linked list
def delete_start(head):
    if head:
        return head.next
    return NotImplemented

# Defining a function to delete a node from the end of a linked list
def delete_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

# Defining a function to delete a node at a given position from a linked list
def delete_pos(head, position):
    if position == 0:
        return head.next
    current = head
    cur_pos = 0
    while current:
        if cur_pos + 1 == position:
            current.next = current.next.next
            return head
        current = current.next
        cur_pos += 1
    return None # The position is out of range for the linked list

# Defining a function to search the linked list for a given value
def search_ll(head, search_key):
    while head:
        if head.data == search_key:
            return True
        head = head.next
    return False

# Defining a function to reverse a linked list
def reverse_ll(head):
    previous = None
    current = head
    while current:
        new_node = current.next
        current.next = previous
        previous = current
        current = new_node
    return previous

# Defining a function to find the middle node of a linked list in a single pass
def middle_ll(head):
    if not head:
        return None
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.data

# Defining a function to get the nth node from the end of a linked list
def nth_from_end(head, n):
    if not head:
        return None
    if n < 1:
        return 'The value of n is invalid'
    main_ptr = head
    ref_ptr = head
    while n:
        if not ref_ptr:
            return 'n is greater than the no. of nodes in the linked list'
        ref_ptr = ref_ptr.next
        n -= 1
    while ref_ptr:
        ref_ptr = ref_ptr.next
        main_ptr = main_ptr.next
    return main_ptr.data

# Creating a few nodes to make a linked list
head = ListNode(10)
second = ListNode(8)
third = ListNode(1)
fourth = ListNode(11)
fifth = ListNode(15)

# Connecting the list nodes to form a linked list
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Printing the linked list before performing any operations
print_ll(head)
print(f'The length is {length_ll(head)}')

# Performing the operations using the defined functions
result = nth_from_end(head, 9)
print(result)

# Printing the linked list after performing the operations
print_ll(head)
print(f'The length is {length_ll(head)}')