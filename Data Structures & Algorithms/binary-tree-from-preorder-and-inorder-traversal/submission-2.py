# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Idea:
        # preorder -> tells us the root of the current subtree immediately
        # inorder  -> tells us how to split that subtree into left and right parts
        #
        # So we:
        # 1. Take the next value from preorder as root
        # 2. Find that value in inorder
        # 3. Recursively build the left subtree
        # 4. Recursively build the right subtree
        #
        # Using a hashmap for inorder indices makes the split O(1),
        # so the whole solution is O(n).
        inorder_index = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx

            # no nodes in this inorder range
            if left > right:
                return None

            # next preorder value is the root
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            # split inorder into left subtree and right subtree
            mid = inorder_index[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)