class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        num_counts = defaultdict(int)

        for num in nums:
            num_counts[num] += 1
        
        nums.sort()

        for num in nums:
            if num_counts[num] == 0:
                continue
            
            for i in range(k):
                curr_num = num + i

                if num_counts[curr_num] == 0:
                    return False
                
                num_counts[curr_num] -= 1
        
        return True
        