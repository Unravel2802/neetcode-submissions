class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        if digits[n] == 9:
            while digits[n] == 9:
                digits[n] = 0
                n -= 1
            if digits[n] == 0:
                digits.append(0)
                digits[0] += 1
            else:
                digits[n] += 1
        else: 
            digits[-1] += 1
        return digits