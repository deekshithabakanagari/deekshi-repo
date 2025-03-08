class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head:
        print(head.data, end="-->")
        head = head.next
    print(None)


def kthfromstart(head,k):
    while head:
        k-=1
        if k==0:
            return head.data
        head=head.next
    return None


head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(2)
fifth = ListNode(8)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth


printLL(head)

result = kthfromstart(head,3)

print(result)


