class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            length = ''
            while s[j] != '#':
                length += s[j]
                j += 1
            
            length = int(length)
            res.append(s[j + 1 : j + length + 1])
            i = j + length + 1        
        return res 
            
