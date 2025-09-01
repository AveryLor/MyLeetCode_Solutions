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

        if not root:
            return 0

        queue = deque([(root, root.val)])
        count = 0

        while queue:
            node, curMax = queue.popleft()

            if node.val >= curMax:
                count += 1
            
            curMax = max(curMax, node.val)

            if node.left:
                queue.append((node.left, curMax))
            
            if node.right:
                queue.append((node.right, curMax))
        
        return count
