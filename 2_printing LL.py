class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print("None")

head = ListNode(11)
second = ListNode(12)
third = ListNode(13)
fourth = ListNode(14)

head.next = second
second.next = third
third.next = fourth

printLL(head)