# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        list = []

        # Recursive solution 
        def function(x):
            if not x: # If we are not looking at x leave 
                return 
            function(x.left) # Otherwise we should continually look left 
            list.append(x.val) # Append the value to the list 
            function(x.right) # And go the other way recursively

        function(root)
        return list