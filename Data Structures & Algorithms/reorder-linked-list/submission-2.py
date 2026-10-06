# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 3 Steps: find two halves, reverse the second half, merge

        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev
        first = head

        # 3. Merge
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1 

            first = temp1
            second = temp2
        













