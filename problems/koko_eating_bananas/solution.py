class Solution:
    def can_eat_piles(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0
        for pile in piles:
            hours += ceil(pile / k) 

            if hours > h:
                return False
        
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2 

            if self.can_eat_piles(piles, h, m):
                r = m - 1
            else:
                l = m + 1
        
        return l
        