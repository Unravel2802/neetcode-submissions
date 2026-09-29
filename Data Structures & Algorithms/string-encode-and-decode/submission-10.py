class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        length = ""
        while i < len(s):
            while s[i] != "#":
                length += s[i]
                i += 1
            
            word_length = int(length)
        
            res.append(s[i + 1 : i + word_length + 1])
            i += word_length + 1
            length = ""
        return res