class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            buckets[value].append(key)
    
        print(buckets)
        res = []
        for i in range(len(nums), -1, -1):
            bucket = buckets[i]
            for num in bucket:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
            
        return res 