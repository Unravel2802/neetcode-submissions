from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = defaultdict(int)
        for num in nums: 
            dic[num] += 1
    
        sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        keys = list(sorted_dic.keys())
        return keys[:k]