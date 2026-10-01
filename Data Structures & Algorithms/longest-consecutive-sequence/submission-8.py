class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        longest = 0
        nums.sort()
        for num in nums:
            if (num - 1) in mp:
                mp[num] = mp[num - 1] + 1
            else:
                mp[num] = 1

            longest = max(longest, mp[num])
    
        return longest