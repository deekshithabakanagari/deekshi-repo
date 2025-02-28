# This code is to delete a key from a given linked list
# Defining a class ListNode to create the nodes of a linked list
class ListNode:

    # The instance variables...
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

# Defining a function to insert a node to the start of a linked list
def insert_start(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# Defining a function to insert a node to the end of a linked list
def insert_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Defining a function to insert a node at a given position in a linked list
def insert_pos(head, val, position):
    new_node = ListNode(val)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    cur_pos = 0
    while current:
        if cur_pos + 1 == position:
            new_node.next = current
            current.next = new_node
            return head
        current = current.next
        cur_pos += 1
    return None # The position is out of range for the given linked list

# Defining a function to delete the node at the start of a linked list
def delete_start(head):
    if head:
        return head.next
    return None

# Defining a function to delete the node at the end of a linked list
def delete_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

# Defining a function to delete the node at a given position from a linked list
def delete_position(head, position):
    if position == 0:
        return head.next
    current = head
    cur_pos = 0
    while current.next:
        if cur_pos + 1 == current:
            current.next = current.next.next
            return head
        current = current.next
        cur_pos += 1
    return None # The position is out of range for the linked list

# Defining a function to search for a key in a linked list
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
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

# Defining a function to get the middle value of a linked list
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
        return 'The value of n should be greater than or equal to 1'
    ref_ptr = head
    main_ptr = head
    while n:
        if not ref_ptr.next:
            return 'The value of n is greater than the length of linked list'
        ref_ptr = ref_ptr.next
        n -= 1
    while ref_ptr:
        ref_ptr = ref_ptr.next
        main_ptr = main_ptr.next
    return main_ptr.data

# Defining a function to remove duplicates from a linked list
def rem_duplicates(head):
    if not head or not head.next:
        return head
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Defining a function to  insert a node into a sorted linked list
def insert_sorted(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    if new_node.data < head.data:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

# Defining a function to delete a given element from a linked list
def delete_key(head, key):
    if head.data == key:
        return head.next
    current = head
    while current.next:
        if current.next.data == key:
            current.next = current.next.next
            return head
        current = current.next
    return None # The key is not present in the linked list

# Creating a few nodes to make a linked list
head = ListNode(1)
second = ListNode(8)
third = ListNode(10)
fourth = ListNode(11)
fifth = ListNode(16)

# Linking all the nodes to form a linked list
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Printing the linked list before performing any operations
print_ll(head)
print(f'The length is {length_ll(head)}')

# Performing operations using the defined functions
head = delete_key(head, 16)

# Printing the linked list after performing the operations
print_ll(head)
print(f'The length is {length_ll(head)}')