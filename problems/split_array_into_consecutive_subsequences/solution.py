from collections import defaultdict, Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        subsequence = defaultdict(int)

        for num in nums:
            if num_count[num] == 0:
                continue
            
            if subsequence[num - 1] > 0:
                subsequence[num - 1] -= 1
                subsequence[num] += 1
            else:
                if num_count[num + 1] == 0 or num_count[num + 2] == 0:
                    return False
                
                num_count[num + 1] -= 1
                num_count[num + 2] -= 1

                subsequence[num + 2] += 1
            
            num_count[num] -= 1
        
        return True

        