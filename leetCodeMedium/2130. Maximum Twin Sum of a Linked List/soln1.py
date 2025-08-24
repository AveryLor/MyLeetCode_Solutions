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

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next # For cutting the linked list in half
            tmp = slow.next # For advancing
            slow.next = prev # Reverses link until half
            prev = slow # Moves up prev to slow
            slow = tmp # Moves up slow to slow.next which was stored in tm

        # Saving result as 0 for now, slow points to the next half, prev points to the later half
        res = 0
        while slow: 
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res






        