class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        mp = {}
        max_len = 0 # longest consecutive sequence length

        for num in nums:
            if num - 1 in mp:
                mp[num] = mp[num - 1] + 1
            else:
                mp[num] = 1
            
            max_len = max(max_len, mp[num])
    
        return max_len