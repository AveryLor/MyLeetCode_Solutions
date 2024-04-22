# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # Dummy node to start the result linked list
        current = dummy  # Pointer to the current node in the result linked list
        carry = 0  # Variable to store the carry during addition
        
        # Traverse both input linked lists simultaneously
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 or default to 0
            val2 = l2.val if l2 else 0  # Get value from l2 or default to 0
            
            # Calculate the sum of current digits and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next digit
            
            # Create a new node with the sum digit and add it to the result linked list
            current.next = ListNode(total % 10)
            current = current.next  # Move to the next node in the result
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next  # Return the next node after the dummy (the actual result)
     
        