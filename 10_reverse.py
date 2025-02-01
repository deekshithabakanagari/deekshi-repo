# This code is used to reverse a doubly linked list
# Defining a class ListNode to create nodes of the doubly linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

# Defining a function to print the elements in fwd direction
def print_dll_fwd(head):
    if head:
        print('None', end=' <--> ')
    while head:
        print(head.data, end=' <--> ')
        head = head.next
    print('None')

# Defining a function to print the elements in bwd direction
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

# Defining a function to insert a node at the start of doubly linked list
def insert_start(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    new_node.next = head
    head.prev = new_node
    return new_node

# Defining a function to insert a node at the end of doubly linked list
def insert_end(head, end, val): # Tail is written as end to maintain tail as a global variable, not a parameter
    new_node = ListNode(val)
    global tail
    if not head:
        tail = new_node
        return new_node
    end.next = new_node
    new_node.prev = end
    tail = new_node
    return head

# Defining a function to delete a node from the start of a doubly linked list
def delete_start(head):
    if not head or not head.next:
        global tail
        tail = None
        return None
    head = head.next
    head.prev = None
    return head

# Defining a function to delete a node from the endo of a doubly linked list
def delete_end(head, end): # Tail is written as end to maintain tail as a global variable, not a parameter
    global tail
    if not head or not head.next:
        tail = None
        return None
    end = end.prev
    end.next = None
    tail = end
    return head

# Defining a function to insert a node into a sorted doubly linked list
def insert_sorted(head, val):
    new_node = ListNode(val)
    global tail
    if not head:
        tail = new_node
        return new_node
    if new_node.data < head.data:
        new_node.next = head
        head.prev = new_node
        return new_node
    current = head
    while current.next and current.next.data > new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    new_node.prev = current
    if new_node.next:
        new_node.next.prev = new_node
    else:
        tail = new_node
    return head

# Defining a function to reverse a doubly linked list
def reverse_dll(head):
    if not head or not head.next:
        return head
    global tail
    tail = head
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        current.prev = next_node
        previous = current
        current = next_node
    return previous

# Creating a few nodes to make a doubly linked list
head = ListNode(1)
second = ListNode(10)
third = ListNode(15)
tail = ListNode(65)

# Connecting the nodes to form a doubly linked list
head.next = second
second.next, second.prev = third, head
third.next, third.prev = tail, second
tail.prev = third

# Printing the doubly linked list in both directions before performing any operations
print_dll_fwd(head)
print_dll_bwd(tail)
print(f'The length is {length_dll(head)}')

# Inserting a node at the start
head = insert_start(head, 24)

# Inserting a node at the end
head = insert_end(head, tail, 35)

# Deleting a node from the start
head = delete_start(head)

# Deleting a node from the end
head = delete_end(head, tail)

# Inserting a node into sorted linked list
# head = insert_sorted(head, 12)

# Reversing the linked list
head = reverse_dll(head)

# Printing the doubly linked list in both directions before performing any operations
print_dll_fwd(head)
print_dll_bwd(tail)
print(f'The length is {length_dll(head)}')