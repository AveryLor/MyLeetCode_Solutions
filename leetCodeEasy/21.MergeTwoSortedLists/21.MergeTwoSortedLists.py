# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        while list1 and list2: # Iterate through the entire list 
            if list1.val >= list2.val: #If the current value of list 1 is greater  
                cur.next = list2 # We append the current node to
                list2 = list2.next # Moving to the next node 
            else: # Otherwise, we append to the merged list and move list1 to the pointer 
                cur.next = list1 #Otherwise, the list1 value is less which means that we append it 
                list1 = list1.next #We move further in the list1 
            
            cur = cur.next #Moving further along

        if list1: #If there are remaining nodes in either list1 or list2 we append them 
            cur.next = list1
        else: 
            cur.next = list2
            
        return dummy.next #We return the next node after the dummy node, which is the head of the merged list

        