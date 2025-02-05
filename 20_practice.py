# This is for the actual implementation of linked list using classes
# The class definition for creating a linked list
class ListNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Defining another class to make a singly linked list
class SinglyLinkedList:

    # The class variables
    head = None

    # Defining a method to print the elements of a linked list
    def print_ll(self):
        while self.head:
            print(self.head.data, end=' --> ')
            self.head = self.head.next
        print('None')

    # Defining a function to get the length of a linked list
    def length_ll(self):
        length = 0
        while self.head:
            length += 1
            self.head = self.head.next
        return length
    
    # Defining a function to insert a node at the start of a linked list
    def insert_start(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    # Defining a function to insert a node at the end of a linked list
    def insert_end(self, val):
        new_node = ListNode(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Defining a function to insert a node at a given position
    # This method must have an edge case of inserting at start
    def insert_pos(self, val, pos):
        new_node = ListNode(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_pos = 0
        current = self.head
        while pos != current_pos + 1:
            current = current.next
            current_pos += 1
        new_node.next = current.next
        current.next = new_node

    # Defining a function to delete a node from the start of linked list
    def delete_start(self):
        if self.head:
            self.head = self.head.next

    # Defining a function to delete a node from the end of a linked list
    def delete_end(self):
        if not self.head or not self.head.next:
            return
        current = self.head.next
        while current.next.next:
            current = current.next
        current.next = None

    # Defining a function to delete a node from a given position
    def delete_pos(self, pos):
        if pos == 0 and self.head:
            self.head = self.head.next
            return
        cur_pos = 0
        current = self.head
        while cur_pos < pos:
            current = current.next
            cur_pos += 1
        current.next = current.next.next

    # Defining a function to search for a key in a linked list
    def search_ll(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False


my_ll = SinglyLinkedList()
my_ll.insert_start(1)
my_ll.insert_end(3)
my_ll.insert_end(4)
my_ll.insert_end(5)
my_ll.insert_pos(2, 1)
my_ll.print_ll()