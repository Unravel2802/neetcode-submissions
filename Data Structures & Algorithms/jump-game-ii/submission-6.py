class Solution:
    def jump(self, nums: List[int]) -> int:
        nxtEnd = 0
        curEnd = 0
        jump = 0
        
        for i in range(len(nums) - 1):
            nxtEnd = max(nxtEnd, i + nums[i])

            if i == curEnd:
                jump += 1
                curEnd = nxtEnd 

        return jump