# This code is used to delete the last node of a doubly linked lists
# Defining a class ListNode to create nodes of a doubly linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

# Defining a function to print the elements of a doubly linked list in fwd direction
def print_dll_fwd(head):
    if head:
        print('None', end=' <--> ')
    while head:
        print(head.data, end=' <--> ')
        head = head.next
    print('None')

# Defining a function to print the elements of a doubly linked list in bwd direction
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

# Defining a function to insert node at the start of a doubly linked list
def insert_start(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    new_node.next = head
    head.prev = new_node
    return new_node

# Defining a function to insert a node at the end of a doubly linked list
def insert_end(head, end, val): # The tail is written as end to maintain tail as a global variable and not a parameter
    new_node = ListNode(val)
    global tail
    if not head:
        tail = new_node
        return tail
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

# Defining a function to delete a node from the end of a doubly linked list
def delete_end(head, end): # The tail is written as end to maintain tail as a global variable and not a parameter
    global tail
    if not head or not head.next:
        tail = None
        return None
    end = end.prev
    end.next = None
    tail = end
    return head

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
head = insert_end(head, tail, 11)
head = insert_end(head, tail, 21)

# Deleting a node from the start using the function
head = delete_start(head)

# Deleting a node from the end using the function
head = delete_end(head, tail)

# Printing the doubly linked list in both directions before performing any operations
print_dll_fwd(head)
print_dll_bwd(tail)
print(f'The length is {length_dll(head)}')

# Printing the head and tail values
print(f'Head = {head.data}, Tail = {tail.data}')