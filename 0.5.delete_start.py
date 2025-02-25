class ListNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


def printDLL(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print() 


def del_start(head):
    if head is None:
        return None
    temp = head
    head = head.next
    if head is not None:
        head.prev = None
    return head


head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth 
fourth.prev = third 
fourth.next = fifth

printDLL(head)

head = del_start(head)

printDLL(head)

     
