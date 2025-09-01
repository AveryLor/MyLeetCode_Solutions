# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        

        def dfs(root, isLeft, depth): # True for "yes we have gone left"
            if not root:
                return depth

            if isLeft: # Move to the right
                depth = max(
                    depth,
                    dfs(root.right, False, depth + 1),
                    dfs(root.left, True, 0)
                )

            else: # Move to the left
                depth = max(
                    depth, 
                    dfs(root.left, True, depth + 1),
                    dfs(root.right, False, 0)
                )
            
            return depth

        
        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))



        