class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1 

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1



        result = bin_search(0, l - 1)
        if result != -1:
            return result
        return bin_search(l, len(nums) - 1)