# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p1, p2):
            if not p1 and not p2:
                return True 
            elif p1 and p2 and p1.val == p2.val:
                return dfs(p1.left, p2.left) and dfs(p1.right, p2.right)
            else:
                return False
            
        return dfs(p, q)
