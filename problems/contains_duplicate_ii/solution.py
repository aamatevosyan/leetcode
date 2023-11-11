class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, window = 0, set()
        
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            
            if nums[r] in window:
                return True
            
            window.add(nums[r])
        
        return False
        