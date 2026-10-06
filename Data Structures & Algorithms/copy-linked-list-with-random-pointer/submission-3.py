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
        
        # Create a dictionary with the old node and new copy as key-value
        oldToNew = {}

        # Fill the dictionary
        old = head
        while old:
            oldToNew[old] = Node(old.val)
            old = old.next
        
        old = head
        while old:
            oldToNew[old].next = oldToNew.get(old.next)
            oldToNew[old].random = oldToNew.get(old.random)

            old = old.next
        
        return oldToNew[head]

