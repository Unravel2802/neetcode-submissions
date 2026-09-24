class Solution:
    # Idea:
    # Greedy range of possible open parentheses counts.
    # low  = minimum possible number of unmatched '('
    # high = maximum possible number of unmatched '('
    #
    # For each char:
    # '(' -> low += 1, high += 1
    # ')' -> low -= 1, high -= 1
    # '*' -> it can be '(', ')' or empty
    #        so low -= 1, high += 1
    #
    # low can never go below 0 because we cannot have negative unmatched '('.
    # If high < 0 at any point, we have too many ')' and cannot recover.
    # In the end, low must be 0 for a valid assignment.
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0