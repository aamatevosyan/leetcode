class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
            
        start, end = nums[0], nums[0]
        result = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                end += 1
            else:
                if end == start:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                
                start, end = nums[i], nums[i]
        
        if end == start:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        
        return result
