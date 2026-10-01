class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        mp = {}
        longest = 0
        for num in nums:
            if (num - 1) in mp:
                mp[num] = mp[num - 1] + 1
            else:
                mp[num] = 1

            longest = max(longest, mp[num])
    
        return longest