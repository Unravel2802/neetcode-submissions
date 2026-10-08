# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0 
        def dfs(node):
            nonlocal max_depth 

            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            max_depth = max(left, right)

            return 1 + max_depth
        
        return dfs(root)