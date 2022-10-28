class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev, future, ans = -1, 0, 0

        for i in range(len(seats)):
            if seats[i] == 1:
                prev = i
            else:
                while (future < len(seats) and seats[future] == 0) or future < i:
                    future += 1
                
                left = len(seats) if prev == -1 else i - prev
                right = len(seats) if future == len(seats) else future - i
                ans = max(ans, min(left, right))
        
        return ans
