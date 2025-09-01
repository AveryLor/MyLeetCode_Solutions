# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # DFS Solution (Typically with stack LIFO data type)
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            
            # Ignores null nodes
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1]) # Drills down until it is stopped
                stack.append([node.right, depth + 1])
        
        return res