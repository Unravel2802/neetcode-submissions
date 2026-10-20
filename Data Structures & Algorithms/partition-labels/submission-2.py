class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Keep adding to the current substring until all the letters in the current substring
        # do not appear elsewhere
        count = Counter(s)
        res = []
        cur = {}
        l = 0

        for c in s:
            l += 1
            if c not in cur:
                cur[c] = count[c]
        
            cur[c] -= 1
            
            if cur[c] == 0:
                cur.pop(c)
            
            if cur == {}:
                res.append(l)
                l = 0
    
        return res
