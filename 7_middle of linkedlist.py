class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print(None)

def lengthLL(head):
    length = 0
    while(head):
        length+=1
        head=head.next
    return length

def middleLL(head):
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


head = ListNode(2)
f = ListNode(5)
s = ListNode(28)
t = ListNode(23)

head.next = f
f.next = s
s.next = t


middle = middleLL(head)

printLL(middle)

