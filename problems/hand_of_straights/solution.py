from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        num_counts = defaultdict(int)

        for num in hand:
            num_counts[num] += 1
        
        hand.sort()

        for num in hand:
            if num_counts[num] == 0:
                continue
            
            for i in range(groupSize):
                curr_num = num + i

                if num_counts[curr_num] == 0:
                    return False
                
                num_counts[curr_num] -= 1
        
        return True
