class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printDLL(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print()


def insert_start(head,data):
        new_node = ListNode(data)
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

def insert_end(head,data):
    new_node = ListNode(data)
    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    return head
            

def insert_pos(head,position,data):
    if position == 0:
        new_node = ListNode(data)
        new_node.next = head
        head.prev = new_node
        return new_node
    temp = head
    pos = 0
    while temp:
        if pos+1 == position:
            new_node = ListNode(data)
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp
            if temp.next.next:
                temp.next.next.prev = new_node
            return head

        pos+=1
        temp = temp.next

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth 
fourth.prev = third

printDLL(head)

head = insert_start(head,5)

printDLL(head)

head = insert_end(head,100)

printDLL(head)

head=insert_pos(head,2,140)

printDLL(head)