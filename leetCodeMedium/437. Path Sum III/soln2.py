# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.total = 0

        def helper(node, cur):
            if not node:
                return 0
            
            helper(node.left, cur+node.val)
            helper(node.right, cur+node.val)

            if cur + node.val == targetSum:
                self.total += 1

        def dfs(root):
            if not root:
                return 0
            
            helper(root, 0)

            # Traverse both sides of the tree
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return self.total

