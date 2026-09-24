# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Idea:
        # Traverse every node in root.
        # For each node, check whether the subtree starting there is exactly the same as subRoot.
        # "Same tree" means same value and same structure.
        def sameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        if not subRoot:
            return True
        if not root:
            return False

        q = deque([root])

        while q:
            node = q.popleft()
            if sameTree(node, subRoot):
                return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False
