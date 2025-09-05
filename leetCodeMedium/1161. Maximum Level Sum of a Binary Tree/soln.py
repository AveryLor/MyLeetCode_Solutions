# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curMax = float(-inf)
        cur = 0
        level = 0
        soln = 0

        q = deque([root])

        # Get the max at every level and then compare it to the current max

        while (q):
            level += 1
            cur = 0
            for i in range(len(q)):
                node = q.popleft()      

                if node:
                    cur += node.val
                    q.append(node.left)
                    q.append(node.right)
            if q: 
                if cur > curMax:
                    curMax = cur
                    soln = level

                
        
        
        return soln