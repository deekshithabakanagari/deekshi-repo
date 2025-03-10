class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head:
        print(head.data, end="-->")
        head = head.next
    print(None)

def getMiddle(head):
    if not head:
        return head
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeSortedLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

def sortLinkedList(head):
    if not head or not head.next:
        return head

    middle = getMiddle(head)
    right_head = middle.next
    middle.next = None

    left_sorted = sortLinkedList(head)
    right_sorted = sortLinkedList(right_head)

    return mergeSortedLists(left_sorted, right_sorted)


first = ListNode(4)
second = ListNode(2)
third = ListNode(1)
fourth = ListNode(5)
fifth = ListNode(3)

head = first
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth


printLL(head)
head = sortLinkedList(head)
printLL(head)
