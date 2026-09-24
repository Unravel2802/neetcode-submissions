class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def signature(s):
            c = [0] * 26
            for ch in s:
                c[ord(ch) - ord('a')] += 1
            return tuple(c)

        groups = defaultdict(list)

        for s in strs:
            groups[signature(s)].append(s)

        return list(groups.values())