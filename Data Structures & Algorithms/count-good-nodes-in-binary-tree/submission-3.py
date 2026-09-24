# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0 
            
            count = 0 

            if node.val >= maxVal:
                maxVal = node.val
                count += 1
            
            return count + dfs(node.left, maxVal) + dfs(node.right, maxVal)
    
        return dfs(root, float('-inf'))