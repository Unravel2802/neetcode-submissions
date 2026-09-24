class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string = encoded_string + (str(len(s)) + '#' + s)
    
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            nxt = idx
            string_length = ''
            while s[nxt] != '#':
                string_length += s[nxt]
                nxt += 1
            length = int(string_length)
            res.append(s[nxt + 1 : nxt + length + 1])
            idx = nxt + length + 1
        
        return res 