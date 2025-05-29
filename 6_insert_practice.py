class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print(None)


def lengthLL(head):
    length = 0
    while head:
        length +=1
        head=head.next
    return length
    

def insert_start(head,val):
    new_Node = ListNode(val)
    new_Node.next = head
    return new_Node

def insert_end(head,val):
    new_Node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_Node
    return head

def insert_position(head,val,position):
    new_Node = ListNode(val)
    if position == 0:
        new_Node.next = head
        return new_Node
    current= head
    cur_pos = 0
    while current:
        if cur_pos+1 == position:
            new_Node.next = current.next
            current.next = new_Node
            return head
        current = current.next
        cur_pos+=1
    return None

head = ListNode(10)
first = ListNode(20)
second = ListNode(30)
third= ListNode(40)
fourth = ListNode(50)

head.next = first
first.next = second
second.next = third
third.next = fourth

printLL(head)

head = insert_start(head,60)
head = insert_end(head,70)
head = insert_position(head,45,3)

printLL(head)