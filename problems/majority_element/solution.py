class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count, current_num = 0, 0

        for num in nums:
            if max_count == 0:
                current_num = num
            
            max_count += 1 if num == current_num else -1
        
        return current_num
