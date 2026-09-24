"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}

        # 1st pass: make a copy of each node
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 2nd pass: assign next and random pointers
        cur = head
        while cur:
            copy_node = old_to_new[cur]
            copy_node.next = old_to_new.get(cur.next)
            copy_node.random = old_to_new.get(cur.random)
            cur = cur.next
        
        return old_to_new[head]