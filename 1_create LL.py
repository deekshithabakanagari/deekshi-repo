class ListNode:
    def __init__(self,data):
      self.data = data 
      self.next = None

head = ListNode(10)
second = ListNode(2)
third = ListNode(7)
fourth = ListNode(200)

head.next = second
second.next = third
third.next = fourth
