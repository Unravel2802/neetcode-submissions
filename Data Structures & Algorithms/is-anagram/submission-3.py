class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_frequency = defaultdict(int)
        for char in s:
            count_frequency[char] += 1
        
        for char in t:
            count_frequency[char] -= 1
        
        for char, frequency in count_frequency.items():
            if frequency != 0:
                return False
        
        return True