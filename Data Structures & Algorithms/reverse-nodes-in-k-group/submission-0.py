# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node, count = head, 0
        while node and count < k:
            node = node.next
            count += 1
        if count < k: 
            return head      # fewer than k nodes left

        prev = self.reverseKGroup(node, k)  # reverse rest first
        for _ in range(k):
            nxt       = head.next
            head.next = prev
            prev      = head
            head      = nxt
        return prev