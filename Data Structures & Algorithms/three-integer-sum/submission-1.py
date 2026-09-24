from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Can I take 5 minutes to think?
        # All triplets that sums up to 0 
        # The result is a list of triplets lists, no duplicates
        res = []     
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if triplet not in res:
                            res.append(triplet)
                    k += 1
                j += 1
            i += 1

        return res