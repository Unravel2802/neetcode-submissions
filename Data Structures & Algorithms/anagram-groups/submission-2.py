class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagrams(str1, str2):
            dic = defaultdict(int)
            for c in str1:
                dic[c] += 1
            
            for c in str2:
                dic[c] -= 1

            for key, value in dic.items():
                if value != 0:
                    return False

            return True

        res = []
        n = len(strs)
        grouped = [False for i in range(n)]

        for i in range(n):
            add = False
            if not grouped[i]:
                add = True
                grouped[i] = True
                group = [strs[i]]

            for j in range(i + 1, n):
                if not grouped[j]:
                    if isAnagrams(strs[i], strs[j]):
                        group.append(strs[j])
                        grouped[j] = True

            if add:
                res.append(group)

        return res 