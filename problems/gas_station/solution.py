class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index, total_gas, current_gas, total_cost = 0, 0, 0, 0

        for i in range(len(gas)):
            _gas, _cost = gas[i], cost[i]
            total_gas += _gas
            total_cost += _cost

            current_gas += (_gas - _cost)
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        
        if total_gas < total_cost:
            start_index = -1

        return start_index