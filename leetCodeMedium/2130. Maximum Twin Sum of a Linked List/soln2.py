# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        slow, fast = head, head
        maxVal = 0

        # Get middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second part of linked list
        curr, prev = slow, None

        # 2 -> 3 -> None
        # Iteration 1 
        # prev = 2 -> None
        # current = 3 - > None

        # Iteration 2
        # temp = None
        # current.next = 3 -> 2 -> None
        # prev = 3 -> None
        # current = None
        while curr:       
            temp = curr.next
            curr.next = prev
            prev = curr # move up prev
            curr = temp

        # Get max sum of pairs
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal 
                






        