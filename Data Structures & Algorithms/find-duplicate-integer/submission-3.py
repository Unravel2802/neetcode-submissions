class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Idea:
        # Treat the array like a linked list:
        # index -> next index = nums[index]
        # Since one number is duplicated, two indices point to the same next node,
        # which creates a cycle. Use Floyd's cycle detection to find the entry point
        # of the cycle (the duplicate number).
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast] 

        return slow