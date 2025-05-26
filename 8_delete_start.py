class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print("None")

def lengthLL(head):
    length = 0
    while head:
        head = head.next
        length += 1
    return length

def insert_start(head,val):
    new



head = ListNode(11)
second = ListNode(12)
third = ListNode(13)
fourth = ListNode(14)
fifth = ListNode(15)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

printLL(head)