# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        current = head
        n = 0

        while current:
            current = current.next
            n += 1

        middle = n // 2

        current = head
        if (current.next):
            for i in range(middle - 1):
                current = current.next
            
            current.next = current.next.next
        else:
            head = None

        return head
            

