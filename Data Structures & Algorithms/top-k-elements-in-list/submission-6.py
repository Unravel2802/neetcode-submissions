class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count_frequency = Counter(nums)

        max_frequency = max(count_frequency.values())
        buckets = [[] for _ in range(max_frequency + 1)]
        for num, frequency in count_frequency.items():
            buckets[frequency].append(num)
        
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                if k > 0:
                    res.append(num)
                    k -= 1
        
        return res 