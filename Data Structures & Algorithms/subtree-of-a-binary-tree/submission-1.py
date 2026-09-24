# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Questions:
        # 1. Can root be None? Can the subroot be None?
        # 2. Can the values of the nodes be duplicated?
        
        # Solution: using recursion and bfs
        # First traverse the tree until we find a value that is the same with
        # the root of the subroot
        # Then check if that structure matches with the subroot

        # helper function for checking similar trees
        def sameTree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            # if we reach the end for both trees, we return true
            if not tree1 and not tree2:
                return True
            # if one has children and the other doesn't, we return false
            if not tree1 or not tree2:
                return False
            # if the tree node values are not equal, return fasle
            if tree1.val != tree2.val:
                return False
            
            # checking for both left and right subtrees of tree1 and tree2
            return sameTree(tree1.left, tree2.left) and sameTree(tree1.right, tree2.right)

        if not subRoot:
            return True
        if not root:
            return False
        # bfs for getting to the subroot
        q = deque([root])

        # while the queue still has any node left
        while q:
            cur = q.popleft()
            # if the current node value is equal to the root of the subroot,
            # we check if the subroot starting from current not is equal to
            # the subroot 
            if sameTree(cur, subRoot):
                return True

            # append 
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    
        return False