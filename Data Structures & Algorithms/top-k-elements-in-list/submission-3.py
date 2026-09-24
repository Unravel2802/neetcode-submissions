class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        res = []

        for num in nums:
            dic[num] += 1

        s = sorted(dic.items(), key = lambda d: d[1], reverse = True)

        for i in range(k):
            print(s[i])
            res.append(s[i][0])
        return res