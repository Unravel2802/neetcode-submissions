class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        dic = defaultdict(int)

        if n1 > n2:
            return False

        for ch in s1:
            dic[ch] += 1
        
        # need to keep track of left and right index as we move
        # the window is the length of s1
        # use a dictionary to keep track of the letters frequencies 
        # in the substring
        for i in range(n1):
            dic[s2[i]] -= 1

        if max(dic.values()) == 0:
            return True
            
        for i in range(n1, n2):
            dic[s2[i]] -= 1
            dic[s2[i-n1]] += 1
            if max(dic.values()) == 0:
                return True
            
        return False
