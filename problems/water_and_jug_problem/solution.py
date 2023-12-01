class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        q, seen = deque([0]), set()
        steps = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]

        while q:
            curr = q.popleft()

            for step in steps:
                amount = curr + step

                if amount == targetCapacity:
                    return True
                
                if amount not in seen and 0 <= amount <= jug1Capacity + jug2Capacity:
                    seen.add(amount)
                    q.append(amount)
        
        return False

        
        