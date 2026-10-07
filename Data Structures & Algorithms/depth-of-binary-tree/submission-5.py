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

            return 1 + max(max_depth, dfs(node.left), dfs(node. right))
        
        return dfs(root)