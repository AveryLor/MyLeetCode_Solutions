# def star_trace(n):
#     if n == 0:
#         print('(base case)')
#         return
    
#     # Print stars for this level
#     print('*' * n)
    
#     # Recurse once
#     star_trace(n - 1)
    
#     # Recurse again
#     star_trace(n - 1)
    
#     # Indicate returning
#     print('x' * n)

# # Run it
# star_trace(3)

# def star_trace(n, depth=0):
#     if n == 0:
#         print('  ' * depth + '* (base case)')
#         return
    
#     # Print stars for this level
#     print('  ' * depth + '*' * n)
    
#     # Recurse once
#     star_trace(n - 1, depth + 1)
    
#     # Recurse again
#     star_trace(n - 1, depth + 1)
    
#     # Indicate returning
#     print('  ' * depth + '* done')

# # Run it
# star_trace(3)


from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        def collect_leaf_values(root, leaf_values, depth=0):
            indent = '  ' * depth  # indent to visualize stack depth
            if not root:
                print(f"{indent}Called with None -> return")
                return
            
            print(f"{indent}Called with node {root.val}")
            
            if not root.left and not root.right:
                leaf_values.append(root.val)
                print(f"{indent}Leaf node found, added {root.val}")
            
            # Recurse left
            collect_leaf_values(root.left, leaf_values, depth + 1)
            
            # Recurse right
            collect_leaf_values(root.right, leaf_values, depth + 1)
            
            print(f"{indent}Returning from node {root.val}")

        leaf_values1 = []
        leaf_values2 = []

        print("Traversing root1:")
        collect_leaf_values(root1, leaf_values1)
        print("Leaf values of root1:", leaf_values1)
        print("\nTraversing root2:")
        collect_leaf_values(root2, leaf_values2)
        print("Leaf values of root2:", leaf_values2)

        return leaf_values1 == leaf_values2


# Example usage
if __name__ == "__main__":
    # Small test tree
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(4, TreeNode(2), TreeNode(3))

    sol = Solution()
    print("\nAre leaf sequences similar?", sol.leafSimilar(root1, root2))
