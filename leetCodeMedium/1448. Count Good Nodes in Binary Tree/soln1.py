# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # This should be a depth first search using recursion
        def dfs(root, curMax):
            if not root:
                return 0
            
            if root.val >= curMax:
                good = 1
            else:
                good = 0
            
            newMax = max(curMax, root.val)

            good += dfs(root.left, newMax)
            good += dfs(root.right, newMax)

            return good
        
        maxVal = dfs(root, root.val)
        
        return maxVal

