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
        length+=1
        head=head.next
    return length

def rotateRight(head,k):
        if not head:
            return head

        #get length
        length,tail = 1,head
        while tail.next:
                tail = tail.next
                length +=1
            
        k = k%length 
        if k == 0:
            return head

        cur = head
        for i in range(length-k-1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead

def anticlockwise(head,k):
        if not head:
            return head

        #get length
        length,tail = 1,head
        while tail.next:
                tail = tail.next
                length +=1
            
        k = k%length 
        if k == 0:
            return head


        cur = head
        for i in range(k-1):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        tail.next =  head
        return newhead


first = ListNode(1)
second = ListNode(2)
third= ListNode(3)
fourth = ListNode(4)
fifth= ListNode(5)

head = first
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth


printLL(head)
head = rotateRight(head,2)

printLL(head)
head = anticlockwise(head,3)

printLL(head)