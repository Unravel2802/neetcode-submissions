class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        cur = 0
        jump = 0
        
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == cur:
                jump += 1
                cur = furthest 

        return jump