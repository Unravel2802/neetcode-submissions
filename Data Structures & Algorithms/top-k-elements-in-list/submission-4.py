from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        res = []
        for num in nums:
            dic[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, val in dic.items():
            print(key, val)
            bucket[val].append(key)
            print(bucket)

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
