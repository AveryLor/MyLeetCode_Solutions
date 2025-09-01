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
        if not root:
            return 0

        def dfs(root, curr_sum):
            if not root:
                return 0
            
            curr_sum += root.val
            # Number of valid paths ending here
            count = prefix[curr_sum - targetSum] # prefix[old_sum]
            # curr_sum = old_sum + target_sum, if valid path

            # Add current sum to map
            prefix[curr_sum] += 1

            # Recurse children
            count += dfs(root.left, curr_sum)
            count += dfs(root.right, curr_sum)

            # Backtrack
            prefix[curr_sum] -= 1
            return count
        
        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)

        