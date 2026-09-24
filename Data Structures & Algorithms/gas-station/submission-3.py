class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        cur_gas = 0 
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i] 
            total_gas += gain
            cur_gas += gain

            if cur_gas < 0:
                cur_gas = 0
                start = i + 1
        
        return start if total_gas >= 0 else -1