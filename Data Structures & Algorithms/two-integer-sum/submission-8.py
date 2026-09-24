class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Idea: hash map

        Approach:
        - Create a hashmap of the numbers that we have gone through and their index
        - for loop for each number -> find complement -> check if in hash map
        '''

        mp = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in mp:
                return [mp[comp], i]
        
            mp[num] = i
    