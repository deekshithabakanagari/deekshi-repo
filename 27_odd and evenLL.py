class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print("None")


def segevenandodd(head):
    arr = []
    temp = head
    while temp:
        arr.append(temp.data)
        temp = temp.next.next
    if temp:
        arr.append(temp.data)
    temp = head.next
    while temp and temp.next:
        arr.append(temp.data)
        temp = temp.next.next
    if temp:
        arr.append(temp.data)
    i = 0
    temp = head
    while i<len(arr):
        temp.data = arr[i]
        i+=1
        temp = temp.next
    return head


def evenoddseg(head):
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next
    evenhead = head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next.next

    odd.next = evenhead
    return head

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth

printLL(head)

result = evenoddseg(head)

printLL(result)