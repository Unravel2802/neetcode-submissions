class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = cost[0]
        prev2 = cost[1]

        for i in range(2, len(cost)):
            temp = prev2
            prev2 = min(prev1, prev2) + cost[i]
            prev1 = temp

        return min(prev1, prev2)