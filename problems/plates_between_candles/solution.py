class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i in range(len(s)) if s[i] == "|"]
        print(candles)
        result = []

        for q_left, q_right in queries:
            left_pos, right_pos = -1, -1

            l, r = 0, len(candles) - 1
            while l <= r:
                m = l + (r - l) // 2
                
                if candles[m] >= q_left:
                    left_pos = m
                    r = m - 1
                else:
                    l = m + 1
            
            if left_pos == -1:
                result.append(0)
                continue
            
            l, r = 0, len(candles) - 1
            while l <= r:
                m = l + (r - l) // 2
                
                if candles[m] <= q_right:
                    right_pos = m
                    l = m + 1
                else:
                    r = m - 1
            
            if right_pos == -1 or right_pos <= left_pos:
                result.append(0)
                continue
                
            result.append(candles[right_pos] - candles[left_pos] - right_pos + left_pos)
        
        return result
                
        