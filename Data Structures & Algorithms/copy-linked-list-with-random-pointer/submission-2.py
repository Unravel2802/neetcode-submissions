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

        dummy = head
        while dummy:
            old_to_new[dummy] = Node(dummy.val)
            dummy = dummy.next

        dummy = head
        while dummy:
            copy_node = old_to_new[dummy] 
            copy_node.next = old_to_new.get(dummy.next)
            copy_node.random = old_to_new.get(dummy.random)
            dummy = dummy.next
        
        return old_to_new[head]
