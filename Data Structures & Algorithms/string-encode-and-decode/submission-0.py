class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            for ch in s:
                encoded_string = encoded_string + str(ord(ch)) + ","
            encoded_string += "." 
        print(encoded_string)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            word = ""
            while s[i] != ".":
                char = ""
                while s[i] != ",":
                    char += s[i]
                    i += 1
                word += str(chr(int(char)))
                i += 1
            res.append(word)
            i += 1
        return res    
