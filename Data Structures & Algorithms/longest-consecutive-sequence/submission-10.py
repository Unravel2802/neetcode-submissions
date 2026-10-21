class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        maxLength = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                maxLength = max(maxLength, mp[num])
        return maxLength