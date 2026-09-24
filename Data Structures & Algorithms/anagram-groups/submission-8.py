class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def group(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            return tuple(count)
        
        res = defaultdict(list)
        for s in strs:
            res[group(s)].append(s)

        return list(res.values()) 



