# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def leafSimilar(self, root1, root2):
        if not root1 or not root2:
            return False

        def get_leaves(root):
            q = deque([root])
            leaves = []
            while q:
                node = q.popleft()
                if not node.left and not node.right:  # it's a leaf
                    leaves.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return leaves

        return get_leaves(root1) == get_leaves(root2)
