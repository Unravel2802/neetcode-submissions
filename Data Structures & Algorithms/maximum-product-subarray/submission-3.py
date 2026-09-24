class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Idea:
        # Keep track of the maximum and minimum ending at each position
        # The minimum is needed because multiplying by a negative number can 
        # turn it into a new maxium

        curMax = nums[0]
        curMin = nums[0]
    
        res = nums[0]

        for num in nums[1:]:
            tmpMax = max(num, num * curMax, num * curMin)
            tmpMin = min(num, num * curMax, num * curMin)
        
            curMax = tmpMax
            curMin = tmpMin
        
            res = max(res, curMax)
        
        return res