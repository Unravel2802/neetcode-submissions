from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def signature(s):
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord("a")] += 1
            return tuple(cnt)

        groups = defaultdict(list)
        for s in strs:
            groups[signature(s)].append(s)
        
        return list(groups.values())
