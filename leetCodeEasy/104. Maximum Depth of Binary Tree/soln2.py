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
        # BFS Solution (Typically involves a Queue/Deque which is FIFO)
        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:

            for i in range(len(queue)): # len(queue) is evaluated once at the start of the for loop
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level += 1

        return level
        
