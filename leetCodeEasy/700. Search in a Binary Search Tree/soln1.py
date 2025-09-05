# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        q = deque([root])
        soln = []

        while q:
            node = q.popleft()
            if node: 
                # Less than move left
                if val < node.val:
                    q.append(node.left)
                
                # More than move right
                if val > node.val: 
                    q.append(node.right)
                
                elif node.val == val:
                    return node

     
        
        


        

        