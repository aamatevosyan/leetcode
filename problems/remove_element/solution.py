class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start_index = 0

        for num in nums:
            if num == val:
                continue

            nums[start_index] = num
            start_index += 1
        
        return start_index