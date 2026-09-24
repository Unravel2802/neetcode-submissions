from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        res = []
        for num in nums:
            dic[num] += 1 

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in dic.items():
            bucket[freq].append(num)
        
        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                res.append(num)

        return res[:k]